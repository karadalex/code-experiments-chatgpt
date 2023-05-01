from network import run_network
import numpy as np

# Define an example input
input = np.array([1, 2, 3, 4]).reshape((4, 1))

# Run the network on the input
output = run_network(input)

# Print the output
print(output)