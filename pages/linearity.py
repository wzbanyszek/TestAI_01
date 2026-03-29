def render_linearity(data):
    """
    Analyzes linearity of the provided data and performs regression calculations.

    Parameters:
    data (list of tuples): A list containing tuples of (x, y) data points.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression

    # Separate the data into x and y lists
    x = np.array([point[0] for point in data]).reshape(-1, 1)
    y = np.array([point[1] for point in data])

    # Create a linear regression model
    model = LinearRegression()
    model.fit(x, y)

    # Predict y values based on x values
    y_pred = model.predict(x)

    # Calculate the coefficient of determination (R^2)
    r_squared = model.score(x, y)

    # Plotting
    plt.scatter(x, y, color='blue', label='Data Points')
    plt.plot(x, y_pred, color='red', label='Linear Regression Line')
    plt.title(f'Linearity Analysis (R^2 = {r_squared:.2f})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

    return r_squared