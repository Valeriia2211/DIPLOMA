import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

df = df.dropna(how='all')
df = df.dropna(subset=['Athlete_ID'])

level_counts = df['Sport_Level'].value_counts()

plt.figure(figsize=(10,5))

level_counts.plot(
    kind='bar'
)

plt.title('Sport Level Distribution')

plt.xlabel('Sport Level')

plt.ylabel('Number of Athletes')

plt.tight_layout()

plt.show()