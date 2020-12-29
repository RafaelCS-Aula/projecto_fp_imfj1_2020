import pygame
import time
import math

from scene import Scene
from camera import Camera
from breakout_ball import Ball
from breakout_block import Block
from breakout_paddle import Paddle
from vector3 import Vector3
from color import Color
from quaternion import Quaternion
#from color import Color

HORIZONTAL_RESOLUTION = 1280
VERTICAL_RESOLUTION = 720
#BACKGROUND_COLOR = pygame.Color(255, 0, 0) #red



__current_scene = Scene("empty", pygame.Color(0,255,0))

# Scenes initialisation
game_scene = Scene("GameScene", pygame.Color(0,0,140))
menu_scene = Scene("MainMenu",pygame.Color(255,0,0))

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
    
    
    
    # Calculate camera angle
    game_camera.position -= Vector3(0, 10, 15)
    origin = Vector3(0, 0, 0)
    #direction_to_origin = (game_camera.position - origin).normalized()
    #angle = math.atan2(direction_to_origin.y, direction_to_origin.x)
    angle = -35
    game_camera.rotation = Quaternion.AngleAxis(Vector3(1, 0 , 0), math.radians(angle) )
    
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
    
    ################ Testing objects
    ball_object = Ball(1)
    block_object = Block(start_pos=Vector3(-3, 2, 0))
    paddle_object = Paddle(color=Color(1, 0, 0, 0))
    game_scene.add_object(ball_object)
    game_scene.add_object(block_object)
    game_scene.add_object(Block(start_pos=Vector3(3,4,0)))
    game_scene.add_object(paddle_object)
    
    ################
    
    switch_scene(game_scene)
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
    global __current_scene
    __current_scene = new_scene
    __current_scene.start_scene()

__Main()