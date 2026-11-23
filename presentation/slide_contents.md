# Quantum Phase Estimation: slide contents

QuIC Seminar, 15 minutes, 16 slides. For each slide we list what is on screen and what we say.

Colour code used on every slide: $\varphi$ and eigenvalues in gold, control qubits in blue, the eigenstate $|\psi\rangle$ in teal, $U$ in purple, gates like $H$ and $\mathrm{QFT}^\dagger$ in chalk, measured results in green.

---

## 1. How do we read a number hidden in a *phase*?

**On screen**
- A unit circle draws on. A blue arrow sweeps round to $0.625$ of a turn and leaves a gold arc labelled $2\pi\varphi$.
- Subtitle: Quantum Phase Estimation · Shishir · QuIC Seminar

**Say**
Hi everyone. Today we are going to read a number that a quantum computer hides inside a phase. The number is an eigenvalue, and the trick for reading it is called phase estimation. It is the engine inside Shor's algorithm, so it is worth fifteen minutes.

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

**Say**
Eigenvalues are everywhere. Shor's factoring, the HHL algorithm for linear systems, energies in quantum chemistry, even principal component analysis. Classically we diagonalise a matrix. But our matrix is a $2^m$ by $2^m$ unitary acting on $m$ qubits. For 50 qubits that matrix does not fit on any computer on Earth. So we need a quantum way to pull the eigenvalue out.

---

## 3. What does an eigenvalue of $U$ look like?

**On screen**

$$U|x\rangle = \lambda|x\rangle \;\Rightarrow\; \langle x|U^\dagger U|x\rangle = |\lambda|^2\langle x|x\rangle \;\Rightarrow\; |\lambda| = 1$$

- A dot runs once round the unit circle and stops at $0.625$ of a turn. Label: "$\varphi$ of a full turn".
- Boxed: $\lambda = e^{2\pi i\varphi}, \quad 0 \le \varphi < 1$

**Say**
Unitaries preserve length, so every eigenvalue has size one. It sits on the unit circle. That means the whole eigenvalue is just one real number, $\varphi$, the fraction of a full turn. That is the phase in phase estimation. The estimation part is about how many bits of $\varphi$ we get.

---

## 4. How do we write an angle in binary?

**On screen**

$$\varphi = 0.\varphi_1\varphi_2\cdots\varphi_n = \sum_{k=1}^{n}\varphi_k\,2^{-k}$$

- Examples: $0.1_2 = \tfrac12 = 0.5$ and $0.11_2 = \tfrac12 + \tfrac14 = 0.75$
- A ruler from 0 to 1 halves three times around a marker at $0.625$. The digits drop in one by one: $\varphi = 0.101_2 = 0.625$
- Pip: "So $0.1111\ldots$ is just 1!"

**Say**
We write $\varphi$ as a binary fraction. Each bit says: left half or right half. Three bits pin $\varphi$ into one of eight slots. Keep this picture, because the algorithm will hand us these bits one qubit at a time. Today we mostly assume $\varphi$ fits exactly in $n$ bits. We will relax that at the end.

---

## 5. Where does phase live on a Bloch sphere?

**On screen**
- Bloch sphere. The arrow starts at $|0\rangle$, swings about the $H$ axis to $|+\rangle$, then runs once round the equator while a readout counts $\alpha$ from $0$ to $2\pi$.
- $|0\rangle + e^{i\alpha}|1\rangle \;\longmapsto\;$ longitude $\alpha$ on the equator
- Grand Phi's card: $H|0\rangle = |+\rangle,\; H|1\rangle = |-\rangle$. $H$ is a half-turn about the diagonal axis.

**Say**
Here is the picture we will use all talk. Up is zero, down is one. The Hadamard is a half-turn about this diagonal axis, so it takes zero to plus, on the equator. And here is the key point: a relative phase between zero and one is just how far round the equator we are. Phase is longitude. Hold on to that.

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

