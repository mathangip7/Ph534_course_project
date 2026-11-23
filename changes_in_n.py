
import pennylane as qp
from pennylane import numpy as np
from scipy.stats import unitary_group
import matplotlib.pyplot as plt

# QPE for a given unitary and its eigenstate
def run_qpe(U_matrix, eigenstate, n):

    wires = list(range(1, n + 1))
    dev = qp.device("default.qubit", wires=n + 1)

    @qp.qnode(dev)
    def circuit():
        qp.StatePrep(eigenstate, wires=0)

        for wire in wires:
            qp.Hadamard(wires=wire)

        qp.ControlledSequence(
            qp.QubitUnitary(U_matrix, wires=0),
            control=wires
        )

        qp.adjoint(qp.QFT)(wires=wires)

        return qp.probs(wires=wires)

    probs = circuit()

    # Most probable measurement outcome
    k = np.argmax(probs)
    estimated_phase = k / (2**n)

    return estimated_phase


# Experiment parameters
n_values = range(1, 11)
num_trials = 50

mean_errors = []
std_errors = []

# Repeat for multiple random unitaries
for n in n_values:

    errors = []

    for trial in range(num_trials):

        # Generate random 2x2 unitary
        U_matrix = unitary_group.rvs(2)

        # Find eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(U_matrix)

        # Select one eigenstate
        eigenstate = eigenvectors[:, 0]

        # Exact eigenphase
        exact_phase = (
            np.angle(eigenvalues[0]) / (2 * np.pi)
        ) % 1

        # Run QPE
        estimated_phase = run_qpe(
            U_matrix, eigenstate, n
        )

        # Absolute phase error (accounting for circularity)
        error = abs(estimated_phase - exact_phase)
        error = min(error, 1 - error)

        errors.append(error)

    mean_errors.append(np.mean(errors))
    std_errors.append(np.std(errors))



fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Linear scale
axes[0].errorbar(
    list(n_values),
    mean_errors,
    yerr=std_errors,
    marker='o',
    capsize=4
)
axes[0].set_xlabel("Number of estimation qubits (n)")
axes[0].set_ylabel("Mean absolute phase error")
axes[0].set_title("Linear Scale")
axes[0].set_xticks(list(n_values))
axes[0].grid(True)

# Logarithmic scale
axes[1].errorbar(
    list(n_values),
    mean_errors,
    yerr=std_errors,
    marker='o',
    capsize=4
)
axes[1].set_xlabel("Number of estimation qubits (n)")
axes[1].set_ylabel("Mean absolute phase error")
axes[1].set_title("Logarithmic Scale")
axes[1].set_xticks(list(n_values))
axes[1].set_yscale("log")
axes[1].grid(True, which="both")

plt.suptitle("QPE Accuracy vs Number of Estimation Qubits")
plt.tight_layout()
plt.show()

