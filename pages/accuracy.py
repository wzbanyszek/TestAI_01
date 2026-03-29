def render_accuracy(true_labels, predicted_labels):
    """
    Function to calculate and display accuracy metrics.
    
    Parameters:
    - true_labels: List of true labels
    - predicted_labels: List of predicted labels
    
    Returns:
    Accuracy result as a percentage.
    """
    if len(true_labels) == 0:
        return "No data available for accuracy calculation."
    
    correct_predictions = sum(
        1 for true, pred in zip(true_labels, predicted_labels) if true == pred
    )
    accuracy = correct_predictions / len(true_labels) * 100
    
    return f"Accuracy: {accuracy:.2f}%" 

# Example usage:
# true_labels = [1, 0, 1, 1, 0]
# predicted_labels = [1, 0, 1, 0, 0]
# print(render_accuracy(true_labels, predicted_labels))