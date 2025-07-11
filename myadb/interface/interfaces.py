# Abstract interfaces for Clean Architecture

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Union, Tuple

class IDeviceGateway(ABC):
    """Interface for Android device operations."""
    @abstractmethod
    def discover_devices(self) -> List[Dict[str, str]]:
        pass
    @abstractmethod
    def execute_device_command(self, device_id: str, command: str) -> Tuple[str, str, int]:
        pass
    @abstractmethod
    def get_device_status(self, device_id: str) -> str:
        pass
    @abstractmethod
    def send_keyevent(self, device_id: str, keycode: str) -> Tuple[str, str, int]:
        pass
    @abstractmethod
    def install_apk(self, device_id: str, apk_path: str) -> Tuple[str, str, int]:
        pass

class IFileSystemGateway(ABC):
    """Interface for file system operations."""
    @abstractmethod
    def read_file(self, path: str) -> str:
        pass
    @abstractmethod
    def write_file(self, path: str, content: str) -> bool:
        pass
    @abstractmethod
    def file_exists(self, path: str) -> bool:
        pass
    @abstractmethod
    def open_file_in_editor(self, path: str) -> bool:
        pass
    @abstractmethod
    def select_file(self, initial_dir: str = None, file_types: List[Tuple[str, str]] = None) -> Optional[str]:
        pass

class IJsonConfigGateway(ABC):
    """Interface for JSON configuration operations."""
    @abstractmethod
    def parse_config(self, json_content: str) -> Dict[str, Any]:
        pass
    @abstractmethod
    def validate_config(self, config: Dict[str, Any]) -> Tuple[bool, List[str]]:
        pass

class IProcessExecutor(ABC):
    """Interface for process execution operations."""
    @abstractmethod
    def execute(self, command: Union[str, List[str]], shell: bool = False) -> Tuple[str, str, int]:
        pass
    @abstractmethod
    def execute_shell_command(self, command: str) -> Tuple[str, str, int]:
        pass
    @abstractmethod
    def execute_application(self, application_path: str, args: List[str] = None) -> bool:
        pass

class IUserInterfacePresenter(ABC):
    """Interface for user interface presentation."""
    @abstractmethod
    def show_message(self, message: str, message_type: str = 'info') -> None:
        pass
    @abstractmethod
    def update_ui(self, data: Dict[str, Any]) -> None:
        pass
    @abstractmethod
    def create_dynamic_buttons(self, button_definitions: List[Dict[str, Any]]) -> None:
        pass
    @abstractmethod
    def update_devices_list(self, devices: List[Dict[str, str]]) -> None:
        pass
    @abstractmethod
    def append_log(self, log_entry: str, entry_type: str = 'info') -> None:
        pass
    @abstractmethod
    def clear_log(self) -> None:
        pass
    @abstractmethod
    def prompt_user_input(self, prompt: str, default_value: str = '') -> Optional[str]:
        pass

class ICommand(ABC):
    """Interface for command objects."""
    @abstractmethod
    def execute(self) -> Tuple[bool, str]:
        pass
    @abstractmethod
    def get_description(self) -> str:
        pass

class ILogService(ABC):
    """Interface for logging services."""
    @abstractmethod
    def log_info(self, message: str) -> None:
        pass
    @abstractmethod
    def log_error(self, message: str, exception: Optional[Exception] = None) -> None:
        pass
    @abstractmethod
    def log_command(self, command: str, device_id: Optional[str] = None) -> None:
        pass
    @abstractmethod
    def log_command_result(self, stdout: str, stderr: str, return_code: int) -> None:
        pass
    @abstractmethod
    def get_logs(self) -> List[Dict[str, Any]]:
        pass
    @abstractmethod
    def clear_logs(self) -> None:
        pass

class IVariableSubstitutor(ABC):
    """Interface for variable substitution services."""
    @abstractmethod
    def substitute_variables(self, text: str, global_vars: Dict[str, str]) -> str:
        pass
    @abstractmethod
    def get_required_variables(self, text: str) -> List[str]:
        pass
