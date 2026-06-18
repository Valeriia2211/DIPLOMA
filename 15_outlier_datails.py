import pandas as pd

from sklearn.linear_model import LinearRegression

# показувати всі колонки
pd.set_option('display.max_columns', None)

# показувати широку таблицю
pd.set_option('display.width', 1000)

# не обрізати ширину колонок
pd.set_option('display.max_colwidth', None)

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

df = df.dropna(how='all')
df = df.dropna(subset=['Athlete_ID'])

# модель

X = df[['Strength_Index']]
y = df['Final_Score']

model = LinearRegression()

model.fit(X, y)

# прогноз

df['Predicted_Score'] = model.predict(X)

# відхилення

df['Deviation'] = (
    df['Final_Score']
    - df['Predicted_Score']
)

df['Abs_Deviation'] = (
    df['Deviation']
    .abs()
)

# ТОП-10 найбільш незвичайних спортсменів

outliers = df.sort_values(
    by='Abs_Deviation',
    ascending=False
)

print(
    outliers[
        [
            'Athlete_ID',
            'Sport_Level',
            'Experience_Years',
            'Training_Load',
            'Strength_Index',
            'Endurance_Index',
            'Balance_Index',
            'Final_Score',
            'Predicted_Score',
            'Deviation'
        ]
    ].head(10).to_excel(
        "top10_Outliers.xlsx",
        index=False
    ))