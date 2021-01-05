import pygame

from breakout_block import Block
from bo_text_display import TextDisplay
from bo_collider_aabb import AABB_Collider
from vector3 import Vector3

class Paddle(Block):
    

    
    # for mouse input correction
    CAMERA_CORRECTION = 0
    V_RES = 0
    H_RES = 0
    CONTROLS_FLIP_KEY = pygame.K_q
    
    PADDE_SPEED = 6
    
        
    mouse_controlled = False
    paddle_direction = 0
    
    controls_text = TextDisplay((16, 240), "Press [" + pygame.key.name(CONTROLS_FLIP_KEY) +"] to switch controls", text_color=(255, 255, 255))
    
    current_ctrls_text = TextDisplay((16, 260), "", text_size=14, text_color=(220, 220, 220))
    
    def setup(self):
       
        self.add_child(self.controls_text)
        self.add_child(self.current_ctrls_text)
        
        self.my_collider = AABB_Collider(Vector3(self.width, self.height, self.depth))

    def update_behaviour(self, delta):
        
        self.current_ctrls_text.text = self.get_controls()
        
        keys = pygame.key.get_pressed()
        
        if not self.mouse_controlled:
            if(keys[pygame.K_RIGHT]):
                self.paddle_direction = 1
            elif(keys[pygame.K_LEFT]):
                self.paddle_direction = -1
            else:
                self.paddle_direction = 0
            self.position.x += self.PADDE_SPEED * self.paddle_direction * delta
        elif self.mouse_controlled:
            if pygame.mouse.get_focused():
                mouse_pos = pygame.mouse.get_pos()
                # Taken from game sample
                mouse_pos = ((mouse_pos[0] / self.H_RES) * 2 - 1, (mouse_pos[1] / self.V_RES) * 2 - 1)
                self.position.x = mouse_pos[0] * self.CAMERA_CORRECTION # Multiply by camera's Y position at angle -35
                #print(pygame.mouse.get_pos()[0])  
        if keys[self.CONTROLS_FLIP_KEY]:
            if self.mouse_controlled:
                self.mouse_controlled = False
            elif not self.mouse_controlled:
                self.mouse_controlled = True
                            
    def handle_collisions(self, collisions: [], delta):
        #for c in collisions:
         #   print("Paddle HIT by:" + c.name)
         pass
     
    def get_controls(self):
        
        if self.mouse_controlled:
            return "MOUSE [<-(')->]"
        else:
            return "ARROW KEYS [<-] [->]"