import pandas as pd

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

print("Кількість рядків:")
print(len(df))

print("\nУнікальних Athlete_ID:")
print(df["Athlete_ID"].nunique())

print("\nМаксимальний Athlete_ID:")
print(df["Athlete_ID"].max())

print("\nМінімальний Athlete_ID:")
print(df["Athlete_ID"].min())