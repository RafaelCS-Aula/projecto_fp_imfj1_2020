import pygame
from breakout_block import Block
import breakout_game as game

class Paddle(Block):
    
    mouse_controlled = True
    paddle_speed = 1
    paddle_direction = 0
    
    def setup(self):
        pass

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
                mouse_pos = ((mouse_pos[0] / game.HORIZONTAL_RESOLUTION) * 2 - 1, (mouse_pos[1] / game.VERTICAL_RESOLUTION) * 2 - 1)
                self.position.x = mouse_pos[0] * game.game_scene.camera.position.y # Multiply by camera's Y position at angle -35
                print(pygame.mouse.get_pos()[0])              