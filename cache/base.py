from abc import ABC, abstractmethod

class BaseCache(ABC):

    @abstractmethod
    def set(self, key: str, value, expire: int = 3600):
        pass

    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def delete(self, key: str):
        pass

    @abstractmethod
    def clear(self):
        pass
