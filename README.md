# 🏀 NBA Player Performance Predictor

A machine learning project predicting NBA player performance using **RandomForestRegressor** and **Linear Regression** models.

## 📊 Overview
This project uses synthetic historical NBA data (minutes played, FG%, 3PT%, rebounds, assists, etc.) to predict **Points Per Game (PPG)**.  
It applies preprocessing, scaling, cross-validation, and visualization of predicted vs. actual performance.

## ⚙️ Technologies
- Python
- Pandas / NumPy
- Scikit-learn
- Matplotlib / Seaborn

## 🚀 How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/ziontop/nba-performance-predictor.git
   cd nba-performance-predictor

## Dataset
Uses 2023-2024 NBA Regular Season player statistics from Kaggle.

**Features used for prediction:**
- Minutes Played (MP)
- Field Goal % (FG%)
- 3-Point % (3P%)
- Free Throw % (FT%)
- Total Rebounds (TRB)
- Assists (AST)
- Steals (STL)
- Blocks (BLK)
- Turnovers (TOV)

## Results
- Random Forest R²: ~0.95+ (highly accurate)
- RMSE: ~1-2 points per game

## How to Run
1. Clone the repository
```bash
git clone https://github.com/ziontop/nba-performance-predictor.git
```

2. Install dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

3. Run the script
```bash
python nba_predictor.py
```

## Future Improvements
- Add more seasons of data
- Predict other stats (rebounds, assists)
- Deploy as a web app
- Include player position as a feature

## License
MIT License
```

**requirements.txt** (lists required packages):
```
pandas
numpy
matplotlib
seaborn
scikit-learn
```

**.gitignore** (tells git what NOT to upload):
```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/

# Data files (optional - if CSV is large)
*.csv

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
>>>>>>> 3ca77d22afbe9d2038d3a329308b5c3871858f60
