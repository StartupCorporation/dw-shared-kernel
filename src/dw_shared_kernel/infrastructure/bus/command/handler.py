from abc import ABC, abstractmethod

from dw_shared_kernel.infrastructure.bus.command.message import Command


class CommandHandler[COMMAND: Command](ABC):
    @abstractmethod
    async def __call__(self, command: COMMAND) -> None: ...
