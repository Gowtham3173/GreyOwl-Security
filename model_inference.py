# Set a threshold for classification to reduce false positives
ADJUSTED_THRESHOLD = 0.7

def classify_threat(probability):
    """
    Classify whether a given input probability represents a threat.
    """
    return 1 if probability >= ADJUSTED_THRESHOLD else 0
