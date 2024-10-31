from logging_config import set_logging_level
import logging

# Example threshold for threat detection
THRESHOLD = 0.8

def preprocess_data(input_data):
    # Preprocess the input data for the model
    # (Assuming preprocessing steps are already defined here)
    return input_data  # Modify as per preprocessing requirements

def predict_threat(input_data):
    # Log input data at DEBUG level for detailed analysis
    logging.debug(f"Received input data for prediction: {input_data}")

    # Step 1: Preprocess data (Example preprocessing step)
    preprocessed_data = preprocess_data(input_data)
    logging.debug(f"Preprocessed data: {preprocessed_data}")

    # Step 2: Model prediction with confidence score
    prediction, confidence_score = model.predict(preprocessed_data)
    logging.info(f"Prediction: {prediction}, Confidence Score: {confidence_score}")

    # Step 3: Check for threshold to flag as a threat
    if prediction == 'threat' and confidence_score > THRESHOLD:
        logging.warning(f"Threat flagged with confidence score: {confidence_score}")
        reason = "Confidence score exceeds threshold"
    else:
        reason = "Confidence score below threshold"
    
    logging.debug(f"Decision Reason: {reason}")
    return prediction, confidence_score

