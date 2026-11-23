# Quantum Phase Estimation: slide contents

---

## 1. How do we read a number hidden in a *phase*?

**On screen**
- A unit circle draws on. A blue arrow sweeps round to $0.625$ of a turn and leaves a gold arc labelled $2\pi\varphi$.
- Subtitle: Quantum Phase Estimation · Shishir · QuIC Seminar

---

## 2. Why would anyone want an eigenvalue?

**On screen**
- $A\,\vec{x} = \lambda\,\vec{x}$
- Four cards, each with an arrow from $\lambda$:
  - **Shor**: factoring via order finding
  - **HHL**: solving $A\vec{x} = \vec{b}$
  - **Chemistry**: ground-state energies of molecules
  - **qPCA**: finding the main directions in data
- Loop: "Can't we just diagonalise it?"

---

## 3. What does an eigenvalue of $U$ look like?

**On screen**

$$U|x\rangle = \lambda|x\rangle \;\Rightarrow\; \langle x|U^\dagger U|x\rangle = |\lambda|^2\langle x|x\rangle \;\Rightarrow\; |\lambda| = 1$$

- A dot runs once round the unit circle and stops at $0.625$ of a turn. Label: "$\varphi$ of a full turn".
- Boxed: $\lambda = e^{2\pi i\varphi}, \quad 0 \le \varphi < 1$


---

## 4. How do we write an angle in binary?

**On screen**

$$\varphi = 0.\varphi_1\varphi_2\cdots\varphi_n = \sum_{k=1}^{n}\varphi_k\,2^{-k}$$

- Examples: $0.1_2 = \tfrac12 = 0.5$ and $0.11_2 = \tfrac12 + \tfrac14 = 0.75$
- A ruler from 0 to 1 halves three times around a marker at $0.625$. The digits drop in one by one: $\varphi = 0.101_2 = 0.625$
- Pip: "So $0.1111\ldots$ is just 1!"


---

## 5. Where does phase live on a Bloch sphere?

**On screen**
- Bloch sphere. The arrow starts at $|0\rangle$, swings about the $H$ axis to $|+\rangle$, then runs once round the equator while a readout counts $\alpha$ from $0$ to $2\pi$.
- $|0\rangle + e^{i\alpha}|1\rangle \;\longmapsto\;$ longitude $\alpha$ on the equator
- Grand Phi's card: $H|0\rangle = |+\rangle,\; H|1\rangle = |-\rangle$. $H$ is a half-turn about the diagonal axis.


---

## 6. Why does the control qubit change?

**On screen**
- Circuit: $|0\rangle$ then $H$ then a control dot. $|\psi\rangle$ goes into $U^{2^0}$.
- The sphere follows the circuit: $H$ takes the arrow to $|+\rangle$, then the controlled $U$ turns it by $2\pi\varphi$.
- Algebra, with the gold factor sliding from $|\psi\rangle$ over to $|1\rangle$:

$$|0\rangle|\psi\rangle + |1\rangle U|\psi\rangle = |0\rangle|\psi\rangle + e^{2\pi i\,0.\varphi_1}|1\rangle|\psi\rangle = \big(|0\rangle + e^{2\pi i\,0.\varphi_1}|1\rangle\big)\otimes|\psi\rangle$$

- Small print: normalisation dropped
- Boxed: $U$ leaves $|\psi\rangle$ alone and writes its phase onto the control.
- Loop: "Hey, why did I move?"


---

## 7. How do we read one bit of $\varphi$?

**On screen**
- Two spheres, $\varphi_1 = 0$ and $\varphi_1 = 1$. The right arrow turns by $\pi$ to $|-\rangle$. Then $H$ sends the left one to $|0\rangle$ and the right one to $|1\rangle$. Meters read 0 and 1.

$$H\big(|0\rangle + e^{2\pi i\,0.\varphi_1}|1\rangle\big) = \big(1 + e^{2\pi i\,0.\varphi_1}\big)|0\rangle + \big(1 - e^{2\pi i\,0.\varphi_1}\big)|1\rangle$$

