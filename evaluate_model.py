from sklearn.metrics import classification_report

def evaluate_model(model, X_test, y_test):
    """
    Evaluates model performance, focusing on precision to minimize false positives.
    """
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=['Non-Threat', 'Threat'])
    
    print("Classification Report After Optimization:")
    print(report)

    # Specific focus on precision for "Threat" class
    threat_precision = report['Threat']['precision']
    print(f"Threat Detection Precision: {threat_precision}")

