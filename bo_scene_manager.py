"""Holds list of scenes and handles scene switching on command

"""

scene_list = []

current_scene = None


def switch_scene(index):
    global current_scene
    current_scene = scene_list[index]
    current_scene.start_scene()
    return current_scene
