import pygame

from breakout_block import Block
from bo_collider_aabb import AABB_Collider
from vector3 import Vector3

class Paddle(Block):
    
    
    mouse_controlled = True
    paddle_speed = 1
    paddle_direction = 0
    
    # for mouse input correction
    CAMERA_CORRECTION = 0
    V_RES = 0
    H_RES = 0
    
    def setup(self):
        self.my_collider = AABB_Collider(Vector3(self.width, self.height, self.depth))

    def update_behaviour(self, delta):
        
        keys = pygame.key.get_pressed()
        
        if not self.mouse_controlled:
            if(keys[pygame.K_RIGHT]):
                self.paddle_direction = 1
            elif(keys[pygame.K_LEFT]):
                self.paddle_direction = -1
            else:
                self.paddle_direction = 0
            self.position.x += self.paddle_speed * self.paddle_direction * delta
        elif self.mouse_controlled:
            if pygame.mouse.get_focused():
                mouse_pos = pygame.mouse.get_pos()
                # Taken from game sample
                mouse_pos = ((mouse_pos[0] / self.H_RES) * 2 - 1, (mouse_pos[1] / self.V_RES) * 2 - 1)
                self.position.x = mouse_pos[0] * self.CAMERA_CORRECTION # Multiply by camera's Y position at angle -35
                #print(pygame.mouse.get_pos()[0])              