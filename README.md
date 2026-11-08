# 💧 Water Quality Prediction Using Machine Learning

## 📌 Project Overview

This project uses Machine Learning to predict whether water is suitable for drinking based on its physicochemical properties. It applies the **K-Nearest Neighbors (KNN)** classification algorithm and uses **GridSearchCV** to identify the best number of neighbors for the model.

The project also includes Exploratory Data Analysis (EDA), feature visualization, data standardization, model evaluation, and model serialization.

## 🎯 Objectives

- Analyze water quality parameters through Exploratory Data Analysis.
- Identify patterns and relationships between water properties.
- Standardize numerical features using StandardScaler.
- Train a KNN classification model.
- Optimize the number of neighbors using GridSearchCV.
- Evaluate model performance using classification metrics.
- Save the trained model and scaler for future use.

## 📂 Dataset

**Dataset:** `water_quality_potability.csv`

The dataset contains water quality measurements and a target variable called `Potability`.

### Features

| Feature | Description |
|---|---|
| pH | Measures the acidity or alkalinity of water |
| Hardness | Represents dissolved calcium and magnesium |
| Solids | Total dissolved solids in water |
| Chloramines | Chloramine concentration |
| Sulfate | Sulfate concentration |
| Conductivity | Electrical conductivity of water |
| Organic_carbon | Organic carbon concentration |
| Trihalomethanes | Trihalomethane concentration |
| Turbidity | Measures water clarity |

**Target Variable:**
- `0` – Non-potable water
- `1` – Potable water

## 🛠️ Technologies and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Pickle
- Streamlit

## 🔍 Exploratory Data Analysis (EDA)

The project performs several visualization and analysis operations to understand the dataset.

### Visualizations Included

1. Correlation heatmap to examine relationships between features.
2. pH distribution visualization.
3. Histograms of water quality parameters.
4. Average hardness by water potability.
5. Average pH by potability.
6. Boxplots for numerical features.
7. Violin plot for solids distribution.
8. Pairplot to explore relationships between features.
9. Countplot to compare potable and non-potable water samples.

## ⚙️ Data Preprocessing

The following preprocessing steps are implemented:

- Loading the dataset using Pandas.
- Applying `StandardScaler` to standardize numerical values.
- Converting the standardized data into a Pandas DataFrame.
- Separating input features (`X`) and target variable (`y`).
- Splitting the dataset into training and testing sets.

**Train-Test Split:**
- Training data: 80%
- Testing data: 20%
- Random state: 42

## 🤖 Machine Learning Model

### K-Nearest Neighbors (KNN)

The project uses the KNN classification algorithm to predict water potability.

KNN classifies a new sample based on the majority class among its nearest neighboring samples.

### Hyperparameter Optimization

`GridSearchCV` is used to find the optimal value of `n_neighbors`.

**Search Configuration:**
- Algorithm: KNeighborsClassifier
- Parameter: `n_neighbors`
- Search range: 1–20
- Cross-validation: 5 folds

## 📊 Model Evaluation

The trained model is evaluated using the following metrics:

- **Accuracy Score:** Measures the proportion of correct predictions.
- **Precision Score:** Measures how many predicted potable samples are actually potable.
- **F1 Score:** Calculates the harmonic mean of precision and recall.

The code prints these evaluation metrics after testing the model.

*Actual performance values can be added after running the complete notebook.*

## 🔮 Water Quality Prediction

The project demonstrates predictions on unseen water-quality samples using the trained KNN model.

The prediction output is interpreted as:

- `0`: Quality of the water is NOT Drinkable.
- `1`: Quality of the water is Drinkable.

## 💾 Model Saving

The trained model and scaler are saved for future use.

```python
import pickle

pickle.dump(model, open("waterQuality.sav", "wb"))
pickle.dump(scaler, open("scaler.sav", "wb"))
```

Saved files:

- `waterQuality.sav` – Trained KNN/GridSearchCV model.
- `scaler.sav` – StandardScaler object.

## 🚀 Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/water-quality-prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd water-quality-prediction
```

### 3. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
```

### 4. Run the Project

Run the Jupyter Notebook to perform data analysis, train the model, and evaluate predictions.

```bash
jupyter notebook
```

The shared Streamlit code currently initializes a page title. A complete interactive prediction interface would require additional input fields, loading the saved model and scaler, and displaying the prediction.

## 📁 Project Structure

```text
Water-Quality-Prediction/
│
├── water_quality_potability.csv
├── Water_Quality_Prediction.ipynb
├── waterQuality.sav
├── scaler.sav
├── README.md
│
└── requirements.txt
```

## ⚠️ Important Technical Notes

Before publishing the project as a polished machine-learning implementation, consider these improvements:

1. **Data Leakage:** The current code applies `StandardScaler` to the complete dataset before splitting it. Fit the scaler only on training data, then transform the test data.
2. **Target Scaling:** The current code scales the `Potability` target along with the input features. Scale only the input features.
3. **Pipeline:** Use a Scikit-learn Pipeline with `StandardScaler` and `KNeighborsClassifier` inside `GridSearchCV` to ensure preprocessing is performed correctly during cross-validation.
4. **Missing Values:** Check and handle missing values before model training.
5. **Streamlit Interface:** The provided Streamlit section only displays a title; a complete prediction interface has not yet been implemented.

## 👨‍💻 Author

**Muhammad Idrees**  
AI & Machine Learning Developer

Interested in Machine Learning, Deep Learning, Computer Vision, NLP, and AI-powered applications.

⭐ If you find this project useful, consider giving the repository a star!
