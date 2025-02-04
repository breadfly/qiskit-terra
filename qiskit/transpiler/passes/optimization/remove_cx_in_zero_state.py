# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Remove CX gate when the control qubit is in zero state."""

from qiskit.transpiler.basepasses import TransformationPass


class RemoveCXInZeroState(TransformationPass):
    """Remove CX gate when the control qubit is in zero state."""

    def run(self, dag):
        """Run the CXCancellation pass on `dag`.

        Args:
            dag (DAGCircuit): the directed acyclic graph to run on.

        Returns:
            DAGCircuit: Transformed DAG.
        """
        cx_runs = dag.collect_runs(["cx"])
        for cx_run in cx_runs:
            predecessor = next(dag.predecessors(cx_run))
            if predecessor.type == "in":
                dag.remove_op_node(cx_run)
        return dag
