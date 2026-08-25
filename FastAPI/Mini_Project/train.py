from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd 
import joblib

data = fetch_california_housing()
x = pd.DataFrame(data.data,columns = data.feature_names)
y = data.target

X_train,X_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)
model = RandomForestRegressor(n_estimators = 100,random_state = 42)
model.fit(X_train,y_train)
y_pred = model.predict(X_test) #Returns a numpy array


print("R2 Score:",r2_score(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))

joblib.dump(model,"house_model.pkl")
joblib.dump(list(x.columns),"house_features.pkl")
