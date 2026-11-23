import pennylane as qp
from pennylane import numpy as np
from scipy.stats import unitary_group

n = 10
U_matrix = unitary_group.rvs(2)
eigenvalues, eigenvectors = np.linalg.eig(U_matrix)

dev = qp.device("default.qubit", wires=n+1)

@qp.qnode(dev)
def circuit():
    qp.StatePrep(eigenvectors[:, 0], wires=0)

    for wire in range(1, n+1):
        qp.Hadamard(wires=wire)

    qp.ControlledSequence(
        qp.QubitUnitary(U_matrix, wires=0),
        control=list(range(1, n+1))
    )

    qp.adjoint(qp.QFT)(wires=list(range(1, n+1)))

    return qp.probs(wires=list(range(1, n+1)))

exact_phase = (np.angle(eigenvalues[0]) / (2 * np.pi)) % 1

probs = circuit()

exact_phase = (np.angle(eigenvalues[0]) / (2 * np.pi)) % 1

possible_phases = np.arange(2**n) / (2**n)

errors = np.abs(possible_phases - exact_phase)
errors = np.minimum(errors, 1 - errors)

expected_error = np.sum(probs * errors)

print("Exact phase:", exact_phase)
print("Expected absolute phase error:", expected_error)
