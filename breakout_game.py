import pygame
import time
import math

from scene import Scene
from camera import Camera
#from color import Color

HORIZONTAL_RESOLUTION = 1280
VERTICAL_RESOLUTION = 720
BACKGROUND_COLOR = pygame.Color(255, 0, 0) #red


is_running = True

scene_collection = []

current_scene = 0

def Main():
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
    game_scene = Scene("GameScene")
    menu_scene = Scene("MainMenu")
    
    game_scene.camera = game_camera
    menu_scene.camera = menu_camera
    
    scene_collection.append(menu_scene)
    scene_collection.append(game_scene)
    
    # Set up delta time
    delta_time = 0
    prev_time = time.time()
    
    # Show mouse cursor
    pygame.mouse.set_visible(True)
    # Don't lock the mouse cursor to the game window
    pygame.event.set_grab(False)
   
    is_running = True
    
    # Main game loop
    while is_running:

        for event in pygame.event.get():
            # Checks if the user closed the window
            if event.type == pygame.QUIT:
                # Exits the application immediately
                is_running = False
        
        # Update the Display
        window.fill(BACKGROUND_COLOR)
        if current_scene < len(scene_collection) and current_scene > -1:
            scene_collection[current_scene].update_objects(delta_time)
            scene_collection[current_scene].render(window)
        pygame.display.flip()
        
        # Updates delta time, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()
    
Main()