from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def publish(self):
        pass
