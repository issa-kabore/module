from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, explained_variance_score, max_error
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score, f1_score, roc_curve

from module import LOGGER


#  regression/classif metrics.py
def get_metrics(predictions, actual_values, model_type: str = "regression"):
    metrics = dict()
    if model_type.lower().startswith("reg"):
        LOGGER.info(f"Retrieving 'regression' metrics")
        # reg_metrics = ['r2', 'rmse', 'mse', 'mae', 'explained_variance', 'max_error']
        metrics['r2'] = r2_score(actual_values, predictions)
        metrics['rmse'] = mean_squared_error(actual_values, predictions, squared=False)
        metrics['mse'] = mean_squared_error(actual_values, predictions)
        metrics['mae'] = mean_absolute_error(actual_values, predictions)
        metrics['explained_variance'] = explained_variance_score(actual_values, predictions)
        metrics['max_error'] = max_error(actual_values, predictions)

    if model_type.lower().startswith("clas"):
        LOGGER.info(f"Retrieving 'classification' metrics")
        # reg_metrics = ['accuracy', 'precision_score', 'roc_auc_score', 'roc_curve', 'explained_variance', 'max_error']
        metrics['accuracy'] = accuracy_score(actual_values, predictions)
        metrics['AUC'] = roc_auc_score(actual_values, predictions)
        metrics['precision'] = precision_score(actual_values, predictions)
        metrics['recall'] = recall_score(actual_values, predictions)
        metrics['f1_score'] = f1_score(actual_values, predictions)
        metrics['roc_curve'] = roc_curve(actual_values, predictions)

    else:
        raise ValueError(f"Unknown model_type '{model_type}'. Maybe regression or classification")
    return metrics
