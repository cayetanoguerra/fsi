import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Make 100 phony data points in NumPy.
x_data = np.float32(np.random.rand(100)) # Random input
y_data = 2. * x_data + 3.
y_data += np.float32(np.random.normal(size=100))*0.1

plt.plot(x_data, y_data, 'bo')
plt.show()

# Construct a linear model.
b = tf.Variable(tf.zeros([1]))
m = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
y = m * x_data + b

# Minimize the squared errors.
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.05)
train = optimizer.minimize(loss)

# For initializing the variables.
init = tf.initialize_all_variables()

# Launch the graph
sess = tf.Session()
sess.run(init)

# Fit the plane.
for step in xrange(0, 1000):
    sess.run(train)
    if step % 100 == 0:
        print step, sess.run(m), sess.run(b)
        
sess.close()

# Learns best fit is m: 2. , b: 3.