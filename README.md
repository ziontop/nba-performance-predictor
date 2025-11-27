# 🏀 NBA Player Performance Predictor

A machine learning project that predicts NBA player points per game (PPG) based on performance statistics using Random Forest and Linear Regression models.

📊 Project Overview
This project analyzes 2023-2024 NBA season data to predict player scoring performance with high accuracy (~95% R² score). The model uses key performance metrics like shooting percentages, rebounds, assists, and playing time to make predictions.
Key Features

🎯 Dual Model Approach: Implements both Random Forest and Linear Regression for comparison
📈 High Accuracy: Achieves R² score of ~0.95+ with RMSE of 1-2 PPG
📉 Visual Analysis: Generates scatter plots comparing predicted vs actual values
🔍 Feature Importance: Analyzes which stats most impact scoring predictions

🚀 Getting Started
Prerequisites

Python 3.8 or higher
pip package manager

Installation

Clone the repository

bashgit clone https://github.com/ziontop/nba-performance-predictor.git
cd nba-performance-predictor

Create a virtual environment (recommended)

bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

bashpip install -r requirements.txt

Add your dataset

Download the 2023-2024 NBA Season Stats from Kaggle
Place the CSV file in the project directory
Update the filename in nba_predictor.py if needed



Usage
Run the predictor:
bashpython nba_predictor.py
The script will:

Load and preprocess the NBA stats data
Train Random Forest and Linear Regression models
Display model performance metrics (R², RMSE, MAE)
Generate visualization plots showing prediction accuracy

📈 Model Performance
ModelR² ScoreRMSEMAERandom Forest~0.95+1-2 PPG~1 PPGLinear Regression~0.90+2-3 PPG~1.5 PPG

📊 Sample Visualization

![Prediction vs Actual](prediction_plot.png)
*Scatter plot showing predicted vs actual PPG with high correlation (R² ~0.95)*

🔢 Features Used
The model predicts PPG based on these statistics:

MP - Minutes Played per game
FG% - Field Goal Percentage
3P% - Three-Point Percentage
FT% - Free Throw Percentage
TRB - Total Rebounds per game
AST - Assists per game
STL - Steals per game
BLK - Blocks per game
TOV - Turnovers per game

📁 Project Structure
nba-performance-predictor/
│
├── nba_predictor.py          # Main prediction script
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── LICENSE                   # MIT License
├── .gitignore               # Git ignore rules
│
└── data/                    # (Not tracked - add your CSV here)
    └── nba_stats_2023-24.csv
🛠️ Technologies Used

Python 3.8+: Core programming language
pandas: Data manipulation and analysis
numpy: Numerical computing
scikit-learn: Machine learning models and evaluation
matplotlib: Data visualization
seaborn: Statistical data visualization

📊 Sample Output
Random Forest Model Performance:
R² Score: 0.941
RMSE: 1.45 PPG
MAE: 0.98 PPG

Linear Regression Model Performance:
R² Score: 0.889
RMSE: 2.13 PPG
MAE: 1.52 PPG

Top 3 Most Important Features:
1. Minutes Played (MP): 45.2%
2. Field Goal % (FG%): 23.8%
3. Assists (AST): 12.4%
🚧 Future Improvements

 Add more seasons of historical data for trend analysis
 Predict additional stats (rebounds, assists, steals)
 Deploy as an interactive web application (Flask/Streamlit)
 Include player position and team as features
 Implement hyperparameter tuning for optimal performance
 Add player injury history as a feature
 Create API endpoint for real-time predictions

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

NBA statistics data sourced from Kaggle
Inspiration from sports analytics and machine learning communities
scikit-learn documentation and examples

📧 Contact
Zina Okoye - https://github.com/ziontop/
Project Link: https://github.com/ziontop/nba-performance-predictor

⭐ If you found this project helpful, please consider giving it a star!
