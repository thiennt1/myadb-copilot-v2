# Abstract interfaces for Clean Architecture

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Union, Tuple

class IDeviceGateway(ABC):
    """Interface for Android device operations.
    
    This interface defines methods for discovering and interacting with Android devices
    through the Android Debug Bridge (ADB).
    """
    
    @abstractmethod
    def discover_devices(self) -> List[Dict[str, str]]:
        """Discovers all connected Android devices.
        
        Returns:
            List[Dict[str, str]]: List of dictionaries containing device information,
                                 with keys like 'id', 'status', and 'model'.
        """
        pass
    
    @abstractmethod
    def execute_device_command(self, device_id: str, command: str) -> Tuple[str, str, int]:
        """Executes an ADB command on the specified device.
        
        Args:
            device_id (str): The target device identifier.
            command (str): The ADB command to execute.
            
        Returns:
            Tuple[str, str, int]: A tuple containing (stdout, stderr, return_code).
        """
        pass
    
    @abstractmethod
    def get_device_status(self, device_id: str) -> str:
        """Gets the current status of a device.
        
        Args:
            device_id (str): The device identifier.
            
        Returns:
            str: Device status ('online', 'offline', etc.).
        """
        pass
    
    @abstractmethod
    def send_keyevent(self, device_id: str, keycode: str) -> Tuple[str, str, int]:
        """Sends a keyevent to the specified device.
        
        Args:
            device_id (str): The target device identifier.
            keycode (str): The Android keycode to send.
            
        Returns:
            Tuple[str, str, int]: A tuple containing (stdout, stderr, return_code).
        """
        pass
    
    @abstractmethod
    def install_apk(self, device_id: str, apk_path: str) -> Tuple[str, str, int]:
        """Installs an APK on the specified device.
        
        Args:
            device_id (str): The target device identifier.
            apk_path (str): Path to the APK file.
            
        Returns:
            Tuple[str, str, int]: A tuple containing (stdout, stderr, return_code).
        """
        pass


class IFileSystemGateway(ABC):
    """Interface for file system operations.
    
    This interface defines methods for reading, writing, and managing files and directories.
    """
    
    @abstractmethod
    def read_file(self, path: str) -> str:
        """Reads the content of a file.
        
        Args:
            path (str): Path to the file.
            
        Returns:
            str: The content of the file.
        """
        pass
    
    @abstractmethod
    def write_file(self, path: str, content: str) -> bool:
        """Writes content to a file.
        
        Args:
            path (str): Path to the file.
            content (str): Content to write.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        pass
    
    @abstractmethod
    def file_exists(self, path: str) -> bool:
        """Checks if a file exists.
        
        Args:
            path (str): Path to the file.
            
        Returns:
            bool: True if the file exists, False otherwise.
        """
        pass
    
    @abstractmethod
    def open_file_in_editor(self, path: str) -> bool:
        """Opens a file in the system's default editor.
        
        Args:
            path (str): Path to the file.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        pass
    
    @abstractmethod
    def select_file(self, initial_dir: str = None, file_types: List[Tuple[str, str]] = None) -> Optional[str]:
        """Opens a file selection dialog.
        
        Args:
            initial_dir (str, optional): Initial directory to display. Defaults to None.
            file_types (List[Tuple[str, str]], optional): List of file types to filter. Defaults to None.
            
        Returns:
            Optional[str]: Selected file path or None if canceled.
        """
        pass


class IJsonConfigGateway(ABC):
    """Interface for JSON configuration operations.
    
    This interface defines methods for parsing and managing JSON configuration files.
    """
    
    @abstractmethod
    def parse_config(self, json_content: str) -> Dict[str, Any]:
        """Parses JSON configuration content.
        
        Args:
            json_content (str): JSON content string.
            
        Returns:
            Dict[str, Any]: Parsed configuration as a dictionary.
        """
        pass
    
    @abstractmethod
    def validate_config(self, config: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validates a configuration dictionary.
        
        Args:
            config (Dict[str, Any]): Configuration dictionary.
            
        Returns:
            Tuple[bool, List[str]]: Tuple of (is_valid, list_of_errors).
        """
        pass


class IProcessExecutor(ABC):
    """Interface for process execution operations.
    
    This interface defines methods for executing system commands and processes.
    """
    
    @abstractmethod
    def execute(self, command: Union[str, List[str]], shell: bool = False) -> Tuple[str, str, int]:
        """Executes a command and returns its output.
        
        Args:
            command (Union[str, List[str]]): Command string or list of command arguments.
            shell (bool, optional): Whether to use shell execution. Defaults to False.
            
        Returns:
            Tuple[str, str, int]: A tuple containing (stdout, stderr, return_code).
        """
        pass
    
    @abstractmethod
    def execute_shell_command(self, command: str) -> Tuple[str, str, int]:
        """Executes a shell command.
        
        Args:
            command (str): Shell command string.
            
        Returns:
            Tuple[str, str, int]: A tuple containing (stdout, stderr, return_code).
        """
        pass
    
    @abstractmethod
    def execute_application(self, application_path: str, args: List[str] = None) -> bool:
        """Executes an application.
        
        Args:
            application_path (str): Path to the application executable.
            args (List[str], optional): Command line arguments. Defaults to None.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        pass


class IUserInterfacePresenter(ABC):
    """
    Interface for UI presentation logic.
    - show_message: Display a message to the user.
    - update_ui: Update UI components with new data.
    """
    @abstractmethod
    def show_message(self, message):
        pass
    @abstractmethod
    def update_ui(self, data):
        pass

class ICommand(ABC):
    """
    Interface for command objects that can be executed.
    - execute: Perform the command's action.
    """
    @abstractmethod
    def execute(self):
        pass
