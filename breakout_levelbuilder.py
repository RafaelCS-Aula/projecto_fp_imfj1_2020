import random
import bo_score_keeper as ScoreKeeper

from camera import Camera
from breakout_ball import Ball
from breakout_block import Block
from breakout_wall import Wall
from vector3 import Vector3
from color import Color
from breakout_gameobject import GameObject
from breakout_paddle import Paddle
from bo_text_display import TextDisplay




class LevelBuilder(GameObject):


    GRID_X = 10
    GRID_Y = 6
    LEVEL_BLOCK_INCREMENT = 4
    BASE_BLOCK_AMOUNT = 20
    SPACE_X = Block.DEFAULT_WIDTH
    SPACE_Y = Block.DEFAULT_HEIGHT
    # Middle of level
    MID_X = GRID_X / 2
    #midpoint_Y = GRID_Y / 2
    GAME_BALL = Ball("BALL", start_pos=Vector3(0, -GRID_Y * (SPACE_Y - 0.3), 0))
    GAME_PADDLE = Paddle("PADDLE", height=0.5, width=2, start_pos=Vector3(0, -GRID_Y * SPACE_Y, 0), color=Color(1,0,0,1))
    
    current_stage = 0
    block_grid = []
    living_blocks = []
    my_scene = None
    
    stage_display = TextDisplay((16, 356),"", text_color=(255, 100,100))

    
    
    def setup(self):
        self.add_child(self.stage_display) 
        
        
        
    def update_behaviour(self, delta):
        self.living_blocks = self.my_scene.get_objects_by_name("BLOCK")
        #print(len(self.living_blocks))
        if len(self.living_blocks) <= 0:
            self.GAME_BALL.reset_ball()
            self.make_level(self.my_scene, min(self.GRID_X * self.GRID_Y, self.BASE_BLOCK_AMOUNT + self.LEVEL_BLOCK_INCREMENT))
            
        self.stage_display.text = "STAGE: " + str(self.current_stage)
        
    def make_level(self, scene_to_populate, blocks_amount = BASE_BLOCK_AMOUNT):
        
        ScoreKeeper.current_score += ScoreKeeper.SCORE_LEVEL_BONUS * self.current_stage
        self.current_stage += 1
        
        layout_grid = [[(x,y) for y in range(self.GRID_Y + 1)] for x in range(self.GRID_X + 1)]
        placed_blocks = 0
        self.my_scene = scene_to_populate
        self.block_grid = []
        self.children = []
        self.living_blocks = []
        
        # Populate the level with blocks
        while placed_blocks < blocks_amount:
            for x in range(len(layout_grid[0])):
                for y in range(len(layout_grid[x])):
                    if placed_blocks >= blocks_amount:
                        break    
                    rnd = random.randrange(0, 101)
                    # Chance of blocks being placed increases with amount alread placed
                    #(placed_blocks + 1)/(blocks_amount + 1)
                    if rnd <= 100 * (placed_blocks + 1)/(blocks_amount + 1):
                        print((placed_blocks + 1)/(blocks_amount + 1))
                        # Add a block to the block grid in the right position
                        self.block_grid.append(Block("BLOCK", start_pos=Vector3(self.SPACE_X * x, self.SPACE_Y * y, 0), color=Color(random.uniform(0.1, 1),random.uniform(0.1, 1), 0, 1 )))
                        placed_blocks += 1
                        #print("Placed ")
                       # print(placed_blocks)
                        #print("Blocks")
        if self.current_stage == 1:
            # Side Walls
            self.block_grid.append(Wall("WALL", start_pos=Vector3(self.GRID_X * self.SPACE_X , 0, 0), color=Color(1,1,1,1), height= 15))
            self.block_grid.append(Wall("WALL", start_pos=Vector3(-self.SPACE_X, 0, 0), color=Color(1,1,1,1), height= 15))
        
            # Top Wall
            self.block_grid.append(Wall("WALL", start_pos=Vector3(self.MID_X , self.GRID_Y * self.SPACE_Y + 1, 0), color=Color(1,1,1,1), width= 20, depth=2))
                    
        #Populate scene
        for b in self.block_grid:
            scene_to_populate.add_object(b)
        
        self.living_blocks = scene_to_populate.get_objects_by_name("BLOCK")
        
        scene_to_populate.add_object(self.GAME_BALL)
                          
        scene_to_populate.add_object(self.GAME_PADDLE)
        
        scene_to_populate.update_collision_agents()
        
        for c in self.block_grid:
            c.position.x -= self.MID_X
  
        
    def handle_collisions(self,collisions: [], delta):
        pass
        
                
        
        
        
    

    

