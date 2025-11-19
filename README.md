# NBA Player Performance Predictor

A machine learning project that predicts NBA player points per game (PPG) based on performance statistics.

## Features
- Predicts player scoring using Random Forest and Linear Regression models
- Analyzes 2023-2024 NBA season data
- Visualizes prediction accuracy with scatter plots

## Technologies Used
- Python 3.x
- pandas, numpy
- scikit-learn (Machine Learning)
- matplotlib, seaborn (Visualization)

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
git clone https://github.com/YOUR_USERNAME/nba-performance-predictor.git
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
