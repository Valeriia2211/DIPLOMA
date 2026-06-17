import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_excel(
    "Таблиця Основні фізичні показники спортсменів.xlsx"
)

df = df.dropna(how='all')
df = df.dropna(subset=['Athlete_ID'])

features = [

    'Age',

    'Experience_Years',

    'Training_Load',

    'Strength_Index',

    'Endurance_Index',

    'Balance_Index'

]

X = df[features]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

wcss = []

for k in range(1, 11):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    wcss.append(
        kmeans.inertia_
    )

plt.figure(figsize=(8,5))

plt.plot(
    range(1,11),
    wcss,
    marker='o'
)

plt.title(
    'Elbow Method'
)

plt.xlabel(
    'Number of Clusters'
)

plt.ylabel(
    'WCSS'
)

plt.grid(True)

plt.show()