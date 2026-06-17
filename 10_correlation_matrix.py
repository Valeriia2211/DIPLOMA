import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

df = df.dropna(how='all')
df = df.dropna(subset=['Athlete_ID'])

selected = [

    'Age',

    'Experience_Years',

    'Training_Load',

    'Strength_Index',

    'Endurance_Index',

    'Balance_Index',

    'Final_Score'

]

plt.figure(figsize=(10,8))

sns.heatmap(
    df[selected].corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title(
    'Correlation Matrix of Key Indicators'
)

plt.tight_layout()

plt.show()