import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

df = df.dropna(how='all')
df = df.dropna(subset=['Athlete_ID'])

age_counts = df['Age'].value_counts().sort_index()

plt.figure(figsize=(10,5))

age_counts.plot(
    kind='bar'
)

plt.title('Age Distribution')

plt.xlabel('Age')

plt.ylabel('Number of Athletes')

plt.tight_layout()

plt.show()