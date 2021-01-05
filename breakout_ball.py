import pygame
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
    LOWER_LIMIT = -7
    
    ACTIVATE_BALL_KEY = pygame.K_SPACE
    
    def __init__(self, name, start_pos, radius = DEFAULT_RADIUS, speed = DEFAULT_SPEED,  color = Color(0,1,1,1)):
        self.radius = Vector3(radius, radius, radius)
        self.starting_pos = start_pos
        self.position = start_pos
        self.scale = Vector3(1,1,1)
        self.mesh = Mesh.create_sphere(self.radius, 6, 6)
        self.material = Material(color, "Ball Material")
        #self.rotation = Quaternion.AngleAxis(Vector3(0,0,1), math.radians(180))
        self.rotation = Quaternion.identity()
        self.name = name
        self.children = []
    
        self.ball_speed = speed
        self.direction_vector = Vector3(0,0,0)
        
        self.my_collider = Sphere_Collider(radius * 0.2)
        self.handled_collisions = []
        
        self.active = False
    
    def setup(self):
       self.reset_ball()
        

    
    def update_behaviour(self, delta):
        if not self.active:
            keys = pygame.key.get_pressed()
            if keys[self.ACTIVATE_BALL_KEY]:
                self.active = True
            return
        
        self.rotation = Quaternion.AngleAxis(self.up(), 100 * math.radians(delta * self.ball_speed)) * self.rotation
        
        if not self.my_collider.is_colliding:
            #print("not hit")
            self.handled_collisions = []
        # Ball goes forward
        #self.position.z = 0
        
        
        self.position += self.ball_speed * self.direction_vector.normalized() * delta
        
        #Check input to activate ball
        
            
        
        if self.position.y < self.LOWER_LIMIT:
            print("Ball Reset")
            self.reset_ball()
        
    def handle_collisions(self, collisions: [], delta):
        if not self.active:
            return
        unhandled_colisions = [c for c in collisions]
      
        for col in unhandled_colisions:
          #  print("With: " + col.name)
          #  print(col not in self.handled_collisions)
          #  print(self.my_collider.is_colliding)
            if col not in self.handled_collisions:

                other_collision_point = col.my_collider.closest_point_on_surface(col.position, self.position)
                my_collision_point = self.my_collider.closest_point_on_surface(self.position, col.position)
                
                # Check the normal of the colision, assuming AABB colisions
                collision_normal = Vector3(0,0,0)
                if my_collision_point.x > self.position.x: #right side hit
                    collision_normal = -col.right() #Hit surface is col's left side
                elif my_collision_point.x < self.position.x:
                    collision_normal = -col.right()
                elif my_collision_point.y < self.position.y: # Bottom side
                    collision_normal = col.up()
                elif my_collision_point.y > self.position.y: # top side hit
                    collision_normal = -col.up()
                    
               # if col.name == "PADDLE":
               #     print("PADDLE HIT")
               #     direction = self.position - col.position
               #     direction.normalize()
               #     dot = direction.dot(self.up())
               #    
               #     #clamp dot product to exactl 1 or -1
               #     if dot > 1:
               #         dot = 1
               #     elif dot < -1:
               #         dot = -1
                    
                    #print(dot)
                   
                #    mag_product = direction.magnitude_squared() * self.up().magnitude_squared()
                   
                    #print(mag_product)
                #    angle_rad = math.acos(dot / mag_product)
                   
                #    mod = -1
                #    if self.position.x < col.position.x:
                #        mod = 1
                #    self.rotate_angle(-angle_rad)
                   #self.rotation = Quaternion.AngleAxis(Vector3(0,0,1), math.radians(angle_rad * 3)) * self.rotation
                #else:
                if True:
                    print("STANDART HIT")
                   # Reflection formula
                   #reflectionDirection = ProjectileDirection - 2(ProjectileDirection DOT wallsNormalVector)*wallsNormalVector. 
                   
                    
                    direction_normal_dot = min(1, max(-1,(self.direction_vector.dot(collision_normal)))) 
                   
                    ricochet = self.direction_vector - 2 * direction_normal_dot * collision_normal
                   
                    print(ricochet)
                    self.direction_vector = ricochet
                    
                    #dot = (min(1, max(-1, ricochet.dot(self.up()))))
                    #print(dot)
                    #mag_product = ricochet.magnitude_squared() * self.up().magnitude_squared()
                    #print(mag_product)
                    #print(dot / mag_product)
                    #print(mag_product)
                    #angle_rad = math.acos((min(1, max(-1,dot / mag_product))))
                    #print(angle_rad)
                    #self.rotate_angle(angle_rad)
                    #self.rotation = Quaternion.AngleAxis(Vector3(0,0,1),math.radians(angle_rad * 10)) 
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
    
    def reset_ball(self):
        self.position = self.starting_pos
        self.active = False
        self.ball_speed = self.DEFAULT_SPEED
        self.direction_vector = -self.up()
        
        
        