$$\varphi_1 = 0 \Rightarrow e^0 = 1 \Rightarrow |0\rangle \qquad \varphi_1 = 1 \Rightarrow e^{i\pi} = -1 \Rightarrow |1\rangle$$

- Boxed: certain, not probabilistic


---

## 8. Can we try it on Pauli $X$?

**On screen**
- Circuit: top $|0\rangle$, $H$, control, $H$, measure. Bottom $|0\rangle$, $H$, CNOT target. Later an $X$ is added before the bottom $H$ to make $|-\rangle$. Caption: CNOT is a controlled $X$.

| eigenstate | $\lambda$ | $\varphi$ | measured | Qiskit (4096 shots) |
|---|---|---|---|---|
| $\lvert+\rangle$ | $+1$ | $0.0_2$ | 0 | 0 : 4096 |
| $\lvert-\rangle$ | $-1$ | $0.1_2$ | 1 | 1 : 4096 |

- Pip: "100 percent, both times!"



---

## 9. How do we get the other bits?

**On screen**

$$U^{2^k}|\psi\rangle = e^{2\pi i\,2^k\varphi}|\psi\rangle$$

- Small $n = 2$ circuit in the corner.
- $2 \times 0.\varphi_1\varphi_2 = \varphi_1.\varphi_2$. The $\varphi_1$ in front turns red: "whole turn, does nothing". $e^{2\pi i\varphi_1} = 1$ gets crossed out.
- Three qubits spin together at the same speed: qubit 0 ($U$) does $0.625$ turns, qubit 1 ($U^2$) does $1.25$, qubit 2 ($U^4$) does $2.5$. Whole turns fade. They are left seeing $0.101$, $0.01$ and $0.1$.
- Boxed: $e^{2\pi i\,2^k\varphi} = e^{2\pi i\,0.\varphi_{k+1}\varphi_{k+2}\cdots\varphi_n}$


---

## 10. How do we read all the bits at once?

**On screen**

$$\mathrm{QFT}\,|\varphi_1\cdots\varphi_n\rangle = \tfrac{1}{2^{n/2}}\big(|0\rangle + e^{2\pi i\,0.\varphi_n}|1\rangle\big)\otimes\cdots\otimes\big(|0\rangle + e^{2\pi i\,0.\varphi_1\cdots\varphi_n}|1\rangle\big)$$

After the controlled-$U$s:

$$\tfrac{1}{2^{n/2}}\big(|0\rangle + e^{2\pi i\,2^{n-1}\varphi}|1\rangle\big)\otimes\cdots\otimes\big(|0\rangle + e^{2\pi i\,2^{0}\varphi}|1\rangle\big)$$

- Matching factors light up in gold, pair by pair. Small print: up to bit order, which a few SWAPs fix.
- So $\mathrm{QFT}^\dagger$ turns it back into $|\varphi_1\varphi_2\cdots\varphi_n\rangle$.
- A $\mathrm{QFT}^\dagger$ box sweeps across three spheres. Each arrow snaps to a pole and turns green. Bits read 1 0 1. Small print: cartoon of the inverse QFT, which acts on all qubits together.
- Boxed: $\tilde{\varphi} = 0.101_2 = 0.625$


---

## 11. What does the full circuit look like?

**On screen**
- $n$ blue qubits in $|0\rangle$, each with $H$. Qubit $k$ controls $U^{2^k}$ on $|\psi\rangle$. Then one tall $\mathrm{QFT}^\dagger$ and meters.
- A "now" line steps through the circuit while the state builds up underneath:

$$|0\rangle^{\otimes n} \xrightarrow{H^{\otimes n}} \tfrac{1}{2^{n/2}}\bigotimes_k\big(|0\rangle+|1\rangle\big) \xrightarrow{C\text{-}U^{2^k}} \tfrac{1}{2^{n/2}}\bigotimes_k\big(|0\rangle+e^{2\pi i\,2^k\varphi}|1\rangle\big) \xrightarrow{\mathrm{QFT}^\dagger} |\varphi_1\cdots\varphi_n\rangle$$


