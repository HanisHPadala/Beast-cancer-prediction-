# Breast Cancer Prediction

This repository contains a machine learning project aimed at predicting breast cancer diagnoses using the Breast Cancer Wisconsin dataset. The project utilizes Python and various data science libraries to analyze and predict whether a tumor is malignant or benign.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Modeling and Evaluation](#modeling-and-evaluation)

## Project Overview
The primary goal of this project is to build a predictive model that classifies tumors as malignant or benign based on features extracted from images of fine needle aspirate (FNA) of breast masses. By analyzing cell characteristics, we can use machine learning techniques to assist in early diagnosis.

## Dataset
The dataset used is the [Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data), available on Kaggle. The features represent cell characteristics, while the target label indicates malignancy or benignity.

### Features
- **Mean Radius**: Mean of distances from the center to points on the perimeter
- **Mean Texture**: Standard deviation of gray-scale values
- **Mean Perimeter** and more...

## Installation
To run this project, clone this repository and install the required dependencies.

```bash
git clone https://github.com/your-username/breast-cancer-prediction.git
cd breast-cancer-prediction
pip install -r requirements.txt

## Usage
1. **Download the Dataset**: The Breast Cancer Wisconsin dataset can be downloaded from Kaggle. Ensure you have your Kaggle API credentials set up.
   - Save your Kaggle API keys in environment variables named `KAGGLE_USERNAME` and `KAGGLE_KEY`.
   - Run the following commands to download and unzip the dataset:
   ```bash
   !kaggle datasets download -d uciml/breast-cancer-wisconsin-data
   !unzip /path/to/breast-cancer-wisconsin-data.zip

## Modeling and Evaluation

This project uses a structured approach for building and evaluating machine learning models for breast cancer prediction:

### Data Preprocessing
- **Handling Missing Values**: Columns with missing values are dropped to ensure clean data.
- **Feature Scaling**: Numerical features are normalized to improve model convergence and performance.
- **Encoding**: Categorical labels, such as the target (malignant/benign), are encoded for compatibility with the model.

### Model Training
Various machine learning models are trained and tested to identify the best-performing model for this dataset, including:
- **Logistic Regression**: A probabilistic approach that works well for binary classification problems.
- **Decision Trees**: A non-parametric model that builds a tree-like structure based on decision rules.
- **Support Vector Machines (SVM)**: A robust model for binary classification, particularly effective with high-dimensional data.

Each model is evaluated based on performance metrics to determine its suitability for predicting breast cancer diagnoses.

### Model Evaluation
To measure the effectiveness of each model, the following metrics are used:

- **Accuracy**: The percentage of correct predictions out of the total predictions.
- **Precision**: The ratio of correctly predicted positive observations to the total predicted positive observations, measuring the quality of positive predictions.
- **Recall (Sensitivity)**: The ratio of correctly predicted positive observations to all actual positives, showing how well the model captures positive cases.
- **F1 Score**: The harmonic mean of precision and recall, providing a single metric that balances both measures, especially useful for imbalanced datasets.
- **Confusion Matrix**: A matrix that shows the breakdown of true positive, true negative, false positive, and false negative predictions, allowing for a deeper understanding of model performance.

Through these metrics, the best-performing model is selected, helping provide reliable breast cancer predictions based on the Wisconsin dataset.

