import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_excel("Таблиця Основні фізичні показники спортсменів.xlsx")

columns = [
    'Age',
    'Experience_Years',
    'Training_Load',
    'Strength_Index',
    'Endurance_Index',
    'Balance_Index',
    'Final_Score'
]

print(df[columns].describe().round(2).T)

