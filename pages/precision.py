def render_precision(y_true, y_pred):
    """
    Calculate and display the precision metric.

    Parameters:
    y_true : list
        True binary labels or binary label indicators.
    y_pred : list
        Estimated targets as returned by a classifier.

    Returns:
    precision : float
        The precision metric calculated as true positives / (true positives + false positives).
    """
    true_positives = sum((1 for true, pred in zip(y_true, y_pred) if true == 1 and pred == 1))
    false_positives = sum((1 for true, pred in zip(y_true, y_pred) if true == 0 and pred == 1))

    if (true_positives + false_positives) == 0:
        return 0.0  # To avoid division by zero

    precision = true_positives / (true_positives + false_positives)
    return precision
