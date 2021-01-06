import pygame
import pygame.freetype
import time
import math
import bo_scene_manager as SceneManager

from scene import Scene
from camera import Camera
from vector3 import Vector3
from quaternion import Quaternion
from breakout_levelbuilder import LevelBuilder
from breakout_paddle import Paddle
from bo_main_screen import MainMenu
#from color import Color

HORIZONTAL_RESOLUTION = 1280
VERTICAL_RESOLUTION = 720





__current_scene = Scene("empty", pygame.Color(0,255,0))

# Scenes initialisation
game_scene = Scene("GameScene", pygame.Color(0,0,30))
menu_scene = Scene("MainMenu",pygame.Color(100,0,0))

def __Main():
    """
    Main app loop
    """
    # Pygame initialization
    pygame.init()
    pygame.freetype.init()
    pygame.display.set_caption("Breakout Breakdown Forever")
    
    window = pygame.display.set_mode((HORIZONTAL_RESOLUTION, VERTICAL_RESOLUTION))
    
    
    
    # Cameras
    game_camera = Camera(False, HORIZONTAL_RESOLUTION, VERTICAL_RESOLUTION)
    menu_camera = Camera(True, HORIZONTAL_RESOLUTION, VERTICAL_RESOLUTION)
    
    # Tilt camera to desired view
    game_camera.position -= Vector3(0, 5, 20)
    #origin = Vector3(0, 0, 0)
    #direction_to_origin = (game_camera.position - origin).normalized()
    #angle = math.atan2(direction_to_origin.y, direction_to_origin.x)
    angle = -15
    game_camera.rotation = Quaternion.AngleAxis(Vector3(1, 0, 0), math.radians(angle) )
    
    game_scene.camera = game_camera
    menu_scene.camera = menu_camera
    Paddle.V_RES = VERTICAL_RESOLUTION
    Paddle.H_RES = HORIZONTAL_RESOLUTION
    Paddle.CAMERA_CORRECTION = -game_camera.position.y + 7 #  at angle of -15
    level_builder = LevelBuilder("Level Builder")
    level_builder.make_level(game_scene)
    game_scene.add_object(level_builder)
        
    menu_scene.add_object(MainMenu("MENU"))
    
    SceneManager.scene_list = []
    SceneManager.scene_list.append(menu_scene)
    SceneManager.scene_list.append(game_scene)
   
    # Set up delta time
    delta_time = 0
    prev_time = time.time()
    
    # Show mouse cursor
    pygame.mouse.set_visible(True)
    # Don't lock the mouse cursor to the game window
    pygame.event.set_grab(False)
   
   
   
    is_running = True
    
    SceneManager.switch_scene(0)
    # Main game loop
    while is_running:

        for event in pygame.event.get():
            # Checks if the user closed the window
            if event.type == pygame.QUIT:
                # Exits the application immediately
                is_running = False
            elif event.type == pygame.KEYDOWN:
                # If ESC is pressed exit the game
                if event.key == pygame.K_ESCAPE:
                    is_running = False
        
        __current_scene = SceneManager.current_scene
        # Update the Display
        window.fill(__current_scene.BACKGROUND_COLOR)
        __current_scene.update_objects(delta_time)
        __current_scene.render(window)
    
        pygame.display.flip()
        
        # Updates delta time, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()
        


__Main()