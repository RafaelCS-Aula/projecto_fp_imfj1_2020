import math

from breakout_gameobject import GameObject
from mesh import Mesh
from vector3 import Vector3
from material import Material
from color import Color
from quaternion import Quaternion

from bo_collider_sphere import Sphere_Collider

class Ball(GameObject):
    
    ball_speed = 0.2
    starting_pos = Vector3(0,0,0)
    DEFAULT_RADIUS = 1
    DEFAULT_SPEED = 1
    
    def __init__(self, name, start_pos, radius = DEFAULT_RADIUS, speed = DEFAULT_SPEED,  color = Color(0,1,1,1)):
        self.radius = Vector3(radius, radius, radius)
        self.position = start_pos
        self.scale = Vector3(1,1,1)
        self.mesh = Mesh.create_sphere(self.radius, 6, 6)
        self.material = Material(color, "Ball Material")
        self.rotation = Quaternion.AngleAxis(Vector3(0,0,1), math.radians(180))
        self.name = name
        self.children = []
    
        
        self.my_collider = Sphere_Collider(radius)
        self.handled_collisions = []
    
    def setup(self):
       
        pass

    
    def update_behaviour(self, delta):
        self.rotation = Quaternion.AngleAxis(self.up(), 100 * math.radians(delta)) * self.rotation
        
        if not self.my_collider.is_colliding:
            self.handled_collisions = []
        # Ball goes forward
        self.position += self.ball_speed * self.up() * delta
        
    def handle_collisions(self, collisions: []):
        unhandled_colisions = [c for c in collisions]
        for col in unhandled_colisions:
            if self.my_collider.is_colliding and col not in self.handled_collisions:
                if col.name == "PADDLE":
                   print("PADDLE HIT")
                else:
                   print("STANDART HIT")
            self.handled_collisions.append(col)
        
       
       
         
    
    def rotate_angle(self, angle):
        """Rotates the ball to a certain angle, parallel to the ground

        Args:
            angle (Vector3): Angle in degrees to snap the rotation to
        """
        self.rotation = Quaternion.AngleAxis(Vector3(0,0,1), math.radians(angle))
        
        
        