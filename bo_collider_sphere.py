from bo_collider import Collider
from vector3 import Vector3

class Sphere_Collider(Collider):
    
    def __init__(self, radius):
        self.radius = radius
    
    def within_bounds(self, my_position: Vector3, other_point: Vector3):
        distance = (my_position - other_point).magnitude_squared()
        if distance <= self.radius:
            self.is_colliding = True
        else:
            self.is_colliding = False
        return self.is_colliding
            
    def closest_point_on_surface(self, my_position, other_point: Vector3):
        direction = other_point - my_position
        direction.normalize()
        direction *= self.radius
        closest_point = direction + my_position
        return closest_point
    