#  SpaceX_Falcon9_first_stage_Landing_Prediction

## 📌 Project Overview
To determmine the price of each lounch by gathering information about spaceX.To determine this, have to determine wether the spaceX will Reuse the first stage of falcon 9 rocket beacuse first stage holds 50-60 percent cost of overall rocket.

## 💼 Business Problem
In this capstone, we will predict if the Falcon 9 first stage will land successfully. SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage.SpaceY company want to compite spaceX in the race of space.
Stages:-
Fairings  - Carries Payloads
Stage Two - Help Payload the Fairings to bring the Payload to Orbit.
Stage One - Most of the work done by first stage.
## 🎯 Goal
- Predict the first stage of falcon9 Rocket will land sucessfully or Not land.
- Identify key factors influencing landing outcome.

## 🔍 Key Findings
- ES-L1, GEO, HEO, SSO, Orbits has most success rate.
- Max Load carried out by Falcon9 rocket is 3726 kg.
- NASA is also client of spaceX with 32 lounches.

## 📂 Dataset Information
- Data Collected using spaceX api with the help of requests.
- Web scraping using BeautifulSoup to get Falcon 9 and Falcon Heavy Launches Records from Wikipedia
## 🛠️ Methodology
### 1. Data Wrangling
- Dropped unnecessary columns.
- Checked and corrected data types.
- Handled missing values.

### 2.Feature Engeneering
- Created Class column using outcome to determing success or failure.

### 2. Exploratory Data Analysis (EDA)
- Load data in sqlite3 to query data for key findings.
- Visualized trends using **Seaborn**,**Folium**and **Matplotlib**.

### 3. Data Visualization
- Plots used: `barplot`, `catplot` (Seaborn), `lineplot` and custom charts with Matplotlib.
- Folium World map,Folium marker cluster to visualize location with the outcome sign red or green

### 4. Model Development
- Models tested: `LogisticRegression`, `SVC`, `DecisionTreeClassifier`, `KNeighborsClassifier`.
- Train-test split: 80% training, 20% testing.
- Selected Model: **LogisticRegression**
- Best Parameters (via GridSearchCV): {'C': 0.01, 'penalty': 'l2', 'solver': 'lbfgs'}
- Performance: **R² Score = 0.94**

### 5. Model Evaluation
- Metrics: `r2_score`
- Cross-validation: `cross_val_score(cv=5, scoring='r2')`

### 6. Deployment
- Model saved as `.pkl` using **joblib**.
- Integrated with **Streamlit** for interactive web app.
- Hosted on **Streamlit Cloud**.

## 🌐 App Link
[SpaceX_Falcon9_First_Stage_Landing_Prediction_model](https://datascienceskills-q36rxhcunb7g9aj57krg9j.streamlit.app/)

## 🛠️ Tech Stack
- **Languages & Libraries**: Python, BeautifulSoup, Pandas, NumPy, Matplotlib, Seaborn, folium, Scikit-learn, Streamlit.
- **Tools**: Google Colab, GitHub, Streamlit Cloud

## 📌 Conclusion
- LogisticRegression with tuned parameters achieved **R² = 0.94**.
- Key drivers of price: Orbit and PayloadMass.
- Deployed an interactive app for real-time predictions.
