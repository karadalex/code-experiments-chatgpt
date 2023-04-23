from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to the qubit
qc.h(0)

# Measure the qubit and store the result in the classical bit
qc.measure(0, 0)

# Use the qasm_simulator to run the circuit and get the results
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend).result()

# Print the measurement result
print(result.get_counts(qc))
