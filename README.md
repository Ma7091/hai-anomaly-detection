# Isolation Forest Anomaly Detection (HAI Dataset)

This project implements an **Isolation Forest model** to detect anomalies in industrial control system sensor data using the **HAI dataset**.

The goal is to identify abnormal behavior or cyber attacks in industrial sensor readings.

---

## Method

The anomaly detection pipeline follows these steps:

1. Load training and testing sensor data
2. Remove the timestamp column
3. Normalize sensor values using `StandardScaler`
4. Train an **Isolation Forest** model on normal system data
5. Detect anomalies in the test dataset
6. Evaluate the results using **precision, recall, and F1-score**

---

## Model Configuration

The Isolation Forest model uses the following parameters:

- `n_estimators = 200`
- `contamination = 0.05`
- `random_state = 42`

Isolation Forest works by isolating rare observations in the dataset, which are likely to be anomalies.

---

## Example Output

Running the model produces a classification report like this:
precision recall f1-score support

0 0.95 0.98 0.97 51019
1 0.21 0.07 0.11 2981

accuracy 0.93


### Explanation

| Metric | Meaning |
|------|------|
Precision | Percentage of predicted anomalies that are correct |
Recall | Percentage of actual attacks detected |
F1-score | Balance between precision and recall |
Accuracy | Overall prediction accuracy |

Class labels:

- **0 = Normal system behavior**
- **1 = Attack / anomaly**

The model performs well at detecting normal behavior but detecting attacks is more challenging due to the **imbalanced dataset**.

---

## Dataset

This project uses the **HAI Industrial Control System Dataset**.

Download it from:

https://github.com/icsdataset/hai

After downloading, place the folders like this:


---

## Installation
Install required Python libraries:

pip install -r requirements.txt


---

## Running the Model
Run the script with:

python models/simple_iso_forest.py


The program will train the Isolation Forest model and print the evaluation results.

---

## Author

Isolation Forest implementation for anomaly detection in industrial sensor data.




