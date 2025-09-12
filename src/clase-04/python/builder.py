"""
Clase 4 — Patrones Creacionales
Ejemplo: Builder (Python)
-------------------------
Construye un objeto complejo paso a paso con method chaining.
"""
from typing import Optional

class Computer:
    def __init__(self, cpu: Optional[str] = None, ram: Optional[int] = None, storage: Optional[str] = None, gpu: Optional[str] = None):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu

    def __str__(self):
        return f"Computer(cpu={self.cpu}, ram={self.ram}, storage={self.storage}, gpu={self.gpu})"


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self, cpu: str):
        self.cpu = cpu
        return self

    def add_ram(self, ram: str):
        self.ram = ram
        return self

    def add_storage(self, storage: str):
        self.storage = storage
        return self

    def add_gpu(self, gpu: str):
        self.gpu = gpu
        return self

    def build(self) -> Computer:
        computer = Computer (
            cpu = self.cpu,
            ram = self.ram,
            storage = self.storage,
            gpu = self.gpu,
        )
        return computer


if __name__ == "__main__":
    builder = ComputerBuilder()
    workstation = (builder.add_cpu("AMD Ryzen 9")
                          .add_ram("64GB")
                          .add_storage("2TB NVMe")
                          .add_gpu("NVIDIA RTX A5000")
                          .build())
    print(workstation)
