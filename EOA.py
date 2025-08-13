import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Veri set yükleme
df = pd.read_csv('Veri.csv')  # Kendi veri setinizin yolunu belirtin

# 1. Basit bilgi
print("Shape of data:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())

# 2. Ortalama, medyan, varyans gibi özet istatistikler
print("\nSummary statistics:\n", df.describe())

# 3. Eksik değerlerin kontrolü
print("\nMissing values:\n", df.isnull().sum())
df_filled = df.fillna(df.mean(numeric_only=True))

print("\nMissing values after filling:\n", df_filled.isnull().sum())

# 4. Veri dağılımı görselleştirmeleri
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()

# 5. Korelasyon matrisi
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
corr = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 6. Çift değişkenli ilişkiler
sns.pairplot(df[numeric_cols].dropna())
plt.show()
