import math

from breakout_gameobject import GameObject
from mesh import Mesh
from vector3 import Vector3
from material import Material
from color import Color
from quaternion import Quaternion

class Block(GameObject):
    
    DEFAULT_HEIGHT = 0.8
    DEFAULT_WIDTH = 1.5
    DEFAULT_DEPTH = 1
    
    #mesh for all blocks
    BLOCK_MESH = Mesh.create_cube((DEFAULT_WIDTH, DEFAULT_HEIGHT,DEFAULT_DEPTH) )
    
    def __init__(self, height = DEFAULT_HEIGHT, width = DEFAULT_WIDTH, depth = DEFAULT_DEPTH, start_pos = Vector3(0, 0, 0), color = Color(0, 1, 0, 1)):
        
        self.height = height
        self.width = width
        self.depth = depth
        
        self.position = start_pos
        self.rotation = Quaternion.identity()
        self.scale = Vector3(1,1,1)
        if (height == self.DEFAULT_HEIGHT) and (width == self.DEFAULT_WIDTH) and (depth == self.DEFAULT_DEPTH):
            self.mesh = self.BLOCK_MESH
        else:
            self.mesh = Mesh.create_cube((self.height, self.width, self.depth))
        
        self.material = Material(color, "Block Material")
        self.children = []
        
    def setup(self):
        pass
    
    def update_behaviour(self, delta):
        pass
    
        
        