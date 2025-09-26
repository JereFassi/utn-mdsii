from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...

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
    def undo(self) -> None:
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    def execute(self) -> None:
        self.light.off()
    def undo(self) -> None:
        self.light.on()

class RemoteControl:
    def __init__(self, history_limit: int = 100):
        self._undo_stack: List[Command] = []
        self._redo_stack: List[Command] = []
        self.history_limit = history_limit

    def run(self, cmd: Command) -> None:
        cmd.execute()
        self._push_undo(cmd)
        self._redo_stack.clear()

    def undo(self) -> None:
        if not self._undo_stack:
            print("Nada para deshacer")
            return
        cmd = self._undo_stack.pop()
        cmd.undo()
        self._redo_stack.append(cmd)

    def redo(self) -> None:
        if not self._redo_stack:
            print("Nada para rehacer")
            return
        cmd = self._redo_stack.pop()
        cmd.execute()
        self._undo_stack.append(cmd)

    def _push_undo(self, cmd: Command) -> None:
        self._undo_stack.append(cmd)
        if len(self._undo_stack) > self.history_limit:
            self._undo_stack.pop(0)

if __name__ == "__main__":
    light = Light()
    remote = RemoteControl()

    remote.run(LightOnCommand(light))   
    remote.run(LightOffCommand(light))  

    remote.undo() 
    remote.undo() 

    remote.redo()  
    remote.redo()  
