# -*- coding: utf-8 -*-
"""Advanced_heart_disease_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pVn5y6xaM7WHe-r7tR4JtZ3cfLZn1v8I

Data Extraction, Transformation, and Loading (ETL)
"""

import pandas as pd
df = pd.read_csv('heart.csv')
df.head()

# Check for missing values
print(df.isnull().sum)

# Drop rows with missing values (if any)
df = df.dropna()

# Display the info of the DataFrame
print(df.info())

# Data Transformation
df.fillna(df.mean(), inplace=True)
df = pd.get_dummies(df, drop_first=True)

# Feature Scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df.drop('target', axis=1))

# Creating the final DataFrame
df_final = pd.DataFrame(scaled_features, columns=df.columns[:-1])
df_final['target'] = df['target']

df_final.to_csv('cleaned_heart_disease_data.csv', index=False)

"""Step 2: Exploratory Data Analysis (EDA)"""

import seaborn as sns
import matplotlib.pyplot as plt

# Correlation Matrix
plt.figure(figsize=(12, 8))
sns.heatmap(df_final.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Heart Disease Data')
plt.show()

# Distribution of Target Variable
plt.figure(figsize=(8, 6))
sns.countplot(df_final['target'])
plt.title('Distribution of Heart Disease')
plt.show()

# Boxplot by Age
plt.figure(figsize=(10, 6))
sns.boxplot(x='target', y='age', data=df_final)
plt.title('Age vs. Heart Disease')
plt.show()

# Pairplot to examine relationships between features
sns.pairplot(df_final, hue='target', diag_kind='kde')
plt.show()

"""Additional Plots for Enhanced Visualization"""

# Histogram of Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df_final['age'], kde=True, bins=30)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Heatmap of Missing Values
plt.figure(figsize=(10, 6))
sns.heatmap(df_final.isnull(), cbar=False, cmap='viridis')
plt.title('Heatmap of Missing Values')
plt.show()

# Pairwise Relationships of Selected Features
selected_features = ['age', 'chol', 'thalach', 'cp', 'target']
sns.pairplot(df_final[selected_features], hue='target')
plt.suptitle('Pairwise Relationships of Selected Features', y=1.02)
plt.show()

# Density Plot for Cholesterol Levels by Heart Disease Status
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df_final, x='chol', hue='target', fill=True)
plt.title('Density Plot of Cholesterol Levels by Heart Disease Status')
plt.xlabel('Cholesterol')
plt.ylabel('Density')
plt.show()

# Violin Plot for Maximum Heart Rate by Heart Disease Status
plt.figure(figsize=(10, 6))
sns.violinplot(x='target', y='thalach', data=df_final)
plt.title('Violin Plot of Max Heart Rate by Heart Disease Status')
plt.xlabel('Heart Disease')
plt.ylabel('Max Heart Rate')
plt.show()

"""Histogram of Age Distribution: Shows how ages are distributed across the dataset.

Heatmap of Missing Values: Displays missing data, if any.

Pairwise Relationships: Examines relationships between selected features.

Density Plot: Visualizes the distribution of cholesterol levels for different heart disease statuses.

Violin Plot: Combines boxplot and KDE plot to show data distribution for maximum heart rate.

Advanced Modeling

Objective: Train and evaluate a machine learning model to predict heart disease.
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Splitting the dataset into training and testing sets
X = df_final.drop('target', axis=1)
y = df_final['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Training a RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions and Evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

"""Advanced Visualization with Plotly
Objective: Create interactive visualizations using Plotly.
"""

import plotly.express as px

"""Scatter Plot: Shows the relationship between age and maximum heart rate.
Boxplot: Compares cholesterol levels across different heart disease statuses.

"""

# Scatter plot for Age vs. Max Heart Rate
fig = px.scatter(df_final, x='age', y='thalach', color='target',
                 labels={'thalach':'Max Heart Rate', 'target':'Heart Disease'})
fig.update_layout(title='Age vs. Max Heart Rate by Heart Disease')
fig.show()

# Boxplot for Cholesterol levels by Heart Disease
fig = px.box(df_final, x='target', y='chol', color='target',
             labels={'chol':'Cholesterol', 'target':'Heart Disease'})
fig.update_layout(title='Cholesterol Levels by Heart Disease')
fig.show()

"""
Dataset Feature Display"""

# Display basic information about the dataset
def display_dataset_info(df):
    print("Dataset Information:")
    print(df.info())
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    print("\nSummary Statistics:")
    print(df.describe())
    print("\nCorrelation Matrix:")
    print(df.corr())

display_dataset_info(df_final)

# Feature Summary Table
def feature_summary(df):
    print("Feature Summary:")
    summary = df.describe().transpose()
    print(summary)

feature_summary(df_final)

import pandas as pd
from sklearn.preprocessing import StandardScaler

df_final = pd.read_csv('cleaned_heart_disease_data.csv')

# Features and Target
X = df_final.drop('target', axis=1)
y = df_final['target']

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions and Evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

