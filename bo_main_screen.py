import pygame
import bo_scene_manager as SceneManager

from breakout_gameobject import GameObject
from bo_text_display import TextDisplay




class MainMenu(GameObject):
    """Controls text and input on main menu
    """
    START_KEY = pygame.K_SPACE
    
    TITLE_DISPLAY = TextDisplay((200,150), "BREAKOUT BREAKDOWN INFINITE", text_size=48)
    SUBTITLE_DISPLAY = TextDisplay((250,210), "A project developed for the Bachelor in Videojogos at Lusofona University, by Rafael Castro e Silva", text_size=16)
    
    
    
    flash_timer = 0
    
    def setup(self):
        self.add_child(self.TITLE_DISPLAY)
        self.add_child(self.SUBTITLE_DISPLAY)
        self.START_DISPLAY = TextDisplay((400,500), "--- PRESS " +pygame.key.name(self.START_KEY) + " TO START ---", text_size=24)
        self.add_child(self.START_DISPLAY)

    
    def update_behaviour(self, delta):
        keys = pygame.key.get_pressed()
        
        self.flash_timer += 2 * delta
        if int(self.flash_timer) % 2 == 0:
          
            self.START_DISPLAY.visible = False
            
        else:
            self.START_DISPLAY.visible = True
        
        if keys[self.START_KEY]:
            SceneManager.switch_scene(1)
            

    
    def handle_collisions(self, collisions: [], delta):
        pass
    