# Domain Entities for MyAdb (Clean Architecture)

from typing import List, Dict, Any, Optional

class Device:
    def __init__(self, id: str, status: str, model: str):
        self.id = id
        self.status = status
        self.model = model

class ButtonDefinition:
    def __init__(self, label: str, color: str, position: Dict[str, int], functions: List[str]):
        self.label = label
        self.color = color
        self.position = position
        self.functions = functions

class FunctionDefinition:
    def __init__(self, name: str, commands: List[str]):
        self.name = name
        self.commands = commands

class InputDefinition:
    def __init__(self, name: str, prompt: str, default: Optional[str] = None):
        self.name = name
        self.prompt = prompt
        self.default = default

class GlobalInputItem:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

class UIConfig:
    def __init__(self, title: str, global_inputs: List[GlobalInputItem], buttons: List[ButtonDefinition]):
        self.title = title
        self.global_inputs = global_inputs
        self.buttons = buttons

class LogEntry:
    def __init__(self, timestamp: str, command: str, stdout: str, stderr: str, success: bool):
        self.timestamp = timestamp
        self.command = command
        self.stdout = stdout
        self.stderr = stderr
        self.success = success
