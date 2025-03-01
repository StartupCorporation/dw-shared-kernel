from infrastructure.bus.command.bus import CommandBus
from infrastructure.bus.query.bus import QueryBus
from infrastructure.di.container import Container
from infrastructure.di.layer import Layer


class InfrastructureLayer(Layer):
    def setup(
        self,
        container: Container,
    ) -> None:
        container[QueryBus] = QueryBus()
        container[CommandBus] = CommandBus()
