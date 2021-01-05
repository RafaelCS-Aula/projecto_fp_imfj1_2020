import math

from breakout_gameobject import GameObject
from mesh import Mesh
from vector3 import Vector3
from material import Material
from color import Color
from quaternion import Quaternion

from bo_collider_sphere import Sphere_Collider

class Ball(GameObject):
    
    ball_speed = 0
    starting_pos = Vector3(0,0,0)
    DEFAULT_RADIUS = 0.6
    DEFAULT_SPEED = 3
    SPEED_INCREMENT = 0.5
    
    def __init__(self, name, start_pos, radius = DEFAULT_RADIUS, speed = DEFAULT_SPEED,  color = Color(0,1,1,1)):
        self.radius = Vector3(radius, radius, radius)
        self.position = start_pos
        self.scale = Vector3(1,1,1)
        self.mesh = Mesh.create_sphere(self.radius, 6, 6)
        self.material = Material(color, "Ball Material")
        self.rotation = Quaternion.AngleAxis(Vector3(0,0,1), math.radians(180))
        self.name = name
        self.children = []
    
        self.ball_speed = speed
        
        self.my_collider = Sphere_Collider(radius * 0.2)
        self.handled_collisions = []
    
    def setup(self):
       
        pass

    
    def update_behaviour(self, delta):
        self.rotation = Quaternion.AngleAxis(self.up(), 100 * math.radians(delta * self.ball_speed)) * self.rotation
        
        if not self.my_collider.is_colliding:
            #print("not hit")
            self.handled_collisions = []
        # Ball goes forward
        #self.position.z = 0
        self.position += self.ball_speed * self.up() * delta
        
    def handle_collisions(self, collisions: [], delta):
        
        unhandled_colisions = [c for c in collisions]
      
        for col in unhandled_colisions:
          #  print("With: " + col.name)
          #  print(col not in self.handled_collisions)
          #  print(self.my_collider.is_colliding)
            if col not in self.handled_collisions:
           #     print(self.up())
            #    print(-self.up())
                other_collision_point = col.my_collider.closest_point_on_surface(col.position, self.position)
                my_collision_point = self.my_collider.closest_point_on_surface(self.position, col.position)
                
                if col.name == "PADDLE":
                    print("PADDLE HIT")
                    direction = self.position - col.position
                    direction.normalize()
                    dot = direction.dot(self.up())
                   
                    #clamp dot product to exactl 1 or -1
                    if dot > 1:
                        dot = 1
                    elif dot < -1:
                        dot = -1
                    
                    #print(dot)
                   
                    mag_product = direction.magnitude_squared() * self.up().magnitude_squared()
                   
                    #print(mag_product)
                    angle_rad = math.acos(dot / mag_product)
                   
                    mod = -1
                    if self.position.x < col.position.x:
                        mod = 1
                    self.rotate_angle(-angle_rad)
                   #self.rotation = Quaternion.AngleAxis(Vector3(0,0,1), math.radians(angle_rad * 3)) * self.rotation
                else:
                    print("STANDART HIT")
                   # Reflection formula
                   #reflectionDirection = ProjectileDirection - 2(ProjectileDirection DOT wallsNormalVector)*wallsNormalVector. 
                   
                    collision_normal = Vector3(0,0,0)
                    if my_collision_point.x > self.position.x: #right side hit
                        collision_normal = -col.right() #Hit surface is col's left side
                    elif my_collision_point.x < self.position.x:
                        collision_normal = -col.right()
                    elif my_collision_point.y < self.position.y: # Bottom side
                        collision_normal = col.up()
                    elif my_collision_point.y > self.position.y: # top side hit
                        collision_normal = -col.up()
                    
                    ricochet = self.up() - (2*(self.up().dot(collision_normal.normalized()))) * collision_normal
                   
                    print(ricochet)
                   
                    dot = ricochet.dot(self.up())
                    mag_product = ricochet.magnitude_squared() * self.up().magnitude_squared()
                   
                    #print(mag_product)
                    angle_rad = math.acos(dot / mag_product)
                   
                    #self.rotate_angle(angle_rad)
                    self.rotation *= Quaternion.AngleAxis(Vector3(0,0,1),angle_rad)
                    if col.name == "BLOCK":
                        col.queue_destroy = True
                
                self.ball_speed += self.SPEED_INCREMENT
            self.handled_collisions.append(col)
                #print(col.name)"""
       
    def rotate_angle(self, angle):
        """Rotates the ball to a certain angle, parallel to the ground

        Args:
            angle (Vector3): Angle in degrees to snap the rotation to
        """
        self.rotation = Quaternion.AngleAxis(Vector3(0,0,1), angle)
        
        
        