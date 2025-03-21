from dataclasses import dataclass

from dw_shared_kernel.domain.exception.base import DomainException
from dw_shared_kernel.domain.specification.base import Specification


@dataclass(kw_only=True, slots=True, frozen=True)
class StringLengthSpecification(Specification[str]):
    min_length: int
    max_length: int

    def __post_init__(self) -> None:
        if self.min_length > self.max_length:
            raise DomainException("Min length can't be greater than max length in string length specification.")

    def is_satisfied_by(
        self,
        value: str,
    ) -> bool:
        return self.min_length <= len(value) <= self.max_length
