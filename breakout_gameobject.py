from abc import abstractmethod

from object3d import Object3d


class GameObject(Object3d):
    """
    Object in the scene with logic, inherits Object3d
    """
        
    @abstractmethod
    def setup(self):
        pass
    @abstractmethod
    def update_behaviour(self, delta):
        pass