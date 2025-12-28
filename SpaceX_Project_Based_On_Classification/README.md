# 🚀 SpaceX Falcon 9 First Stage Landing Prediction
### 📌 Project Overview
- The cost of a SpaceX Falcon 9 launch is approximately $62 million, significantly lower than competitors charging upwards of $165 million. This cost advantage comes primarily from reusing the first stage, which accounts   for 50–60% of the total rocket cost.
- This project predicts whether the Falcon 9 first stage will successfully land, enabling cost estimation and strategic insights for companies like SpaceY, aiming to compete with SpaceX.

### 💼 Business Problem
- SpaceX’s ability to reuse the first stage is a game-changer in the space industry. Predicting landing success helps estimate launch costs and optimize mission planning.
- **Objective:**  Build a predictive model to determine if the Falcon 9 first stage will land successfully based on mission parameters.

### 🎯 Goals

- Predict landing success of Falcon 9 first stage.
- Identify key factors influencing landing outcomes.
- Provide actionable insights for cost estimation and competitive strategy.


### 🔍 Key Insights

- Orbits like ES-L1, GEO, HEO, SSO have the highest success rates.
- Maximum payload carried by Falcon 9: 5000 kg.
- NASA is a major client with 32 launches.


### 📂 Dataset

**Source:**

- SpaceX API (via requests)
- Wikipedia Falcon 9 & Falcon Heavy launch records (via BeautifulSoup)


- Storage: SQLite database for efficient querying.


### 🛠️ Methodology
 **1. Data Wrangling**

  - Removed irrelevant columns.
  - Corrected data types.
  - Handled missing values.

 **2. Feature Engineering**

  - Created Class column (Success = 1, Failure = 0).

 **3. Exploratory Data Analysis**

  - Queried data using SQLite.
  - Visualized trends with Seaborn, Matplotlib, and Folium.

 **4. Data Visualization**

  - Seaborn: barplot, catplot, lineplot
  - Matplotlib: Custom charts
  - Folium: World map with marker clusters (green = success, red = failure)

 **5. Model Development**

  **Models tested:**
  - `LogisticRegression`, `SVC`, `DecisionTreeClassifier`, `KNeighborsClassifier`.
  - Train-test split: 80/20
  - Best Model: Logistic Regression

  **Tuned via GridSearchCV**
  - Best Params: {'C': 0.01, 'penalty': 'l2', 'solver': 'lbfgs'}


  **Performance:**
  
  - R² Score = 0.94
  - Cross-validation: cv=5



**6. Deployment**

- Model saved as .pkl using joblib.
- Integrated with Streamlit for interactive web app.
- Hosted on Streamlit Cloud.


### 🌐 Live App
- Deployed Streamlit app - https://datascienceskills-l6mckmftcxrfvnxk2dhgpv.streamlit.app/

### 🛠️ Tech Stack

- Languages & Libraries: Python, Pandas, NumPy, BeautifulSoup, Matplotlib, Seaborn, Folium, Scikit-learn, Streamlit
- Tools: Google Colab, GitHub, Streamlit Cloud
## Created PowerBI Dashboard To Visualize Insights 
<img width="1333" height="745" alt="image" src="https://github.com/user-attachments/assets/045d97d2-763e-4ef6-9e72-72705e709c0a" />


### ✅ Conclusion

- Logistic Regression achieved R² = 0.94 after hyperparameter tuning.
- Orbit type and Payload mass are key drivers of landing success.
- Deployed an interactive app for real-time predictions.
