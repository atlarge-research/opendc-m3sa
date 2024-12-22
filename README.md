# M3SA

Multi- and Meta-Model Simulation and Analysis for ICT infrastructure.

---

**Contents**

-   [Abstract](#abstract)
-   [Repository Structure](#repository-structure)
-   [M3SA Architecture](#m3sa-architecture)
-   [Reproducibility capsule](#reproducibility-capsule)
-   [Open Science](#open-science)
-   [License](#license)

---

## Abstract

Datacenters are vital for the digital society but represent a considerable fraction of global energy consumption. To improve their sustainability and performance when demand is foreseen to increase, we envision simulators and simulation-based digital twins will become primary decision-making tools. However, unlike other fields focusing on key societal infrastructure such as waterworks and mass transit, datacenter simulators cannot yet combine multiple, independent models into their operation. Addressing this challenge, in this work we propose M3SA, a datacenter simulation and analysis framework that uses discrete-event simulation to predict, per model and combined into a meta-model, the impact on climate and performance of various realistic datacenter conditions. We design an architecture for simulating with multiple concurrent models, a technique to integrate the results of multiple models into a meta-model, and a procedure to evaluate the accuracy of the meta-model.

## Repository Structure

-   `m3sa/` - M3SA independent tool
-   `m3sa-opendc/` - M3SA coupled with OpenDC
-   `reproducibility-capsule` - Reproducibility capsule of the experiments in the paper
-   `M3SA-technical-report.pdf` - Technical report of the paper
-   `README.md` - _you are here_
-   `LICENSE` - License file (MIT, Open Science)
-   others (e.g., `m3sa-architecture.png`, `.gitignore`, etc.)

## M3SA Architecture

![m3sa-architecture.png](m3sa-architecture.png)

We design M3SA to be capable of operating coupled or decoupled from a datacenter simulator. The figure above depicts an overview of the system's architecture, in which M3SA extends a black-boxed simulator. We couple M3SA with OpenDC, a peer-reviewed, open-source, discrete-event simulator with simple interfaces, and over 5 years of development and operation.

The user interacts with the system through the Input Interface (A) and Output Interface (B) interfaces. The M3SA process begins with the user configuring the Multi-Model (C) and the Meta-Model (D). The simulation process is triggered and controlled by the M3SA backend, occurring between (M)-(S): the system sets up a simulation based on user input, simulates, and centralizes predictions. The simulation block (M)-(S) reflects the operation of discrete-event simulators commonly used in the field, similar to the architectures of OpenDC and CloudSim; specifically, the simulation assembler (M) is where single models are typically defined in current experiments.

## Reproducibility capsule
### Reproducibility (with docker)
```bash
cd reproducibility-capsule 
```

```bash
sudo docker build -t m3sa .
```
```bash
sudo docker run -it m3sa
````
### Reproducibility capsule (without docker)
Step 1 (alternative) - without docker
#### Dependencies
- Gradle
- JDK 21
- Python 3.12
- Make

```bash
cd reproducibility-capsule
make build
make run
```

## Open Science
We provide M3SA as open-source software, under the MIT license. Together with M3SA, we make open-source the trace archive used throughout the experiments.  Double-blinded submission link: https://anonymous.4open.science/r/trace-archive/.

## License

M3SA is distributed under the MIT license. See [LICENSE](/LICENSE).
