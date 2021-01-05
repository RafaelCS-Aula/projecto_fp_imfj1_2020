import pygame
from breakout_gameobject import GameObject

class TextDisplay(GameObject):
    
    
    
    
    def __init__(self, screen_position, text, text_size = 16, text_color = (255, 255, 255)):
        self.name = "TEXTDISPLAY"
        self.screen_position = screen_position    
        self.text = text_size
        self.text_color = text_color
        self.text_size = text_size
        
        self.GAME_FONT = pygame.freetype.SysFont("ComicSansMS", self.text_size)
        
    def setup(self):
        pass
    
    
    def update_behaviour(self, delta):
        pass

   
   
    def handle_collisions(self, collisions: [], delta):
        pass
    
    def display_text(self, surface):
        self.GAME_FONT.render_to(surface,self.screen_position, self.text, self.text_color)