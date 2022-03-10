from abc import ABC
from typing import Dict


class AbstractEvolutionAlg(ABC):
    """An abstract class to be inherited by evolutionary algorithms such as
    Differential Evolution, Swarm Particle Optimization etc."""

    def __init__(self, init_params: Dict[str, int]) -> None:

        pass
