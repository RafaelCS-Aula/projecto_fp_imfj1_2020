from bo_collider import Collider
from vector3 import Vector3

class Sphere_Collider(Collider):
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def within_bounds(self, my_position: Vector3, other_point: Vector3):
        
        distance = (my_position - other_point).magnitude_squared()
        if distance <= self.radius:
            self.is_colliding = True
        elif distance > self.radius:
            self.is_colliding = False
        return self.is_colliding
            
    def closest_point_on_surface(self, my_position, other_point: Vector3):
        """Get the closest point on the surface of the sphere towards other point

        Args:
            my_position (Vector3): Center position of sphere
            other_point (Vector3): Point being tested

        Returns:
            Tuple(Vector3, Vector3): The closest point on the sphere's surface in [0], and the surface normal of the point in [1]
            
        """
        direction = other_point - my_position
        direction.normalize()
        direction *= self.radius
        closest_point = my_position + direction
        
        
        return (closest_point, direction)
    