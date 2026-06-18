import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

# Видалення порожніх рядків
df = df.dropna(how='all')

# Перелік індексів
indices = [
    'Strength_Index',
    'Endurance_Index',
    'Balance_Index'
]

# Побудова графіків
for col in indices:

    # Перетворення в числовий формат
    df[col] = pd.to_numeric(df[col], errors='coerce')

    plt.figure(figsize=(8, 5))

    plt.hist(
        df[col].dropna(),
        bins=10,
        edgecolor='black'
    )

    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Number of Athletes')

    plt.grid(axis='y', alpha=0.3)

    plt.tight_layout()

    plt.savefig(f'{col}_distribution.png', dpi=300)

    plt.show()