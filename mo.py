import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor

# =========================
# 1. LOAD DATA
# =========================
df = pd.read_csv("clean.csv")

# =========================
# 2. HANDLE DATE COLUMN
# =========================
df['Date'] = pd.to_datetime(df['Date'])

df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day

df.drop('Date', axis=1, inplace=True)

# =========================
# 3. SPLIT FEATURES & TARGETS
# =========================
X = df.drop(['Risk_Score', 'Mortality_Rate', 'Risk_Level'], axis=1)
y = df[['Risk_Score', 'Mortality_Rate']]

# =========================
# 4. FIX OBJECT (STRING) COLUMNS
# =========================
X = pd.get_dummies(X)

# =========================
# 5. TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 6. TRAIN MODEL (XGBOOST)
# =========================
model = XGBRegressor(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    random_state=42
)

model.fit(X_train, y_train)

# =========================
# 7. PREDICTION
# =========================
pred = model.predict(X_test)

risk_score_pred = pred[:, 0]
mortality_pred = pred[:, 1]

# =========================
# 8. EVALUATION
# =========================
print("Risk Score MSE:", mean_squared_error(y_test['Risk_Score'], risk_score_pred))
print("Mortality MSE:", mean_squared_error(y_test['Mortality_Rate'], mortality_pred))

# =========================
# 9. RISK LEVEL (DERIVED)
# =========================
def get_risk_level(score):
    if score < 30:
        return "Low"
    elif score < 70:
        return "Medium"
    else:
        return "High"

risk_level_pred = [get_risk_level(s) for s in risk_score_pred]

# =========================
# 10. FINAL OUTPUT
# =========================
results = pd.DataFrame({
    "Pred_Risk_Score": risk_score_pred,
    "Pred_Mortality_Rate": mortality_pred,
    "Pred_Risk_Level": risk_level_pred
})

print(results.head())