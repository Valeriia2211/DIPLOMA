import pandas as pd

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

print(df.head())

print("\nРозмір датасету:")
print(df.shape)

print("\nНазви колонок:")
print(df.columns.tolist())