**Say**
Put the top qubit in plus and the bottom in an eigenstate. The controlled $U$ acts only on the one-branch. But $|\psi\rangle$ is an eigenstate, so $U$ just multiplies it by $e^{2\pi i\varphi}$. A number does not care which register it sits next to, so we can slide it over to the control qubit. The target never changes. The control picks up the phase. On the sphere, the arrow turns by exactly $2\pi\varphi$. This is called phase kickback, and it is the whole trick.

---

## 7. How do we read one bit of $\varphi$?

**On screen**
- Two spheres, $\varphi_1 = 0$ and $\varphi_1 = 1$. The right arrow turns by $\pi$ to $|-\rangle$. Then $H$ sends the left one to $|0\rangle$ and the right one to $|1\rangle$. Meters read 0 and 1.

$$H\big(|0\rangle + e^{2\pi i\,0.\varphi_1}|1\rangle\big) = \big(1 + e^{2\pi i\,0.\varphi_1}\big)|0\rangle + \big(1 - e^{2\pi i\,0.\varphi_1}\big)|1\rangle$$

$$\varphi_1 = 0 \Rightarrow e^0 = 1 \Rightarrow |0\rangle \qquad \varphi_1 = 1 \Rightarrow e^{i\pi} = -1 \Rightarrow |1\rangle$$

- Boxed: certain, not probabilistic

**Say**
How do we read the phase? Another Hadamard. If $\varphi_1$ is zero we are at plus and we go back to zero. If $\varphi_1$ is one we are at minus and we go to one. No randomness. We get the bit with certainty.

---

## 8. Can we try it on Pauli $X$?

**On screen**
- Circuit: top $|0\rangle$, $H$, control, $H$, measure. Bottom $|0\rangle$, $H$, CNOT target. Later an $X$ is added before the bottom $H$ to make $|-\rangle$. Caption: CNOT is a controlled $X$.

| eigenstate | $\lambda$ | $\varphi$ | measured | Qiskit (4096 shots) |
|---|---|---|---|---|
| $\lvert+\rangle$ | $+1$ | $0.0_2$ | 0 | 0 : 4096 |
| $\lvert-\rangle$ | $-1$ | $0.1_2$ | 1 | 1 : 4096 |

- Pip: "100 percent, both times!"

**Say**
Quick sanity check. Pauli $X$ has eigenvalues plus and minus one. CNOT is just controlled $X$. With plus in the bottom register we always read zero, so lambda is one. Put minus there and we always read one, so lambda is minus one. The simulator agrees, four thousand ninety six out of four thousand ninety six.

---

## 9. How do we get the other bits?

**On screen**

$$U^{2^k}|\psi\rangle = e^{2\pi i\,2^k\varphi}|\psi\rangle$$

- Small $n = 2$ circuit in the corner.
- $2 \times 0.\varphi_1\varphi_2 = \varphi_1.\varphi_2$. The $\varphi_1$ in front turns red: "whole turn, does nothing". $e^{2\pi i\varphi_1} = 1$ gets crossed out.
- Three qubits spin together at the same speed: qubit 0 ($U$) does $0.625$ turns, qubit 1 ($U^2$) does $1.25$, qubit 2 ($U^4$) does $2.5$. Whole turns fade. They are left seeing $0.101$, $0.01$ and $0.1$.
- Boxed: $e^{2\pi i\,2^k\varphi} = e^{2\pi i\,0.\varphi_{k+1}\varphi_{k+2}\cdots\varphi_n}$

**Say**
One qubit gives us one bit. For more bits we add more control qubits, and qubit $k$ controls $U$ to the power $2^k$. Doubling $\varphi$ slides the binary point one place right. The digit that pops out in front is a whole number of turns, and a whole turn does nothing. So each qubit sees $\varphi$ with the first few bits chopped off. The last qubit sees just one bit, the second last sees two, and so on.

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

