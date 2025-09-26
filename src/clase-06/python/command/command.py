from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...

class Light:
    def __init__(self):
        self.state = "off"
    def on(self) -> None:
        self.state = "on"
        print("Luz encendida")
    def off(self) -> None:
        self.state = "off"
        print("Luz apagada")

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    def execute(self) -> None:
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    def execute(self) -> None:
        self.light.off()

class RemoteControl:
    def __init__(self):
        self.history: List[Command] = []
    def run(self, cmd: Command) -> None:
        cmd.execute()
        self.history.append(cmd)

if __name__ == "__main__":
    light = Light()
    remote = RemoteControl()
    remote.run(LightOnCommand(light))
    remote.run(LightOffCommand(light))
