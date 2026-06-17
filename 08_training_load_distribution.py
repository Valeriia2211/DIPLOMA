import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

df = df.dropna(how='all')
df = df.dropna(subset=['Athlete_ID'])

load_counts = (
    df['Training_Load']
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(10,5))

load_counts.plot(
    kind='bar'
)

plt.title('Training Load Distribution')

plt.xlabel('Training Load')

plt.ylabel('Number of Athletes')

plt.tight_layout()

plt.show()