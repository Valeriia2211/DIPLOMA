import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

df = df.dropna(how='all')
df = df.dropna(subset=['Athlete_ID'])

indices = [
    'Strength_Index',
    'Endurance_Index',
    'Balance_Index'
]

for col in indices:

    counts = (
        df[col]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(12,5))

    counts.plot(
        kind='bar'
    )

    plt.title(f'{col} Distribution')

    plt.xlabel(col)

    plt.ylabel('Number of Athletes')

    plt.tight_layout()

    plt.show()