import pandas as pd

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

print("До очищення:")
print(df.shape)

# Видалення повністю порожніх рядків
df = df.dropna(how='all')

# Видалення рядків без Athlete_ID
df = df.dropna(subset=['Athlete_ID'])

print("\nПісля очищення:")
print(df.shape)

print("\nПропуски:")
print(df.isnull().sum())