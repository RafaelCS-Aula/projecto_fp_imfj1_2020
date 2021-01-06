import pygame
import math
import bo_score_keeper as ScoreKeeper

from bo_text_display import TextDisplay
from breakout_gameobject import GameObject
from mesh import Mesh
from vector3 import Vector3
from material import Material
from color import Color
from quaternion import Quaternion

from bo_collider_sphere import Sphere_Collider


class Ball(GameObject):
    """Game object that bounces around the stage and destroys blocks
    """
    ball_speed = 0
    starting_pos = Vector3(0,0,0)
    DEFAULT_RADIUS = 0.6
    DEFAULT_SPEED = 3
    SPEED_INCREMENT = 0.5
    LOWER_LIMIT = -7
    
    ACTIVATE_BALL_KEY = pygame.K_SPACE
    
    def __init__(self, name, start_pos, radius = DEFAULT_RADIUS, speed = DEFAULT_SPEED,  color = Color(0,1,1,1)):
        self.radius = Vector3(radius, radius, radius)
        self.starting_pos = start_pos
        self.position = start_pos
        self.scale = Vector3(1,1,1)
        self.mesh = Mesh.create_sphere(self.radius, 6, 6)
        self.material = Material(color, "Ball Material")
        #self.rotation = Quaternion.AngleAxis(Vector3(0,0,1), math.radians(180))
        self.rotation = Quaternion.identity()
        self.name = name
        self.children = []
    
        self.ball_speed = speed
        self.direction_vector = Vector3(0,0,0)
        
        self.my_collider = Sphere_Collider(radius *0.3)
        self.handled_collisions = []
        
        self.active = False
        
        self.score_display = TextDisplay((16,300), " -- SCORE -- ")
        self.score_number_display = TextDisplay((16,316), "0 x(combo)", text_size=18, text_color=(100, 200, 100))
        
        self.activation_display = TextDisplay((16,200),  "")
        
        self.combo = 0
    
    def setup(self):
       self.reset_ball()
       self.add_child(self.activation_display)
       self.add_child(self.score_display)
       self.add_child(self.score_number_display)
       self.activation_display.text = "Press [" + pygame.key.name(self.ACTIVATE_BALL_KEY) +"] to activate ball"
       
        

    
    def update_behaviour(self, delta):
        
        # Do nothing but check for input if not active
        if not self.active:
            keys = pygame.key.get_pressed()
            if keys[self.ACTIVATE_BALL_KEY]:
                self.active = True
            return
        
        # Update the score display
        self.score_number_display.text = str(ScoreKeeper.current_score) + " (x" + str(self.combo) + ")"
        
        # Rotate over itself to show ball speed
        self.rotation = Quaternion.AngleAxis(self.up(), 20 * math.radians(delta * self.ball_speed)) * self.rotation
        
        # Keep it aligned with the "ground"
        self.position.z = 0
        
        # Reset the list of unhandled collisions, since we're not even colliding
        if not self.my_collider.is_colliding:
            self.handled_collisions = []

        
        # Move the ball
        self.position += self.ball_speed * self.direction_vector.normalized() * delta
            
        # If ball falls under the screen, reset it
        if self.position.y < self.LOWER_LIMIT:
            print("Ball Reset")
            ScoreKeeper.current_score += ScoreKeeper.SCORE_DEATH_PENALTY
            self.reset_ball()
        
    def handle_collisions(self, collisions: [], delta):
        
        if not self.active:
            return
        
        unhandled_colisions = [c for c in collisions]
      
        for col in unhandled_colisions:
            if col not in self.handled_collisions:

                my_collision_point = self.my_collider.closest_point_on_surface(self.position, col.position)
                other_collision_point = col.my_collider.closest_point_on_surface(col.position, my_collision_point[0])
                
                
                # Check the normal of the colision, assuming AABB colisions
                collision_normal = other_collision_point[1]
                print(str(other_collision_point[0]) + str(other_collision_point[1]))
                
                
                # Reflection formula
                #reflectionDirection = ProjectileDirection - 2(ProjectileDirection DOT wallsNormalVector)*wallsNormalVector
                    
                # Clamped dot product between direction of collision with surface normal
                direction_normal_dot = max(-1, min(1, self.direction_vector.dot(collision_normal)))
                   
                ricochet = self.direction_vector - 2 * direction_normal_dot * collision_normal 
                
                #we've struck the paddle
                if col.name == "PADDLE":
                    self.combo = 0
                    
                    #Direction from center of block to ball
                    col_to_centre = other_collision_point[0] - col.position
                    col_to_centre.normalize()
                    
                    #Bounce using that direction
                    ricochet = col_to_centre
                else:
                    #we've hit a normal Block
                    if col.name == "BLOCK":
                        # Make this block tell the scene it is up to die
                        col.queue_destroy = True
                        
                        # Add to our current score, take into account the combo
                        ScoreKeeper.current_score += ScoreKeeper.SCORE_BLOCK_DESTROY + (ScoreKeeper.SCORE_COMBO_BONUS * self.combo)
                        self.combo += 1
                #
                self.direction_vector = ricochet
                self.ball_speed += self.SPEED_INCREMENT
                
                #Add this collision to the handled bunch so we dont worry about it again
                self.handled_collisions.append(col)
                #print(col.name)"""
       
    def rotate_angle(self, angle):
        """Rotates the ball to a certain angle, parallel to the ground

        Args:
            angle (Vector3): Angle in degrees to snap the rotation to
        """
        self.rotation = Quaternion.AngleAxis(Vector3(0,0,1), angle)
    
    def reset_ball(self):
        self.position = self.starting_pos
        self.active = False
        self.ball_speed = self.DEFAULT_SPEED
        self.direction_vector = Vector3(-self.up().x, -self.up().y, -self.up().z)
        
        
        