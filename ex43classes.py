class Scene(object):

    def __enter__(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def __enter__(self):
        pass

class CentralCorridor(Scene):

    def __enter__(self):
        pass

class LaserWeaponArmory(Scene):

    def __enter__(self):
        pass

class TheBridge(Scene):

    def __enter__(self):
        pass

class EscapePod(Scene):

    def __enter__(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_sente(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()