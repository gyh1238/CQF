# CQF – Continuous-valued Quantum Framework for Network Assignment  
*A universal quantum workflow for inter-/intra-cell resource optimisation*

> **Paper:** “A Universal Quantum Framework for Assignment Optimisation in  
> Network Administration” (IEEE X, 20xx)  
> **Authors:** Yong Hun Jang · Junyoung Hwang · Wookjin Lee · Sang Hyun Lee

---

## 1  Overview : What is CQF?  
CQF implements the **gate-level quantum algorithm** proposed in the paper.  
It tackles two nested network-management problems:

1. **Inter-cell user association** – choose the best Access Point (AP) for every User Equipment (UE) while respecting each AP’s access limit.  
2. **Intra-cell RB allocation** – assign Resource Blocks (RBs) to the UEs served by the same AP, maximising total throughput.

Classical brute force needs  \|𝐶\| = *M​N*  evaluations; CQF lowers the cost to  
*O*(√\|𝐶\|⁄\|𝐹\|) amplitude-amplification iterations by  
*encoding continuous metrics (power, rate) directly as qubit phases* and enforcing combinatorial constraints with modular oracles. :contentReference[oaicite:1]{index=1}

---

## 2  Repository layout


CQF/
├─ fig/                 # High-resolution figures used in the paper
│  ├─ fig1\_network\_overview\.png
│  ├─ fig2\_quantum\_flow\.png
│  ├─ fig3\_qubit\_encoding.png
│  ├─ fig4\_access\_limit\_oracles.png
│  ├─ fig5\_phase\_rotation.png
│  └─ fig6\_performance\_korea\_map.png
├─ qiskit<1.0/          # Stand-alone code tested on Qiskit 0.46
│  ├─ inter\_cell\_demo.ipynb
│  ├─ intra\_cell\_demo.ipynb
│  ├─ oracle.py
│  ├─ phase\_utils.py
│  └─ README\_code.md
└─ README.md            # (you are here)



### What lives where?

| Path / file | Purpose |
|-------------|---------|
| **fig/**    | All illustrations appearing as Fig. 1-6 in the paper, exported to PNG for GitHub rendering. |
| **qiskit&lt;1.0/** | Pure-Python implementation compatible with Qiskit **&lt; 1.0** (0.46 tested). Each notebook reproduces one of the experiments shown in Fig. 6. |
| `oracle.py` | Gate factories for (i) access-limit selection, (ii) RB exclusivity, and (iii) multi-controlled phase kicks. |
| `phase_utils.py` | Helper functions that map real-valued link metrics to bounded phase increments 0 → π. :contentReference[oaicite:3]{index=3} |

---

## 3  Quick start

```bash
# 1. Clone
git clone https://github.com/gyh1238/CQF.git
cd CQF

# 2. (Recommended) Create a fresh Conda env
conda create -n cqf python=3.10
conda activate cqf
pip install qiskit==0.46 jupyterlab matplotlib

# 3. Run the tutorials
jupyter lab qiskit<1.0/inter_cell_demo.ipynb
jupyter lab qiskit<1.0/intra_cell_demo.ipynb
````

Each notebook initialises **state qubits** for assignments, attaches **auxiliary qubits** for constraint checks, applies the **oracle → diffusion loop** *⌊π⁄4 √|𝐶|⁄|𝐹|⌋* times, and measures the optimal solution.&#x20;

---

## 4  Reproducing the paper’s figures

| Figure                              | Script / notebook                                | How to generate                                                                   |
| ----------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------- |
| **Fig 1-5** (concept)               | Already in *fig/*                                | No action needed – diagrams were drawn in Adobe Illustrator.                      |
| **Fig 6** (Korea-campus evaluation) | `inter_cell_demo.ipynb`, `intra_cell_demo.ipynb` | Run all cells; the notebook saves `fig6_performance_korea_map.png` inside *fig/*. |

---

## 5  Results and Visualisation

CQF demonstrates high-quality solutions under both problem types:

| Task                          | Exact-optimal hit-rate | ≤ 5% deviation |
|------------------------------|------------------------|----------------|
| Inter-cell power minimisation | **98.6%**              | **98.6%**      |
| Intra-cell throughput maximisation | **96.8%**         | **96.8%**      |

### 📍 Inference Histograms
These histograms show the measured quantum output bitstrings over 100,000 shots.
Each spike indicates a feasible assignment decoded from the qubit register.

<div align="center">
  <img src="fig/inter_histogram.png" width="380"/>
  <br><em>Fig – Measured bitstring distribution for inter-cell assignment</em>
</div>

<div align="center">
  <img src="fig/intra_histogram.png" width="380"/>
  <br><em>Fig – Measured bitstring distribution for intra-cell assignment</em>
</div>

### 🔍 Quantum Circuits
The exact quantum circuits for each case are constructed with controlled phase rotations and constraint oracles.

<div align="center">
  <img src="fig/inter_circuit.png" width="500"/>
  <br><em>Fig – Quantum circuit for inter-cell association</em>
</div>

<div align="center">
  <img src="fig/intra_circuit.png" width="700"/>
  <br><em>Fig – Quantum circuit for intra-cell RB allocation</em>
</div>

These circuits use modular constraint encoders (see `oracle.py`) and phase encoding functions (`phase_utils.py`) to support arbitrary cost models. Bitwise exclusivity, access limits, and real-valued link costs are handled by custom oracles applied before amplitude amplification.

---

## 6  Citing

If CQF helps your research, please cite the original article:

```bibtex
@article{jang2025cqf,
  title   = {A Universal Quantum Framework for Assignment Optimization in Network Administration},
  author  = {Jang, Yong Hun and Hwang, Junyoung and Lee, Wookjin and Lee, Sang Hyun},
  journal = {IEEE X},
  year    = {20xx},
}
```

---

## 7  Contact / Questions

Open an issue or reach out to **disclose \[at] korea.ac.kr**.
Contributions (bug reports, pull requests, alternative oracle designs) are welcome!

---

<p align="center">
  <img src="fig/fig2_quantum_flow.png" width="500"/>
  <br><em>Fig 2 – Universal quantum flow implemented by this repo.</em>
</p>
```

*Happy quantum hacking!* 🎉
