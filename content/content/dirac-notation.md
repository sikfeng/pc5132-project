---
title: "Dirac Notation"
katex: true
weight: 5
---

# Dirac Notation

*Prerequisite: Basic Linear Algebra (covered under H2 ’A’ Level Further Mathematics Syllabus)*

Dirac notation is often used in quantum mechanics and quantum information to describe phenomena. Here we will try to explain the notation that you will need to know.

## Ket

A ket {{< katex >}}\vert\psi\rangle{{< /katex >}} can be represented by a column vector.

For example, a 2 dimensional ket could be represented  by {{< katex >}}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix}{{< /katex >}}, and a 3 dimensional ket could be represented by {{< katex >}}\begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix}{{< /katex >}}, and so on (where {{< katex >}}v_i\in\mathbb{C}{{< /katex >}} for {{< katex >}}i\in\mathbb{N}{{< /katex >}}). 

We can perform addition and scalar multiplication of kets just like vectors in linear algebra.

For our purposes, it is safe to assume kets are 2-dimensional unless stated otherwise.

A few common kets are defined below.

{{< katex >}}\vert0\rangle=\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \vert1\rangle=\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \vert+\rangle=\begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}, \vert-\rangle=\begin{pmatrix} \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} \end{pmatrix}{{< /katex >}}

It is also common to represent the spin-up electron or horizontally polarized photon as {{< katex >}}\vert0\rangle{{< /katex >}}, and the spin-down electron or vertically polarized photon as {{< katex >}}\vert0\rangle{{< /katex >}}.

## Kronecker product

The only operation involving kets that (probably) isn't covered under H2 ’A’ Level Further Mathematics Syllabus would be the Kronecker product. 

The Kronecker product is a binary operator that maps 2 matrices to a larger matrix.

{{< katex >}}\mathbf{A}\otimes\mathbf{B}=\mathbf{C}, \mathbf{A}\in M^{m_A\times n_A}, \mathbf{B}\in M^{m_B\times n_B}, \mathbf{C}\in M^{m_Am_B\times n_An_B}{{< /katex >}}

For 2 dimensional kets, the Kronecker product acts as follows:

{{< katex >}}\vert\psi\rangle\otimes\vert\phi\rangle=\begin{pmatrix} v_1 \\ v_2 \end{pmatrix}\otimes\begin{pmatrix} w_1 \\ w_2 \end{pmatrix}=\begin{pmatrix} v_1w_1 \\ v_1w_2 \\ v_2w_1 \\ v_2w_2 \end{pmatrix}{{< /katex >}}

As an example, {{< katex >}}\vert0\rangle\otimes\vert1\rangle=\begin{pmatrix} 1 \\ 0 \end{pmatrix}\otimes\begin{pmatrix} 0 \\ 1 \end{pmatrix}=\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}{{< /katex >}}

The composition of 2 quantum systems can be represented by the Kronecker product of 2 kets ({{< katex >}}\vert\psi\rangle\otimes\vert\phi\rangle{{< /katex >}}).

We also often write {{< katex >}}\vert\psi\rangle\otimes\vert\phi\rangle{{< /katex >}} simply as {{< katex >}}\vert\psi\phi\rangle{{< /katex >}}.

# Quantum Postulates

## Postulate 1

> Associated to any isolated physical system is a complex vector space with inner product (that is, a Hilbert space) known as the **state space** of the system. The system is completely described by its state vector, which is a **unit vector** in the system’s state space.

A qubit is the simplest quantum mechanical system with a 2 dimensional state space {{< katex >}}\mathbb{C}^2{{< /katex >}}. Qubit states are often described as {{< katex >}}\alpha\vert0\rangle+\beta\vert1\rangle{{< /katex >}}, which is a linear combination of the orthonormal basis states {{< katex >}}\vert0\rangle{{< /katex >}} and {{< katex >}}\vert1\rangle{{< /katex >}}. {{< katex >}}\alpha{{< /katex >}} and {{< katex >}}\beta{{< /katex >}} are both complex numbers subject to the conditions {{< katex >}}\lVert\alpha\rVert^2+\lVert\beta\rVert^2=1{{< /katex >}}, thus satisfying the condition that they are a unit vector within the state space {{< katex >}}\mathbb{C}^2{{< /katex >}}.

It is also worthy to remember that {{< katex >}}\lVert\alpha\rVert^2{{< /katex >}} and {{< katex >}}\lVert\beta\rVert^2{{< /katex >}} represent the probabilities of measuring {{< katex >}}\vert0\rangle{{< /katex >}} and {{< katex >}}\vert1\rangle{{< /katex >}}.

# Further Reading

In this page, we have only covered the notation that we will use in the subsequent pages to describe entanglement. However, there is so much more math and linear algebra that are used in quantum mechanics! If interested, you can refer to Chapter 2 of Quantum coherence in photosynthesis by **Dr.** Ng Tiong Eng[^Ng2020] or Chapter 2 of Quantum Computation and Quantum Information[^Nielsen2010] by Michael Nielsen and Isaac Chuang. For the more mathematically advanced, you can also refer to Chapter 1 of Modern Quantum Mechanics[^Sakurai2020] by J. J. Sakurai and Jim Napolitano.

[^Ng2020]: Tiong Eng, Ng. (2020). "Quantum coherence in photosynthesis". http://hdl.handle.net/10497/22624
[^Nielsen2010]: Nielsen, Michael A.; Chuang, Isaac L. (2010). Quantum Computation and Quantum Information (2nd ed.). Cambridge: Cambridge University Press. ISBN 978-1-107-00217-3.
[^Sakurai2020]: Sakurai, J. J.; Napolitano, Jim (2020). Modern Quantum Mechanics (3rd ed.). Cambridge. ISBN 978-1-108-47322-4.
