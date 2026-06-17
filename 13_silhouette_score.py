import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

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

for k in range(2, 8):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(X_scaled)

    score = silhouette_score(
        X_scaled,
        labels
    )

    print(
        f"k = {k}, Silhouette Score = {score:.4f}"
    )