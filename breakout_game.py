import pygame
import time

from scene import Scene
from camera import Camera
#from color import Color

HORIZONTAL_RESOLUTION = 1280
VERTICAL_RESOLUTION = 720
#BACKGROUND_COLOR = pygame.Color(255, 0, 0) #red



__current_scene = Scene("empty", pygame.Color(0,255,0))

def __Main():
    """
    Main app loop
    """
    # Pygame initialization
    pygame.init()
    window = pygame.display.set_mode((HORIZONTAL_RESOLUTION, VERTICAL_RESOLUTION))
    
    
    
    # Cameras
    game_camera = Camera(False, HORIZONTAL_RESOLUTION, VERTICAL_RESOLUTION)
    menu_camera = Camera(False, HORIZONTAL_RESOLUTION, VERTICAL_RESOLUTION)
    
    # Scene initialisation
    game_scene = Scene("GameScene", pygame.Color(0,0,255))
    menu_scene = Scene("MainMenu",pygame.Color(255,0,0))
    
    game_scene.camera = game_camera
    menu_scene.camera = menu_camera
    
    
    # Set up delta time
    delta_time = 0
    prev_time = time.time()
    
    # Show mouse cursor
    pygame.mouse.set_visible(True)
    # Don't lock the mouse cursor to the game window
    pygame.event.set_grab(False)
   
    is_running = True
    
    switch_scene(menu_scene)
    # Main game loop
    while is_running:

        for event in pygame.event.get():
            # Checks if the user closed the window
            if event.type == pygame.QUIT:
                # Exits the application immediately
                is_running = False
        
        # Update the Display
        window.fill(__current_scene.BACKGROUND_COLOR)
        __current_scene.update_objects(delta_time)
        __current_scene.render(window)
        pygame.display.flip()
        
        # Updates delta time, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()
        
def switch_scene(new_scene) -> Scene:
    __current_scene = new_scene
    __current_scene.start_scene()

__Main()