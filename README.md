#  SpaceX_Falcon9_first_stage_Landing_Prediction

## 📌 Project Overview
This project predicts house sale prices in the USA using machine learning models. It involves data cleaning, exploratory data analysis (EDA), feature engineering, model development, evaluation, and deployment via Streamlit.

## 💼 Business Problem
SpaceY company want to A Real Estate Investment Trust (REIT) wants to start investing in residential properties. The goal is to determine the market price of a house based on its features to make informed investment decisions.

## 🎯 Goal
- Predict the sale price of a house.
- Identify key factors influencing house prices.

## 🔍 Key Findings
- **Condition of the house** does not affect price as much as expected.
- **Square footage** and **overall grade** dominate price prediction.
- Houses with **waterfront views** are significantly more expensive.
- Square footage apart from the basement also positively impacts price.

## 📂 Dataset Information
- Timeframe: May 2014 – May 2015
- Columns cleaned: Dropped `['Unnamed: 0', 'id']`
- Missing values handled by replacing with column mean.

## 🛠️ Methodology
### 1. Data Wrangling
- Dropped unnecessary columns.
- Checked and corrected data types.
- Handled missing values.

### 2. Exploratory Data Analysis (EDA)
- Analyzed feature distributions and correlations using `pandas.corr()`.
- Visualized trends using **Seaborn** and **Matplotlib**.

### 3. Data Visualization
- Plots used: `barplot`, `regplot` (Seaborn), and custom charts with Matplotlib.

### 4. Model Development
- Models tested: `LinearRegression`, `Ridge`, `Lasso`, `DecisionTreeRegressor`, `RandomForestRegressor`, `XGBRegressor`.
- Train-test split: 80% training, 20% testing.
- Selected Model: **RandomForestRegressor**
- Best Parameters (via GridSearchCV): `max_depth=30`, `n_estimators=300`
- Performance: **R² Score = 0.78**

### 5. Model Evaluation
- Metrics: `mean_squared_error`, `r2_score`
- Cross-validation: `cross_val_score(cv=5, scoring='r2')`

### 6. Deployment
- Model saved as `.pkl` using **joblib**.
- Integrated with **Streamlit** for interactive web app.
- Hosted on **Streamlit Cloud**.

## 🌐 App Link
[SpaceX_Falcon9_First_Stage_Landing_Prediction_model](https://datascienceskills-q36rxhcunb7g9aj57krg9j.streamlit.app/)

## 🛠️ Tech Stack
- **Languages & Libraries**: Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost, Plotly Dash
- **Tools**: Google Colab, GitHub, Streamlit Cloud

## 📌 Conclusion
- RandomForestRegressor with tuned parameters achieved **R² = 0.78**.
- Key drivers of price: Square footage, grade, and waterfront view.
- Deployed an interactive app for real-time predictions.
