import pygame

from breakout_block import Block
from bo_text_display import TextDisplay
from bo_collider_aabb import AABB_Collider
from vector3 import Vector3

class Paddle(Block):
    """Player controlled paddle that sends the ball flying when hit
    """

    
    # for mouse input correction
    CAMERA_CORRECTION = 0
    V_RES = 0
    H_RES = 0
    CONTROLS_FLIP_KEY = pygame.K_q
    
    PADDLE_SPEED = 10
    
        
    mouse_controlled = False
    paddle_direction = 0
    
    controls_text = TextDisplay((16, 240), "", text_color=(255, 255, 255))
    
    current_ctrls_text = TextDisplay((16, 260), "", text_size=14, text_color=(220, 220, 220))
    
    def setup(self):
       
        self.add_child(self.controls_text)
        self.add_child(self.current_ctrls_text)
        self.controls_text.text = "Press [" + pygame.key.name(self.CONTROLS_FLIP_KEY) +"] to switch controls"
        self.my_collider = AABB_Collider(Vector3(self.width, self.height, self.depth))

    def update_behaviour(self, delta):
        
        self.current_ctrls_text.text = self.get_controls()
        
        keys = pygame.key.get_pressed()
        
        
        if not self.mouse_controlled: #Keyboard controls
            if(keys[pygame.K_RIGHT]):
                self.paddle_direction = 1
            elif(keys[pygame.K_LEFT]):
                self.paddle_direction = -1
            else:
                self.paddle_direction = 0
            self.position.x += self.PADDLE_SPEED * self.paddle_direction * delta
        elif self.mouse_controlled: # Match x with mouse x
            if pygame.mouse.get_focused():
                mouse_pos = pygame.mouse.get_pos()
                # Taken from game sample
                mouse_pos = ((mouse_pos[0] / self.H_RES) * 2 - 1, (mouse_pos[1] / self.V_RES) * 2 - 1)
                self.position.x = mouse_pos[0] * self.CAMERA_CORRECTION 
        if keys[self.CONTROLS_FLIP_KEY]: # Switch between mouse and keyboard controls
            if self.mouse_controlled:
                self.mouse_controlled = False
            elif not self.mouse_controlled:
                self.mouse_controlled = True
                            
    def handle_collisions(self, collisions: [], delta):
         pass
     
    def get_controls(self):
        
        if self.mouse_controlled:
            return "MOUSE [<-(')->]"
        else:
            return "ARROW KEYS [<-] [->]"