#  SpaceX_Falcon9_first_stage_Landing_Prediction

## 📌 Project Overview
To determmine the price of each lounch by gathering information about spaceX.To determine this, have to determine wether the spaceX will Reuse the first stage of falcon 9 rocket beacuse first stage holds 50-60 percent cost of overall rocket.

## 💼 Business Problem
SpaceX adverties falcon9 rocket lounch with $62 million cost.While other providers cost $165 million.
Stages:-
Fairings  - Carries Payloads
Stage Two - Help Payload the Fairings to bring the Payload to Orbit.
Stage One - Most of the work done by first stage.
Unlike other providers spaceX falcon9 can recover the first stage.Sometimes the first stage does not land,it will crash other times spaceX will sacrifies first stage due to mission parameters like Payload,Orbit and Customer.
SpaceY company want to compite spaceX in the race of space.

## 🎯 Goal
- Predict the first stage of falcon9 Rocket will land sucessfully or Not land.
- Identify key factors influencing landing outcome.

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
- **Languages & Libraries**: Python, BeautifulSoup, Pandas, NumPy, Matplotlib, Seaborn, folium, Scikit-learn, Plotly Dash
- **Tools**: Google Colab, GitHub, Streamlit Cloud

## 📌 Conclusion
- RandomForestRegressor with tuned parameters achieved **R² = 0.78**.
- Key drivers of price: Square footage, grade, and waterfront view.
- Deployed an interactive app for real-time predictions.
