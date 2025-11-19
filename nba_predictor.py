import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# -------------------------------------------------------------------------
# STEP 1: Load and clean dataset
# -------------------------------------------------------------------------
# FIX: Specify semicolon as delimiter
df = pd.read_csv("2023-2024 NBA Player Stats - Regular.csv", encoding="latin1", sep=";")

# Show sample
print("Raw Data Sample:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())

# Keep relevant numeric features
features = [
    'MP', 'FG%', '3P%', 'FT%', 'TRB', 'AST', 'STL', 'BLK', 'TOV'
]
target = 'PTS'  # Points per game
player_names = df['Player']

# Remove rows with missing or invalid values
df = df.dropna(subset=features + [target])

# Convert percentage columns from strings to floats if needed
for col in ['FG%', '3P%', 'FT%']:
    if df[col].dtype == 'object':
        df[col] = pd.to_numeric(df[col], errors='coerce')

X = df[features]
y = df[target]

# -------------------------------------------------------------------------
# STEP 2: Scale and split data
# -------------------------------------------------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test, names_train, names_test = train_test_split(
    X_scaled, y, player_names, test_size=0.2, random_state=42
)

# -------------------------------------------------------------------------
# STEP 3: Train models
# -------------------------------------------------------------------------
rf = RandomForestRegressor(n_estimators=300, random_state=42)
lr = LinearRegression()

rf.fit(X_train, y_train)
lr.fit(X_train, y_train)

# -------------------------------------------------------------------------
# STEP 4: Evaluate
# -------------------------------------------------------------------------
rf_preds = rf.predict(X_test)
lr_preds = lr.predict(X_test)

rf_r2 = r2_score(y_test, rf_preds)
lr_r2 = r2_score(y_test, lr_preds)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_preds))

print(f"\nRandom Forest R²: {rf_r2:.3f}, RMSE: {rf_rmse:.3f}")
print(f"Linear Regression R²: {lr_r2:.3f}")

cv_rf = np.mean(cross_val_score(rf, X_scaled, y, cv=5))
print(f"Cross-validated Random Forest R²: {cv_rf:.3f}")

# Feature importance
feature_importance = pd.DataFrame({
    'feature': features,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)
print("\nFeature Importance:")
print(feature_importance)

# -------------------------------------------------------------------------
# STEP 5: Visualization (with player names)
# -------------------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=rf_preds, color='royalblue', s=60)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual PPG")
plt.ylabel("Predicted PPG")
plt.title("NBA Player Performance Prediction")

# Annotate top players
for i, name in enumerate(names_test):
    if abs(y_test.iloc[i] - rf_preds[i]) < 2:  # label accurate predictions
        plt.text(y_test.iloc[i], rf_preds[i], name.split()[0], fontsize=8)

plt.tight_layout()
plt.show()