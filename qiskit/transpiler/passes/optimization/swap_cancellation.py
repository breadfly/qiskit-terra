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

"""Cancel back-to-back `swap` gates in dag."""

from qiskit.transpiler.basepasses import TransformationPass


class SwapCancellation(TransformationPass):
    """Cancel back-to-back `swap` gates in dag."""

    def run(self, dag):
        """Run the SwapCancellation pass on `dag`.

        Args:
            dag (DAGCircuit): the directed acyclic graph to run on.

        Returns:
            DAGCircuit: Transformed DAG.
        """
        swap_runs = dag.collect_runs(["swap"])
        for swap_run in swap_runs:
            # Partition the cx_run into chunks with equal gate arguments
            partition = []
            chunk = []
            for i in range(len(swap_run) - 1):
                chunk.append(swap_run[i])

                qargs0 = swap_run[i].qargs
                qargs1 = swap_run[i + 1].qargs

                if qargs0 != qargs1:
                    partition.append(chunk)
                    chunk = []
            chunk.append(swap_run[-1])
            partition.append(chunk)
            # Simplify each chunk in the partition
            for chunk in partition:
                if len(chunk) % 2 == 0:
                    for n in chunk:
                        dag.remove_op_node(n)
                else:
                    for n in chunk[1:]:
                        dag.remove_op_node(n)
        return dag
