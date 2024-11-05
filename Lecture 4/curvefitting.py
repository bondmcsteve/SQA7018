# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt  # module required to plot graph
from scipy.optimize import curve_fit

# Load data from a text file
mydata = np.loadtxt('data.txt',skiprows=1)

# Extract x and y data from the loaded file
x = mydata[:, 0]
y = mydata[:, 1]

# Function to fit the data and plot the result
def drawgraph(func, x, y):
    """
    This function takes in a model function 'func', the x and y data, and fits the model
    to the data using non-linear least squares fitting. It then calculates the coefficient
    of determination (R²) and plots the original data and fitted curve.
    """
    # Perform curve fitting to find optimal parameters for the model
    popt, pcov = curve_fit(func, x, y)

    # Calculate the predicted y-values using the optimized parameters
    predicted = func(x, *popt)

    # Calculate the coefficient of determination (R²)
    r = np.corrcoef(y, predicted)  # Correlation coefficient matrix
    r2 = r[0, 1] ** 2  # Square of the correlation coefficient (R²)
    print(f'Coefficient of determination (R²): {r2:.3g}')

    # Display the optimal parameters found by curve_fit
    for idx, (param, sd) in enumerate(zip(popt, pcov), 1):
        print(f'Parameter {idx}: {param:.3g} ± {sd[idx-1]:.3g}')
    return popt, r2

# Define the model function
def func(x,a,b):
    return np.exp(a*x)*np.sin(x)+b

# Fit the model to the data and retrieve optimal parameters and R² value
popt, r2 = drawgraph(func, x, y)

# Create a smooth line for the fitted curve using 100 points between 0 and max(x)
newx = np.linspace(0, max(x), 100)

# Plot the fitted curve using the optimized parameters
plt.plot(newx, func(newx, *popt), label='Fitted Curve')

# Set the y-axis limit slightly above the maximum of the actual data for better visualization
plt.ylim(0, max(y) * 1.1)

# Plot the original data points as a scatter plot
plt.scatter(x, y, color='red', label='Original Data', marker='x')

# Label the axes and add a title
plt.xlabel('x-axis (Time or Independent Variable)')
plt.ylabel('y-axis (Dependent Variable)')
plt.title('Best Fit')

# Add a legend to differentiate between the original data and fitted curve
plt.legend()
# Display the plot
plt.show()