---

## 12. What if life is not that tidy?

**On screen**

*Left: we don't know an eigenstate*
- $|\psi\rangle = \sum_u c_u|u\rangle$ splits into strands $|u_1\rangle, |u_2\rangle, |u_3\rangle$, each with its own $\varphi_u$ and weight $|c_u|^2$.
- Each $|u\rangle$ runs its own QPE. We read $\varphi_u$ with probability $|c_u|^2$, and the register collapses into $|u\rangle$.

*Right: $\varphi$ needs infinitely many bits*
- Ruler with $\varphi = 1/3$. With $n = 3$ the nearest tick is $0.375$. With $n = 5$ it is $0.34375$.
- We get the nearest $n$-bit value with probability at least $4/\pi^2 \approx 0.405$. More qubits, more precision.
- Pip: "More qubits, sharper answer."


---

## 13. How do we build it for any $U$?

**On screen**
- Brief: *Implement phase estimation for an arbitrary unitary using Qiskit*
- Code, highlighted one block at a time while the matching part of a small circuit lights up:

```python
def qpe_circuit(U, psi, n):
    m = int(np.log2(U.shape[0]))
    qc = QuantumCircuit(n + m, n)
    qc.initialize(psi, range(n, n + m))  # bottom register |psi>
    qc.h(range(n))  # top register into |+>^n
    gate = UnitaryGate(U, label="U")
    for k in range(n):  # qubit k controls U^(2^k)
        cU = gate.power(2 ** k).control(1)
        qc.append(cU, [k] + list(range(n, n + m)))
    qc.append(QFTGate(n).inverse(), range(n))  # inverse QFT reads out the bits
    qc.measure(range(n), range(n))
    return qc
```

Highlight order: initialize, then $H$, then the controlled-$U$ loop, then inverse QFT, then measure.


---

## 14. Did it actually work?

**On screen** (three histograms, gold dashed lines at the true phases)

1. **Exact: $\varphi = 0.625$, $n = 3$.** Outcome 101 in 4096 of 4096 shots, so $\tilde{\varphi} = 0.625$.
2. **Inexact: $\varphi = 1/3$, $n = 5$, 8192 shots.** Peak at 01011 $= 0.34375$ with 68.7% (the floor is 40.5%). Other outcomes: 01010 1390, 01100 323, 01001 218, 01101 112, 01000 97, 01110 73.
3. **Random 2-qubit $U$, input $|00\rangle$, $n = 5$.** Not an eigenstate, top outcomes shown: 01100 12.8%, 10101 16.1%, 10111 19.4%, 11000 10.9%, 11101 23.6%, 11100 4.3%.

| true $\varphi_u$ (numpy) | peak $\tilde{\varphi}$ |
|---|---|
| 0.3671 | 0.375 |
| 0.6538 | 0.65625 |
| 0.7320 | 0.71875, 0.75 |
| 0.8972 | 0.90625 |

- Pip: "Bang on."


---

## 15. Is there a cheaper cousin?

**On screen**
- The one-bit circuit again: $|0\rangle$, $H$, control, $H$, measure, with $|\psi\rangle$ into a box. The $U$ becomes $Q$. The label "eigenstate" is struck out: not needed, any state works.
- Boxed: $p(0) - p(1) = \mathrm{Re}\,\langle\psi|Q|\psi\rangle$
- Small print: add an $S$ gate before the last $H$ to get the imaginary part.


---

## 16. What should we remember?

**On screen**
1. Eigenvalues of unitaries are angles, $e^{2\pi i\varphi}$.
2. Phase kickback moves that angle onto the control qubit.
3. Powers of two + inverse QFT read it out bit by bit.

The unit circle from slide 1 sweeps once more to $0.625$. 


