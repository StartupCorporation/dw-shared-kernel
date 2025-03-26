from dataclasses import dataclass

from dw_shared_kernel.domain.specification.base import Specification


@dataclass(kw_only=True, slots=True, frozen=True)
class NotEmptyStringSpecification(Specification[str]):
    can_be_nullable: bool

    def is_satisfied_by(
        self,
        value: str | None,
    ) -> bool:
        return True if value is None and self.can_be_nullable else bool(value and value.strip())
