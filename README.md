# CQF – Continuous-valued Quantum Framework for Network Assignment  
*A universal quantum workflow for inter-/intra-cell resource optimisation*

> **Paper:** “A Universal Quantum Framework for Assignment Optimisation in  
> Network Administration” (IEEE X, 20xx)  
> **Authors:** Yong Hun Jang · Junyoung Hwang · Wookjin Lee · Sang Hyun Lee

> **Version note**  
> This repository contains code compatible with **Qiskit ≥ 1.0** (tested on 1.1).  
> Legacy support for Qiskit 0.46 is archived separately.

---

## Overview: What is CQF?

CQF implements a gate-level quantum workflow for solving two key network management problems:

1. **Inter-cell user association** – Assign each User Equipment (UE) to the most suitable Access Point (AP), while enforcing access limits.
2. **Intra-cell resource block (RB) allocation** – Allocate RBs to UEs within the same AP to maximize total throughput.

A classical brute-force search requires evaluating all \|𝐶\| = M<sup>N</sup> configurations.  
CQF reduces this complexity using **amplitude amplification**, requiring only  
**O(√(\|𝐶\|⁄\|𝐹\|))** iterations.

This is achieved by:
- Encoding real-valued metrics (e.g., power, rate) directly into **qubit phases**.
- Enforcing combinatorial constraints using modular oracles.

---

## Repository Layout

```text
CQF/
├── fig/                # All figures used in the paper and extended results
│   ├── fig1_network_overview.png
│   ├── fig2_quantum_flow.png
│   ├── fig3_qubit_encoding.png
│   ├── fig4_access_limit_oracles.png
│   ├── fig5_phase_rotation.png
│   ├── fig6_performance_korea_map.png
│   ├── inter_circuit.png
│   ├── intra_circuit.png
│   ├── inter_histogram.png
│   └── intra_histogram.png
├── qiskit/             # Main implementation (Qiskit ≥ 1.0)
│   ├── inter_cell_demo.ipynb
│   ├── intra_cell_demo.ipynb
│   ├── oracle.py
│   ├── phase_utils.py
│   └── README_code.md
└── README.md
````

---

## Quick start

```bash
# Clone the repo
git clone https://github.com/gyh1238/CQF.git
cd CQF

# (Optional) Set up a clean Python environment
conda create -n cqf python=3.12
conda activate cqf

# Install Qiskit and Jupyter
pip install "qiskit>=1.1" jupyterlab matplotlib

# Run the notebooks
jupyter lab qiskit/inter_cell_demo.ipynb
jupyter lab qiskit/intra_cell_demo.ipynb
````

---

## Quantum Flow Diagram
<div align="center"> <img src="fig/fig2_quantum_flow.png" width="500"/> <br><em>Fig 2 – Quantum optimization loop used in CQF</em> </div>

---

## Reproducing the Paper Figures

| Figure               | Contents                         | Generated from           |
| -------------------- | -------------------------------- | ------------------------ |
| Fig 1–5              | Conceptual illustrations         | Pre-drawn in Illustrator |
| Fig 6                | Campus simulation results        | inter/intra notebooks    |
| inter\_circuit.png   | Gate-level circuit (inter-cell)  | auto-generated           |
| intra\_circuit.png   | Gate-level circuit (intra-cell)  | auto-generated           |
| inter\_histogram.png | Output distribution (inter-cell) | from sampling            |
| intra\_histogram.png | Output distribution (intra-cell) | from sampling            |

---

## Results and Visualization

CQF achieves high fidelity in both problems:

| Task                               | Exact-optimal hit-rate | ≤5% deviation |
| ---------------------------------- | ---------------------- | ------------- |
| Inter-cell power minimization      | 98.6%                  | 98.6%         |
| Intra-cell throughput maximization | 96.8%                  | 96.8%         |

### Inference Histograms

<div align="center">
  <img src="fig/inter_histogram.png" width="380"/>
  <br><em>Measured output bitstrings – inter-cell assignment</em>
</div>

<div align="center">
  <img src="fig/intra_histogram.png" width="380"/>
  <br><em>Measured output bitstrings – intra-cell assignment</em>
</div>

### Gate-Level Quantum Circuits

<div align="center">
  <img src="fig/inter_circuit.png" width="600"/>
  <br><em>Quantum circuit used in inter-cell demo</em>
</div>

<div align="center">
  <img src="fig/intra_circuit.png" width="700"/>
  <br><em>Quantum circuit used in intra-cell demo</em>
</div>

---

## Citation

If you use CQF in your research, please cite the following article:

```bibtex
@article{jang2025cqf,
  title   = {A Universal Quantum Framework for Assignment Optimization in Network Administration},
  author  = {Jang, Yong Hun and Hwang, Junyoung and Lee, Wookjin and Lee, Sang Hyun},
  journal = {IEEE X},
  year    = {20xx}
}
```

---

## Contact

For questions or contributions, open an issue or contact:
📧 **[disclose@korea.ac.kr](mailto:disclose@korea.ac.kr)**

---

<p align="center">
  <img src="fig/fig6_performance_map.png" width="700"/>
  <br><em>Fig 6 – Simulation results for Korea University campus deployment</em>
</p>
```

---
