import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

df = df.dropna(how='all')
df = df.dropna(subset=['Athlete_ID'])

gender_counts = df['Gender'].value_counts()

plt.figure(figsize=(7,5))

gender_counts.plot(
    kind='bar'
)

plt.title('Gender Distribution')

plt.xlabel('Gender')

plt.ylabel('Number of Athletes')

plt.tight_layout()

plt.show()