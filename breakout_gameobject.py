from abc import abstractmethod

from object3d import Object3d
from bo_collider import Collider


class GameObject(Object3d):
    """
    Object in the scene with logic, inherits Object3d
    """
    my_collider: Collider = None
    
    """Whether the scene is to destroy this object before the next update frame
    """
    queue_destroy = False
    
    @abstractmethod
    def setup(self):
        """Is called at the beginning of the scene to which this object belongs
        """
        pass
    @abstractmethod
    def update_behaviour(self, delta):
        """Called every frame this object is in an active scene

        Args:
            delta (float): time since last frame, used in calculations
        """
        pass

    @abstractmethod
    def handle_collisions(self, collisions: [], delta):
        """Resolve all colisions detected with this object's colider, if it has one

        Args:
            collisions ([type]): Colliding colliders
            delta (float): time since last frame, used in calculations
        """
        pass