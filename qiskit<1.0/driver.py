import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, AncillaRegister
from qiskit.circuit.library import MCXGate

def encode_state(num_ue, num_ap):
    """Create a quantum circuit with state and auxiliary qubits initialized."""
    n_state = int(np.ceil(np.log2(num_ap))) * num_ue
    state = QuantumRegister(n_state, name="s")
    aux = AncillaRegister(1, name="a")
    qc = QuantumCircuit(state, aux)
    
    qc.h(state)  # uniform superposition
    return state, aux, qc

def run_amplitude_amplification(qc, num_iter=3):
    """Wrap amplitude amplification loop."""
    from qiskit.circuit.library import ZGate
    diffuser = qc.copy()
    n = len(qc.qubits)
    diffuser.h(range(n))
    diffuser.x(range(n))
    diffuser.h(n-1)
    diffuser.mct(list(range(n-1)), n-1)
    diffuser.h(n-1)
    diffuser.x(range(n))
    diffuser.h(range(n))

    full = qc.copy()
    for _ in range(num_iter):
        full.compose(diffuser, inplace=True)
    full.measure_all()
    return full

def decode_counts(counts, num_ue, num_ap):
    """Convert bitstring output to integer assignment list."""
    def bitstring_to_assign(bitstring):
        n = int(np.ceil(np.log2(num_ap)))
        return [int(bitstring[i*n:(i+1)*n], 2) for i in range(num_ue)]

    decoded = [(bitstring_to_assign(k[::-1]), v) for k, v in counts.items()]
    decoded.sort(key=lambda x: -x[1])
    return [x[0] for x in decoded]
