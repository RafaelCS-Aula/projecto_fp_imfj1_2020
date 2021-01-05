from breakout_block import Block
from bo_collider_aabb import AABB_Collider
from vector3 import Vector3

class Wall(Block):
    def setup(self):
        self.my_collider = AABB_Collider(Vector3(self.width, self.height, self.depth))
        
        
    
    def update_behaviour(self, delta):
        pass
    
    def handle_collisions(self, collisions: [], delta):
        pass