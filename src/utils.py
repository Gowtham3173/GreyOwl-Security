def calculate_false_positive_rate(y_true, y_pred):
    false_positives = sum((y_pred == 1) & (y_true == 0))
    total_negatives = sum(y_true == 0)
    return false_positives / total_negatives if total_negatives > 0 else 0
