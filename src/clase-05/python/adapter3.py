from __future__ import annotations
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
import json
from typing import Any, Dict

# Interfaz objetivo que el cliente espera (JSON string)
class NewInterface(ABC):
    @abstractmethod
    def request(self) -> str:  # pragma: no cover
        pass

# Clase existente (incompatible)
class OldSystem:
    def specific_request(self) -> str:
        # Ejemplo más complejo: lista y anidamiento
        return """<usuario id="u123">
                    <nombre>Ana</nombre>
                    <emails>
                      <email>ana@example.com</email>
                      <email>ana.work@example.com</email>
                    </emails>
                    <direccion>
                      <calle>Av. Siempre Viva</calle>
                      <numero>742</numero>
                      <ciudad>Springfield</ciudad>
                    </direccion>
                  </usuario>"""

# Helper: convierte un Element en dict recursivamente
def _element_to_dict(elem: ET.Element) -> Dict[str, Any]:
    node: Dict[str, Any] = {}

    # 1) atributos -> se prefijan con '@'
    for k, v in elem.attrib.items():
        node[f"@{k}"] = v

    # 2) hijos
    children = list(elem)
    if children:
        for child in children:
            child_dict = _element_to_dict(child)
            # child_dict viene como {child.tag: value}
            tag = child.tag
            value = child_dict[tag]

            # si ya existe la clave -> convertir a lista / agregar
            if tag in node:
                if isinstance(node[tag], list):
                    node[tag].append(value)
                else:
                    node[tag] = [node[tag], value]
            else:
                node[tag] = value

        # 3) texto directo (si existe y no es sólo espacios)
        text = elem.text.strip() if elem.text and elem.text.strip() else None
        if text:
            # si ya hay hijos, guardamos el texto bajo '#text'
            node["#text"] = text

        return {elem.tag: node}

    # Caso hoja (sin hijos): devolver texto (vacío string si no tiene)
    text = elem.text.strip() if elem.text and elem.text.strip() else ""
    # si tiene atributos pero no texto, devolvemos atributos como dict
    if node:
        # node contiene atributos sólo; añadir texto (aunque vacío)
        node["#text"] = text
        return {elem.tag: node}

    return {elem.tag: text}

# Adapter: traduce XML → JSON
class Adapter(NewInterface):
    def __init__(self, adaptee: OldSystem):
        self._adaptee = adaptee

    def request(self) -> str:
        raw_xml = self._adaptee.specific_request()
        try:
            root = ET.fromstring(raw_xml)
        except ET.ParseError as e:
            # Manejo básico del error: devolver JSON con info de error
            return json.dumps({"error": "XML inválido", "details": str(e)}, ensure_ascii=False)

        # Convertimos el árbol empezando por la raíz
        converted = _element_to_dict(root)  # e.g. {'usuario': {...}}
        # Extraemos el contenido de la raíz (para mantener comportamiento similar al ejemplo original)
        data = converted[root.tag]

        # Serializar a JSON (preservando unicode)
        return json.dumps(data, ensure_ascii=False, indent=2)

def main():
    old = OldSystem()
    adapter = Adapter(old)
    
    print("Salida no adaptada:", old.specific_request())
    print("Salida adaptada:", adapter.request())

if __name__ == "__main__":
    main()