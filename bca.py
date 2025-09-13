import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from scipy import stats

# ---- Load Iris dataset ----
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print("Iris Dataset (first 5 rows):\n", df.head())

# ---- Select Sepal features ----
sepal_df = df[['sepal length (cm)', 'sepal width (cm)']]

# ---- Compute Z-scores ----
z_scores = np.abs(stats.zscore(sepal_df))
print("\nZ-scores for Sepal features (first 5 rows):\n", z_scores[:5])

# ---- Detect Outliers (threshold = 2) ----
threshold = 2
outliers = sepal_df[(z_scores > threshold).any(axis=1)]

print("\nOutliers detected (threshold = 2):")
print(outliers)
