# Regression Projects

## Single Variable Non-linear Regression

This file imports data_nonlinear.csv and using pandas, numpy, and matplotlib it:

1. Establishes a relationship between Y and X with a quadratic function
2. Computes MSE loss with observation-prediction pairs
3. Implements Gradient Descent to achieve the optimal solution with the learning rate of 0.0001 (1e-4) and 10000 (1e4) epochs
4. Prints out the optimal solution

## Multiple Variable Linear Regression

This file imports data_two_variables.csv and using pandas, numpy, and mpl_toolkits it:

1. Establishes a linear function to describe the relationship among Y, X1, and X2
2. Computes MSE loss with observation-prediction pairs
3. Implements Gradient Descent to achieve optimal solution with the learning rate of 0.001 (1e-3) and 10000 (1e4) epochs
4. Prints out the optimal solution

## Logistic Regression

This file imports data_logistic.csv and using pandas, numpy, and matplotlib it:

1. Generates a scatter plot of the data
2. Implements a signmoid function
3. Implements the "cal_cost" to compute the cost
4. Implements the "cal_grad" to compute the gradients
5. Tests "cal_cost" and "cal_grad" with initial values and print out the results
6. Calculates the best fit theta by Gradient Descent with learning rate of 0.001 (1e-3) and epoch of 80K.
7. Prints out the best theta and its corresponding cost.
8. Plots the decision boundary.
9. Calculates the training accuracy
10. Evaluates the predicted probability of the learnt model with x1 = 56 and x2 = 32
11. Implements the "cal_reg_cost" to compute the cost.
12. Implements the "cal_reg_grad" to compute the gradients.
13. Tests the the two functions with initial values.
14. Implements a Gradient Descent function to optimize parameters.
15. Calculates best fit theta by Gradient Descent with learning rate of 0.001 (1e-3), epoch of 80K, and lambda 1.
16. Prints out the best theta and its corresponding cost
