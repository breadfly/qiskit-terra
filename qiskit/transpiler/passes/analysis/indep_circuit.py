# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Return the list of independent circuits of a DAG circuit."""

from qiskit.transpiler.basepasses import AnalysisPass


class IndepCircuit(AnalysisPass):
    """Return the list of independent circuits of a DAG circuit.
    For example, if circuit has 3 qubits and 1 CNOT gate between 0th qubit and 1st qubit.
    Then, we can divide into 2 independent circuit.
    So return [[0,1], [2]].

    The result is saved in ``property_set['indep_circuit']`` as an list of list of integer.
    """

    def run(self, dag):
        """Run the IndepCircuit pass on `dag`."""
        
        self.property_set["indep_circuit"] = dag.indep_circuit()
