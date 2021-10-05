---
title: "Definition"
katex: true
weight: 6
---
# Definition

## Entanglement

Entanglement refers to a phenomenon observed in quantum systems where multiple particles in a system are unable to be described independently of one another.[^Horodecki2007]

The term "entanglement" was introduced by Schrödinger in his 1935 article. [^Schrodinger1935] Entanglement exists between multiple particles. When performing an operation on one of the particles, the other entangled particles may also be affected by this operation.

In Schrödinger's paper, he also highlighted the unintuitiveness of quantum entanglement. He references the 1935 paper by Einstein, Podolsky, and Rosen[^EPR1935], stating:
> Attention has recently been called to the obvious but very disconcerting fact that even though we restrict the disentangling measurements to one system, the representative obtained for the other system is by no means independent of the particular choice of observations which we select for that purpose and which by the way are entirely arbitrary. It is rather discomforting that the theory should allow a system to be steered or piloted into one or the other type of state at the experimenter’s mercy in spite of his having no access to it.

## Example

Suppose Bob has 2 electrons which are entangled in the Bell state {{< katex >}}|\psi^+\rangle=\frac{\vert01\rangle\otimes+\vert10\rangle}{\sqrt{2}}{{< /katex >}}. The electrons are then taken far away from each other. If Bob measures the state of the first electron, it will collapse the wave function of the second electron. In this example, if he measures {{< katex >}}\vert0\rangle{{< /katex >}} on the first electron, the second electron will collapse to {{< katex >}}\vert1\rangle{{< /katex >}}. Likewise, if he measures {{< katex >}}\vert1\rangle{{< /katex >}} on the first electron, the second electron will collapse to {{< katex >}}\vert0\rangle{{< /katex >}}. This is an example of the "spooky action" that Einstein had refered to, where operations on the first election can change the state of the second electron.

Even though the idea of entanglement had already been introduced by Schrödinger in 1935, it took till 1995 for the first experimental realization of a two-qubit entangling quantum gate by Monroe et al. [^Monroe1995]

[^Horodecki2007]: Ryszard Horodecki; Pawel Horodecki; Michal Horodecki; Karol Horodecki (2007). "Quantum entanglement". arXiv:quant-ph/0702225
[^Schrodinger1935]: Schrödinger, E. (1935). "Discussion of Probability Relations Between Separated Systems". Proceedings of the Cambridge Philosophical Society, 31: pg. 555
[^EPR1935]: Einstein, A; B Podolsky; N Rosen (1935). "Can Quantum-Mechanical Description of Physical Reality be Considered Complete?". Physical Review. 47 (10): 777–780. 
[^Monroe1995]: C. Monroe; D. M. Meekhof; B. E. King; W. M. Itano; D. J. Wineland (1995). "Demonstration of a Fundamental Quantum Logic Gate". Phys. Rev. Lett., 75 (25): 4714-7.
