import random

from camera import Camera
from breakout_ball import Ball
from breakout_block import Block
from vector3 import Vector3
from color import Color
from breakout_gameobject import GameObject
from breakout_paddle import Paddle



class LevelBuilder(GameObject):


    #paddle_obj = Paddle()
    #ball_obj = Ball()
    GRID_X = 10
    GRID_Y = 6
    current_level = 0
    BASE_BLOCK_AMOUNT = 12
    SPACE_X = Block.DEFAULT_WIDTH
    SPACE_Y = Block.DEFAULT_HEIGHT
    # Middle of level
    MID_X = GRID_X / 2
    #midpoint_Y = GRID_Y / 2
        
    def setup(self):
        self.make_level(self.BASE_BLOCK_AMOUNT)
        
        
        
    def update_behaviour(self, delta):
        pass
        
    def make_level(self, blocks_amount):
        layout_grid = [[(x,y) for y in range(self.GRID_Y + 1)] for x in range(self.GRID_X + 1)]
        placed_blocks = 0
        block_grid = []
        self.children = []
        

        
        
        # Populate the level with blocks
        while placed_blocks < blocks_amount:
            for x in range(len(layout_grid[0])):
                for y in range(len(layout_grid[x])):
                    if placed_blocks >= blocks_amount:
                        break    
                    rnd = random.randrange(0, 101)
                    # Chance of blocks being placed increases with amount alread placed
                    if(rnd <= 100 * ((placed_blocks + 1)/(blocks_amount + 1))):
                        print((placed_blocks + 1)/(blocks_amount + 1))
                        # Add a block to the block grid in the right position
                        block_grid.append(Block("BLOCK", start_pos=Vector3(self.SPACE_X * x, self.SPACE_Y * y, 0), color=Color(random.uniform(0.1, 1),random.uniform(0.1, 1), 0, 1 )))
                        placed_blocks += 1
                        print("Placed ")
                        print(placed_blocks)
                        print("Blocks")
                        
                    
            
                        
        for i in range(0,len(block_grid)):
            self.children.append(block_grid[i])
        
        
        
        #Move block field to center of screen
        #self.position.y -= midpoint_Y
        self.position.x -= self.MID_X 
        
        # spawn paddle
       # paddle_obj = Paddle(start_pos=Vector3(midpoint_X, -GRID_Y * spaceY, 0), color=Color(1,0,0,1))
        
        print("spawn paddle")
        
        #spawn Ball
       # ball_obj = Ball(start_pos=Vector3(midpoint_X, -GRID_Y * spaceY, 0 ))
        
        print("spawn ball")
        
        
        
                
        
        
        
    

    

