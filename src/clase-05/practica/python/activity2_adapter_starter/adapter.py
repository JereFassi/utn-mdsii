from abc import ABC, abstractmethod
from old_system import OldSystem

class NewInterface(ABC):
    @abstractmethod
    def request(self) -> str:  # pragma: no cover
        pass

class Adapter(NewInterface):
    def __init__(self, adaptee: OldSystem):
        self._adaptee = adaptee

    def request(self) -> str:
        # TODO: traducir la interfaz del adaptee y normalizar el formato (XML → JSON simulado)
        raw = self._adaptee.specific_request()
        normalized = raw.replace(" (XML → datos brutos)", " (normalizado)")                        .replace("<data><msg>", "{'msg':'")                        .replace("</msg></data>", "'}")
        return normalized
