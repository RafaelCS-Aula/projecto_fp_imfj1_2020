import random

from camera import Camera
from breakout_ball import Ball
from breakout_block import Block
from breakout_paddle import Paddle
from vector3 import Vector3
from color import Color
from breakout_gameobject import GameObject


GRID_X = 10
GRID_Y = 6

current_level = 0
BASE_BLOCK_AMOUNT = 10

class LevelBuilder(GameObject):
    layout_grid = [[(x,y) for y in range(GRID_Y + 1)] for x in range(GRID_X + 1)]

    
        
        #Move this object so the block grid is centered
    def setup(self):
        #self.make_level(BASE_BLOCK_AMOUNT)
        pass
        
        
    def update_behaviour(self, delta):
        if len(self.children) == 0:
            pass
        
    def make_level(self, blocks_amount):
        placed_blocks = 0
        block_grid = []
        
        spaceX = Block.DEFAULT_WIDTH
        spaceY = Block.DEFAULT_HEIGHT
        
        # Populate the level with blocks
        while placed_blocks <= blocks_amount:
            for x in range(len(self.layout_grid[0])):
                for y in range(len(self.layout_grid[x])):
                    rnd = random.randrange(0, 101)
                    # Chance of blocks being placed increases with amount alread placed
                    if(rnd <= 1/(placed_blocks + 1/blocks_amount + 1) * 100):
                    
                    # Add a block to the block grid in the right position
                        block_grid.append(Block(start_pos=Vector3(spaceX * x, spaceY * y, 0), color=Color(random.uniform(0.1, 1),random.uniform(0.1, 1), 0, 1 )))
                        placed_blocks += 1
        for i in range(0,len(block_grid)):
            self.children.append(block_grid[i])
            
        
                
        
        
        
    

    

