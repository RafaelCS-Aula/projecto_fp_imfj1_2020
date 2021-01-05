"""Scene class definition"""
from camera import Camera
import pygame

class Scene:
    """Scene class.
    It handles a scene, storing a list of objects and a camera/viewpoint"""
    def __init__(self, name, bg_color = pygame.Color(0,0,0)):
        """
        Arguments:

            name {str} -- Name of the material, defaults to 'UnknownMesh'
            bg_color {Color} -- default color of background
        """
        self.name = name
        """ {str} Name of the scene"""
        self.camera = Camera(True, 640, 480)
        """ {Camera} Camera linked to this scene"""
        self.objects = []
        """ {List[GameObject]} List of 3d objects on the scene"""
        self.BACKGROUND_COLOR = bg_color

        self.collision_agents = []

    def add_object(self, obj):
        """Adds a 3d object to the scene.

        Arguments:

            obj {GameObject} -- 3d object to add to the scene
        """
        if obj not in self.objects:
            self.objects.append(obj)

    def remove_object(self, obj):
        """Removes a 3d object from the scene. This function does not scan the child objects,
        so it's only used to remove objects at the root level. If the object is not at the root
        level of the scene, nothing happens

        Arguments:

            obj {GameObject} -- 3d object to remove from the scene
        """
        if obj in self.objects:
            self.objects.remove(obj)

    def render(self, screen):
        """Renders this scene on the given target

        Arguments:

            screen {pygame.Surface} -- Pygame surface where the scene should be drawn
        """
        # Create clip matrix to be passed to the root-level objects, so they can be drawn
        camera_matrix = self.camera.get_camera_matrix()
        projection_matrix = self.camera.get_projection_matrix()

        clip_matrix = camera_matrix * projection_matrix

        # Render all root-level objects
        for obj in self.objects:
            obj.render(screen, clip_matrix)
        #for obj in range(len(self.objects)):
        #    self.objects[obj].render(screen, clip_matrix)
        #    for child in self.objects[obj].children:
        #        child.render(screen, clip_matrix)
            
    def start_scene(self):
        """Executes the setup method for all game objects of the scene and gathers collision agents
        """
        self.collision_agents = []
        
        for obj in range(len(self.objects)):
            self.objects[obj].setup()
            if(self.objects[obj].my_collider is not None):
                self.collision_agents.append(self.objects[obj])
            for child in self.objects[obj].children:
                child.setup()
                if(child.my_collider is not None):
                    self.collision_agents.append(child)
                #print("Child setup")
        print("COLLIDERS: ")
        print(len(self.collision_agents))
            
    def update_objects(self, delta):
        """Updates all the objects' states

        Args:
            delta ([float]): Time passed since last frame
        """
        objects_destroy = []
        for obj in range(len(self.objects)):
            
            self.objects[obj].update_behaviour(delta)
            if self.objects[obj].queue_destroy:
                objects_destroy.append(self.objects[obj])
            
            for child in self.objects[obj].children:
                if child.queue_destroy:
                    self.remove_object(child)
                else:
                    child.update_behaviour(delta)
        
        for o in objects_destroy:
            self.remove_object(o)
            if o in self.collision_agents:
                self.collision_agents.remove(o)
                
        # Detect Collisions
        # For every agent go trough every other agent on the collection
        for current in range(len(self.collision_agents)):
            collisions = []
            agent = self.collision_agents[current]
            for other in range(len(self.collision_agents)):
                # Compare every collider against every other one
                if other == current:
                    continue
                foreign = self.collision_agents[other]
                
                # Check if agent is colliding with foreign by checking if the
                # closest point to agent on foregisn surface is within bounds
                # of agent's collider
                if(agent.my_collider.within_bounds(agent.position, foreign.my_collider.closest_point_on_surface(foreign.position, agent.position)[0])):
                    
                    collisions.append(foreign)
            agent.handle_collisions(collisions, delta)
            
    def get_objects_by_name(self, name):
        listing = []
        for obj in self.objects:
            if obj.name == name:
                listing.append(obj)
        return listing