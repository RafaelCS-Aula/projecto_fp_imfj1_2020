from vector3 import Vector3
from abc import abstractmethod

class Collider():
    
    is_colliding = False
    
    @abstractmethod
    def within_bounds(self, my_position, other_point):
        """Returns true if a certain point within the bounds of the object

        Args:
            my_position (Vector3): The position/center of this collider
            other_point (Vector3): The point to test
        """
        
    @abstractmethod
    def closest_point_on_surface(self, my_position, other_point):
        """Returns the closest point in this collider's surface to the other point

        Args:
            my_position (Vector3): The position/center of this collider
            other_point (Vector3): The point to test
        """
           