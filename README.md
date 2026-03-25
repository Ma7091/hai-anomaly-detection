# Isolation Forest Anomaly Detection (HAI Dataset)

This project implements an **Isolation Forest model** to detect anomalies in industrial control system sensor data using the **HAI dataset**.

The goal is to identify abnormal behavior or cyber attacks in industrial sensor readings.
This implementation represents the **anomaly detection component of a Digital Twin monitoring system**.

---

# Digital Twin Anomaly Detection Pipeline

This project is part of a **Digital Twin architecture** for monitoring industrial systems.

The pipeline works as follows:

```
Sensor Data → Digital Twin Model → Prediction Error → Isolation Forest → Attack Detection
```

* **Sensor Data**: Industrial sensor readings from the HAI dataset
* **Digital Twin Model**: Represents normal system behavior
* **Prediction Error**: Difference between expected and observed system behavior
* **Isolation Forest**: Detects abnormal patterns in the data
* **Attack Detection**: Flags potential cyber attacks or system anomalies

The HAI dataset simulates real industrial control system operations and cyber attack scenarios.

---

# Method

The anomaly detection pipeline follows these steps:

1. Load training and testing sensor data
2. Remove the timestamp column
3. Normalize sensor values using `StandardScaler`
4. Train an **Isolation Forest** model on normal system data
5. Detect anomalies in the test dataset
6. Evaluate results using **precision, recall, and F1-score**

---

# Model Configuration

The Isolation Forest model uses the following parameters:

* `n_estimators = 200`
* `contamination = 0.05`
* `random_state = 42`

Isolation Forest detects anomalies by isolating rare observations that differ from normal patterns.

---

# Example Output

Running the model produces a classification report similar to:

```
precision    recall  f1-score   support

0       0.95      0.98      0.97     51019
1       0.21      0.07      0.11      2981

accuracy                           0.93
```

### Explanation of Metrics

| Metric    | Description                                        |
| --------- | -------------------------------------------------- |
| Precision | Percentage of predicted anomalies that are correct |
| Recall    | Percentage of actual attacks detected              |
| F1-score  | Balance between precision and recall               |
| Accuracy  | Overall prediction accuracy                        |

Class labels:

* **0 = Normal system behavior**
* **1 = Attack / anomaly**

Because the dataset is **highly imbalanced**, detecting attacks is more difficult than detecting normal behavior.

---

# Dataset

This project uses the **HAI Industrial Control System Dataset**.

Download the dataset from:

https://github.com/icsdataset/hai

After downloading, place the dataset folders in the project directory as follows:

```
project-folder/
│
├── models/
│   └── simple_iso_forest.py
│
├── hai-23.05/
│   ├── hai-train1.csv
│   └── hai-test1.csv
│
└── haiend-23.05/
    └── label-test1.csv
```

----The dataset is **not included in this repository** due to its large size----

---

# Project Structure

```
hai-anomaly-detection/
│
├── models
│   └── simple_iso_forest.py
│
├── README.md
└── requirements.txt
```

---

# Installation

Install required Python libraries:

```
pip install -r requirements.txt
```

---

# Running the Model

Run the script with:

```
python models/simple_iso_forest.py
```

The program will train the Isolation Forest model and print the evaluation results.

---

# Author
#Mar
Isolation Forest implementation for anomaly detection in industrial sensor data within a Digital Twin monitoring framework.
