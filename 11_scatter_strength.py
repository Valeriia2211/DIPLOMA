import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

df = df.dropna(how='all')

plt.scatter(
    df['Strength_Index'],
    df['Final_Score']
)

plt.title(
    'Strength Index vs Final Score'
)

plt.xlabel(
    'Strength Index'
)

plt.ylabel(
    'Final Score'
)

plt.show()