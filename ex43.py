import sys
# Here we are defining the highest class that defines parts of our game

filename = sys.argv

class Scene(object):

    def enter(self):

        pass

#
class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        Map.opening_scene()
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene():
        print ("""
        'Gothons from Planet Percal #25'\n
        Please enter your player name:\n
        """
        )
        player_name = input("Enter your player's name: ")
        print(f"""\nWelcome {player_name}!\n
        You find yourself isolated on the adrift starship Andromeda.\n
        Aliens from Percal #25, a satellite planet for the alien horde, \n
        has ambushed your unit and you must escape the ship before you are killed.\n
        You have been tasked with deploying a neutron bomb to Andromeda's bridge to destroy it's nuclear core,\n
        in order to prevent capture of the ship's technological capabilities.\n
        Good luck {player_name} and godspeed!\n
        """
        )
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
