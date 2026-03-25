import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# Load data
train = pd.read_csv("C:/Users/...../OneDrive/Desktop/hai-23.05/hai-train1.csv")
test  = pd.read_csv("C:/Users/...../OneDrive/Desktop/hai-23.05/hai-test1.csv")
labels = pd.read_csv("C:/Users/..../OneDrive/Desktop/haiend-23.05/label-test1.csv")

# Remove timestamp
X_train = train.drop(columns=["timestamp"])
X_test  = test.drop(columns=["timestamp"])

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# Train Isolation Forest
model = IsolationForest(
    n_estimators=200,
    contamination=0.05,
    random_state=42
)

model.fit(X_train)

# Predict
pred = model.predict(X_test)

# Convert predictions (-1 anomaly → 1 attack)
pred = [1 if p == -1 else 0 for p in pred]

# True labels
y_true = labels["label"]

# Evaluation
print(classification_report(y_true, pred))
