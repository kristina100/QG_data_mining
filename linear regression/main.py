# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Construct training data.
x = np.arange(0., 10., 0.2)
# Array from 0 to 20 with a step size of 0.2.
m = len(x)
# Number of training data points.
print(m)
x0 = np.full(m, 1.0)
input_data = np.vstack([x0, x]).T

# Taking the bias b as the first component of the weight vector
# refers to the upper and lower merge
target_data = 2 * x + 5 + np.random.randn(m)
# Refers to a random number between 0 and 1

# Termination condition.
loop_max = 10000
# Maximum number of iterations (to prevent infinite loops).
epsilon = 1e-3

# Initialize weight.
np.random.seed(0)
# Random seed.
theta = np.random.randn(2)
# theta(Random number between 0 and 2)
alpha = 0.001
""" Step size (note that if the value is too large, 
    the oscillation will not converge, and if the value is too small, 
    the convergence speed will be slower)"""
diff = 0.
# diff cumulative difference operation.
error = np.zeros(2)
# Is to create a zero matrix.
count = 0
# Cycles.
finish = 0
# Stop sign.

while count < loop_max:
    count += 1
    sum_m = np.zeros(2)
    for i in range(m):
        dif = (np.dot(theta, input_data[i]) - target_data[i]) * input_data[i]
        sum_m = sum_m + dif
        # When the alpha value is too large, sum_m will overflow during the iteration.

    theta = theta - alpha * sum_m
    # If the value of the step size is too large, it will cause oscillation.

    # Determine whether to converge.
    if np.linalg.norm(theta - error) < epsilon:
        finish = 1
        break
    else:
        error = theta
    print('loop count = %d' % count, '\tw:', theta)
print('loop count = %d' % count, '\tw:', theta)

# Check with Scipy linear regression.
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x,
                                                                       target_data)
print('intercept = %s slope = %s' % (intercept, slope))

plt.plot(x, target_data, 'g*')
plt.plot(x, theta[1] * x + theta[0], 'r')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

"""
To sum up:
Standard gradient descent summarizes the errors of all examples before the weights are updated, 
while the weights of stochastic gradient descent are updated by a certain training example 
by examining a certain training example.
In standard gradient descent, 
each step of the weight update sums multiple examples, 
which requires more calculations
"""


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
