from abc import ABC, abstractmethod
from typing import List

class BrowserAgent(ABC):
    """ Abstract class for browser Agent"""
    model: str
    verbose: bool = False

    @abstractmethod
    def run(self, tasks: List[str]) -> str:
        """Take a list of class and execute them"""
