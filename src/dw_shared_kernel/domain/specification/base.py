from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(kw_only=True, slots=True, frozen=True)
class Specification[VALUE](ABC):
    @abstractmethod
    def is_satisfied_by(self, value: VALUE) -> bool: ...
