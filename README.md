# 🏡House Sales Prices Data of USA (May 2014-May 2015)
**Business Problem -** Real Estate Investment Trust would like to start investing in Residential real estate.
                       Want to determining the market price of a house by features of house.
## **Goal -** Determine the sale price of house and Find key insights.
## **Role -** As data Analyst analyze house sale price data and find insights.
## 🔍Key findings from this project: 
- Deployed Machine learning model to help predict house price.
-	Condition of House is not affection price as expected.
-	Square footage of the home and overall grade given to the housing unit, based on USA grading system dominate more to price 
-	Square footage of house apart from basement is also positively impact on price.
-	House which has a view to a waterfront or more expensive than the other.
## Methodes used
- **Data Wrangling-**
  - Droped unusefull columns like['Unnamed: 0','id']
  - Checked null values replaced them with the mean of column
  - Check data types and correct them
- **Exploratory Data Analysis**
  - Analyzed each column check value counts of each
  - Checked correlation of each feature with price by using pandas corr() method  
- **Data visualization**
  - Used visualizations libraries like matplotlib and seaborn
  - Used visualizations like barplot,regplot from seaborn library.
  - Used matplotlib pyplot to add lables and titles to visualizations.  - 
- **Model Development**
  - Used scikit learn library to develop model
  - Used different types regression such as LinearRegression,Ridge,Lasso,RandomForestRegressor,DecisionTreeRegressor,XGBRegressor.
  - Used Model selection tool like train_test_split with the 80 % data for training and 20 % for testing.
  - Calculate training and testing score by using .score().
- **Model Evaluation and Refinement**
  - From model selection of scikit learn used cross_val_score with cv=5 and scoring ='r2'
  - From metrics of scikit learn used mean_squared_error,r2_score of models.
  - From model selection of scikit learn used GridSearchCV to find best Best Parameters for the selected model.
  - From pipeline and preprocessing of scikit learn used pipeline and StandardScaler to improve model performance.
- **Model Deployment**
  - By using joblib create pkl file of the developed model.
  - Model stored at Google drive so by using requests,os,joblib model download in the app
  - Used streamlit library do create layout.
  - Used streamlit functions such as selectbox,number_input,button,write,title,divider.
  - Github repository is used to store app.py file and requiremets.txt
  - Streamlit cloud is used to host app. 
## 🛠️Key skills used in this project:
**Python Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Plotly Dash,os,gdown.
**Other Tools:** Github, Streamlit Cloud, Google Colab.

**Conslusion -** Deployed regression machine learning model where they just select the and enter the details of the house then then model will predict its price.
                Provide key finding to help decision making.

## USA House Price Prediction Model App Link:
**App Link=**https://datascienceskills-txkesgndkbtq49cq36bk7g.streamlit.app/
