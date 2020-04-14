from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("The scene is not yet configured.")
        print("Subclass it and implement enter().")
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        pass

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
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