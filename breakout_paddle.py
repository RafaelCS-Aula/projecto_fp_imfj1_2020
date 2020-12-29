import pygame
from breakout_block import Block
#import breakout_game as game

class Paddle(Block):
    
    mouse_controlled = True
    paddle_speed = 1
    paddle_direction = 0
    
    def setup(self):
        pass

    def update_behaviour(self, delta):
        if not self.mouse_controlled:
            #for event in pygame.event.get():
             #   if event.type == pygame.KEYDOWN
            keys = pygame.key.get_pressed()
            
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
                #mouse_pos = ((mouse_pos[0] / 1280) * 2 - 1, (mouse_pos[1] / 720) * 2 - 1)
                self.position.x = mouse_pos[0]
                print(pygame.mouse.get_pos()[0])              