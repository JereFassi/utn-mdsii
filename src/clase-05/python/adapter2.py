from __future__ import annotations
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
import json

# Interfaz objetivo que el cliente espera (JSON)
class NewInterface(ABC):
    @abstractmethod
    def request(self) -> str:
        pass

# Clase existente (incompatible) que no podemos modificar
class OldSystem:
    def specific_request(self) -> str:
        # Devuelve datos en formato XML
        return """<usuario>
                    <id>123</id>
                    <nombre>Ana</nombre>
                    <email>ana@example.com</email>
                  </usuario>"""

# Adapter: traduce XML → JSON
class Adapter(NewInterface):
    def __init__(self, adaptee: OldSystem):
        self._adaptee = adaptee

    def request(self) -> str:
        raw_xml = self._adaptee.specific_request()

        # Parsear el XML
        root = ET.fromstring(raw_xml)
        data = {child.tag: child.text for child in root}

        # Convertir a JSON
        return json.dumps(data, ensure_ascii=False)

def main():
    old = OldSystem()
    adapter = Adapter(old)

    print("Salida no adaptada:", old.specific_request())
    print("Salida adaptada:", adapter.request())

if __name__ == "__main__":
    main()