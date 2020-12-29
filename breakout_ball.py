import pygame
import math

from breakout_gameobject import GameObject
from mesh import Mesh
from vector3 import Vector3
from material import Material
from color import Color
from quaternion import Quaternion




class Ball(GameObject):
    
    ball_speed = 1
    starting_pos = Vector3(0,0,0)
  
    
    def __init__(self, radius, speed = ball_speed, start_pos = Vector3(0, 0, 0), color = Color(0,1,1,1)):
        self.radius = Vector3(radius, radius, radius)
        self.position = start_pos
        self.scale = Vector3(1,1,1)
        #Create our mesh
        self.mesh = Mesh.create_sphere(self.radius, 6, 6)
        self.material = Material(color, "Ball Material")
        self.rotation = Quaternion.AngleAxis(Vector3(0,0,1), math.radians(180))
        
        self.children = []
        self.tick = 0
    
    def setup(self):
        pass    
        

    
    def update_behaviour(self, delta):
        self.rotation = Quaternion.AngleAxis(Vector3(0,1,0), 1 * delta) * self.rotation
        self.position += self.ball_speed * self.up() * delta