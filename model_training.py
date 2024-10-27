from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

def train_model(X_train, y_train):
    """
    Trains the model with hyperparameter tuning to reduce false positives.
    """
    # Define hyperparameter grid for fine-tuning
    param_grid = {
        'n_estimators': [50, 100, 150],
        'max_depth': [10, 15, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'class_weight': ['balanced']  # To address class imbalance
    }

    # Perform grid search for best parameters with focus on precision
    grid_search = GridSearchCV(estimator=RandomForestClassifier(), param_grid=param_grid, scoring='precision')
    grid_search.fit(X_train, y_train)

    # Return the best model after tuning
    best_model = grid_search.best_estimator_

    return best_model
