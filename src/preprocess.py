import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(data):
    # Remove duplicates and null values
    data = data.drop_duplicates().dropna()

    # Feature scaling
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    return pd.DataFrame(scaled_data, columns=data.columns)
