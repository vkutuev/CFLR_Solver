from typing import Protocol, Hashable


class AllPairsReachabilityAlgorithm(Protocol):

    def solve_all_pairs(self) -> set[tuple[Hashable, Hashable]]:
        """Determines the set of vertex pairs (u, v) in `graph` such that there is a path from u to v
        whose edge labels form a word from the language generated by the context-free grammar `grammar`

        :return: Set of CFL-reachable vertices pairs
        """
        ...