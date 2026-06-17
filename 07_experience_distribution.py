import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

df = df.dropna(how='all')
df = df.dropna(subset=['Athlete_ID'])

experience_counts = (
    df['Experience_Years']
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(10,5))

experience_counts.plot(
    kind='bar'
)

plt.title('Experience Distribution')

plt.xlabel('Experience (Years)')

plt.ylabel('Number of Athletes')

plt.tight_layout()

plt.show()