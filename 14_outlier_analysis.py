import pandas as pd

from sklearn.linear_model import LinearRegression

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

# очищення

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

# абсолютне відхилення

df['Abs_Deviation'] = (
    df['Deviation']
    .abs()
)

# найбільш незвичайні спортсмени

outliers = df.sort_values(
    by='Abs_Deviation',
    ascending=False
)

print(
    outliers[
        [
            'Athlete_ID',
            'Sport_Level',
            'Strength_Index',
            'Endurance_Index',
            'Balance_Index',
            'Final_Score',
            'Predicted_Score',
            'Deviation'
        ]
    ].head(10)
)