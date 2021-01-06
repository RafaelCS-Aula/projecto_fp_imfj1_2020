from bo_collider import Collider
from vector3 import Vector3

class AABB_Collider(Collider):


    def __init__(self, size: Vector3):
        self.dimensions = size

    def within_bounds(self, my_position: Vector3, other_point: Vector3):
        """Check if the given point in inside the box

        Args:
            my_position (Vector3): Center position of box
            other_point (Vector3): Point being tested

        Returns:
            Bool: Point is within bounds
        """

        aabb_bounds = self.__get_max_min(my_position)
        if( (other_point.x < aabb_bounds[0].x and # Within max X
             other_point.x > aabb_bounds[1].x) and # Within min X
            (other_point.y < aabb_bounds[0].y and # Within max Y
             other_point.y > aabb_bounds[1].y) and # Within min Y
           (other_point.z < aabb_bounds[0].z and # Within max Z
             other_point.z > aabb_bounds[1].z) ): # Within min Z

            self.is_colliding = True
        else:
            self.is_colliding = False
        return self.is_colliding


    def closest_point_on_surface(self, my_position, other_point: Vector3):
        """Get the closest point on the surface of the box towards other point

        Args:
            my_position (Vector3): Center position of box
            other_point (Vector3): Point being tested

        Returns:
            Tuple(Vector3, Vector3): The closest point on the box's surface in [0], and the surface normal of the point in [1]
            
        """
        closest_point = Vector3(other_point.x, other_point.y, other_point.z)
        aabb_bounds = self.__get_max_min(my_position)

        surface_normal = Vector3(0,0,0)

        if other_point.x > aabb_bounds[0].x:
            closest_point.x = aabb_bounds[0].x
            surface_normal.x = 1
        elif other_point.x < aabb_bounds[1].x:
            closest_point.x = aabb_bounds[1].x
            surface_normal.x = -1
        if other_point.y > aabb_bounds[0].y:
            closest_point.y = aabb_bounds[0].y
            surface_normal.y = 1
        elif other_point.y < aabb_bounds[1].y:
            closest_point.y = aabb_bounds[1].y
            surface_normal.y = -1

        if other_point.z > aabb_bounds[0].z:
            closest_point.z = aabb_bounds[0].z
            surface_normal.z = 1
        elif other_point.z < aabb_bounds[1].z:
            closest_point.z = aabb_bounds[1].z
            surface_normal.z = -1

        return (closest_point, surface_normal)

    def __get_max_min(self, origin: Vector3):
        """Return the Max and Min points of this box, assuming constant dimensions

        Args:
            origin (Vector3): Center of the Box

        Returns:
            [tuple]: The max point in [0] and min point in [1] 
        """
        aabb_max = Vector3(origin.x + self.dimensions.x * 0.5,
                           origin.y + self.dimensions.y * 0.5,
                           origin.z + self.dimensions.z * 0.5)

        aabb_min = Vector3(origin.x - self.dimensions.x * 0.5,
                           origin.y - self.dimensions.y * 0.5,
                           origin.z - self.dimensions.z * 0.5)

        return (aabb_max, aabb_min)