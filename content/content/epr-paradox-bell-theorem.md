---
title: "EPR Paradox and Bell's Theorem"
katex: true
weight: 7
---

# EPR Paradox

The EPR paradox is a thought experiment intended to demonstrate an inherent paradox in the early formulations of quantum theory. It was to counter an assumption in quantum physics. Niels Bohr and Werner Heisenberg said that a quantum particle or system does not have a definite value until a measurement takes place.

However, if we could predict with certainty the value of a physical quantity without in any way disturbing a system, then there exists an already given value corresponding to that quantity. From this, they inferred that the second particle must have a definite position and/or momentum prior to either being measured. 

{{< columns >}}

{{< figure src="/images/einstein.jpg" caption="Credit: Photograph by Orren Jack Turner, Princeton, N.J" >}}

<--->

{{< figure src="/images/podolsky.jpg" caption="Credit: Emilio Segrè Visual Archives" >}}

<--->

{{< figure src="/images/rosen.jpg" caption="Credit: University of North Carolina at Chapel Hill" >}}

{{< /columns >}}

The paper published by physicists Albert Einstein, Boris Podolsky and Nathan Rosen (EPR)[^EPR1935], describes what happens to 2 systems that are allowed to interact. After a while, the systems will move away from each other and assume that there is no more interaction. 

According to Heisenberg's uncertainty principle, it is impossible to measure both the momentum and the position of particle B exactly; however, it is possible to measure the exact position of particle A. Therefore, the exact position of particle B can be known. Another way to look at this is that when we measure the momentum of particle A, the exact momentum of particle B can be derived without needing to be measured. 

We can use this example for other quantities, for example if A and B were a pair of electrons. There will be a 50% chance A has a positive spin. Assume that we measured A to have a positive electron spin. We can then conclude that B has a 100% chance of having a negative electron spin without disturbing B to measure it. If at any point A changes its spin from positive to negative, then B will also change its spin from negative to positive.

The examples provided above rebut Bohr’s and Heisenberg’s previous statement.

# Bell's Theorem

In Bell's 1964 paper "On the Einstein Podolsky Rosen Paradox"[^Bell1964], he described a test that could determine whether quantum physics was incompatible with local hidden variable theories. Bell's theorem can be generalized the CHSH inequality, developed by Clauser et al.[^CHSH1969]. Experiments have so far all violated this inequality.

Bell's Theorem and its various generalizations also serve as the basis of several applications of quantum entanglement in quantum cryptography, such as the Ekert91 protocol developed by Artur Ekert.[^Ekert1991]

## CHSH Game

The CHSH game, named after the CHSH inequality, is a thought experiment that can be physically realizable, hence provides strong evidence against the local hidden variable theories.

Consider a game with 2 cooperating players, Alice and Bob, and a referee Carol. Alice and Bob are allowed to discuss on a strategy before the game starts, but are not allowed to communicate with each other after it starts. The steps are as follows: 
1. Carol sends 1 bit {{< katex >}}x{{< /katex >}} to Alice and another bit {{< katex >}}y{{< /katex >}} to Bob. Both of these bits have equal probability of being -1 or 1.
2. Alice and Bob each reply Carol with their own bits {{< katex >}}a{{< /katex >}} and {{< katex >}}b{{< /katex >}} respectively.
3. Alice and Bob win the round if {{< katex >}}x\cdot y=a\oplus b{{< /katex >}}, where {{< katex >}}\oplus{{< /katex >}} represents the XOR operation.

{{< video src="/videos/media/videos/animations/720p30/CHSHGame.webm" autoplay=true loop=true style="" >}}

You can even try this game out with 2 friends! You should soon realize that it is impossible to have a classical strategy that guarantees winning every round. In fact, the best possible strategy will only have an expected win rate of {{< katex >}}75\%{{< /katex >}}.

On the other hand, a quantum stratedy allows for a strategy that can have an expected win rate of {{< katex >}}\cos^2\left(\frac{\pi}{8}\right)\approx85\%{{< /katex >}}. The quantum strategy involves Alice and Bob sharing an entangled pair of qubits which are in the state {{< katex >}}\frac{\vert00\rangle+\vert11\rangle}{\sqrt{2}}{{< /katex >}}. By performing certain measurements at the same time and relpying Carol with a bit that depends on the outcome of this measurement, they are able to attain a higher win probability. This would not be possible if there were non-local hidden variables regarding quantum mechanics.

### Proof of win probability of quantum strategy

The winning probability of the quantum strategy is {{< katex >}}\cos^2\left(\frac{\pi}{8}\right){{< /katex >}}, which seems like an odd result. If you are curious about how the quantum strategy works, and how to prove its winning probability, watch the video below by Proffessor Umesh Vazirani[^VaziraniYT] to learn about it!

{{< youtube id="sUQYSy6C1aA" autoplay="true" color="white" yt_start="417" yt_end="815">}}

[^EPR1935]: Einstein, A; B Podolsky; N Rosen (1935). "Can Quantum-Mechanical Description of Physical Reality be Considered Complete?". Physical Review. 47 (10): 777–780. 
[^Bell1964]: J.S. Bell (1964), "On the Einstein Podolsky Rosen Paradox", Physics Physique Физика, 1 (3): 195–200.
[^Ekert1991]: Ekert, Artur (1991). "Quantum cryptography based on Bell's theorem". Physical Review Letters. American Physical Society. 67 (6): 661–663.
[^CHSH1969]: J.F. Clauser; M.A. Horne; A. Shimony; R.A. Holt (1969), "Proposed experiment to test local hidden-variable theories", Phys. Rev. Lett., 23 (15): 880–4.
[^VaziraniYT]: Mareco adolescente (2018). "Lecture 4 3 CHSH INEQUALITY". YouTube. https://www.youtube.com/watch?v=sUQYSy6C1aA
