import pandas as pd

def preprocess_data(data):
    """
    Preprocesses and engineers features to reduce noise in the data.
    """
    # Drop irrelevant features based on domain knowledge
    filtered_data = data.drop(columns=['noisy_feature_1', 'noisy_feature_2', 'irrelevant_feature'])

    # Feature engineering: Create new relevant features
    filtered_data['network_traffic_ratio'] = filtered_data['inbound_traffic'] / (filtered_data['outbound_traffic'] + 1)
    
    return filtered_data