**Say**
Now each control qubit holds part of $\varphi$ in its phase. One Hadamard is not enough any more. But look: this product is exactly what the quantum Fourier transform makes from the bit string of $\varphi$. The QFT is unitary, so it has an inverse. Run the inverse QFT and the phases turn back into plain bits. Measure, and we read $\varphi$ directly. We are borrowing this QFT result today, its derivation is a seminar of its own.

---

## 11. What does the full circuit look like?

**On screen**
- $n$ blue qubits in $|0\rangle$, each with $H$. Qubit $k$ controls $U^{2^k}$ on $|\psi\rangle$. Then one tall $\mathrm{QFT}^\dagger$ and meters.
- A "now" line steps through the circuit while the state builds up underneath:

$$|0\rangle^{\otimes n} \xrightarrow{H^{\otimes n}} \tfrac{1}{2^{n/2}}\bigotimes_k\big(|0\rangle+|1\rangle\big) \xrightarrow{C\text{-}U^{2^k}} \tfrac{1}{2^{n/2}}\bigotimes_k\big(|0\rangle+e^{2\pi i\,2^k\varphi}|1\rangle\big) \xrightarrow{\mathrm{QFT}^\dagger} |\varphi_1\cdots\varphi_n\rangle$$

**Say**
Here is the whole thing. Hadamards to spread out, controlled powers of $U$ to kick the phase in, inverse QFT to read it out. Three steps.

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

**Say**
Two worries. First, if we knew an eigenstate, would we even need this? Good news: we don't need one. Any state is a mix of eigenstates, and QPE hands us one of their phases at random, weighted by how much of it was in the mix. Second, what if $\varphi$ is something like one third, which never ends in binary? Then we get the best $n$-bit guess with decent probability, and adding qubits sharpens it.

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

**Say**
Here is my implementation. The input is any unitary matrix and any input state. Qiskit's UnitaryGate turns the matrix into a gate. For counting qubit $k$ we take that gate to the power $2^k$ and add one control. Then the inverse QFT, then measure. Nothing in here assumes a special $U$. Hand it any $2^m$ by $2^m$ unitary and it runs. One honest caveat: building $U^{2^k}$ by matrix power is fine on a simulator, but on real hardware those big powers are the expensive part.

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

**Say**
First, a phase that fits in three bits. We get one zero one every single time, which is 0.625, exactly right. Next, one third, which never ends in binary. With five qubits the top outcome is 0.344, about 69 percent of the time. Finally the real test: a random two-qubit unitary and an input that is not an eigenstate. The histogram has four peaks, and each one sits next to a true eigenphase from numpy. The heights match how much of each eigenstate was in the input.

---

## 15. Is there a cheaper cousin?

**On screen**
- The one-bit circuit again: $|0\rangle$, $H$, control, $H$, measure, with $|\psi\rangle$ into a box. The $U$ becomes $Q$. The label "eigenstate" is struck out: not needed, any state works.
- Boxed: $p(0) - p(1) = \mathrm{Re}\,\langle\psi|Q|\psi\rangle$
- Small print: add an $S$ gate before the last $H$ to get the imaginary part.

**Say**
A quick cousin. Same circuit shape as our one-bit readout, but now the bottom state need not be an eigenstate. The difference of the two outcome probabilities gives the real part of an expectation value. It shows up all over variational algorithms.

---

## 16. What should we remember?

**On screen**
1. Eigenvalues of unitaries are angles, $e^{2\pi i\varphi}$.
2. Phase kickback moves that angle onto the control qubit.
3. Powers of two + inverse QFT read it out bit by bit.

The unit circle from slide 1 sweeps once more to $0.625$. Then: **Questions?**

**Say**
Three things to take home. Unitary eigenvalues are angles. Kickback puts the angle on the control. Powers of two and an inverse QFT read it out. That is phase estimation. Thank you, happy to take questions.
