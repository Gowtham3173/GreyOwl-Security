import model
import data_preprocessing

def run_inference(input_data):
    processed_data = data_preprocessing.preprocess_data(input_data)
    predictions = model.predict(processed_data)
    return predictions
