from pygame.font import match_font

from src.Tools.EnemyScripts.parse_engine import path_follower
from src.Tools.EnemyScripts.parse_engine.tools.conversion_tools import tools
from src.Tools.time_handler import Timer
from src.Tools.EnemyScripts.parse_engine.path_follower import PathFollower

class Token:

    def __init__(self, name, options):
        self.options = options
        if name not in self.options:
            raise Exception(f"Token \"{name}\" does not follow syntax")
        self.name = name

    def get_name(self):
        return self.name


class Operator(Token):
    options = ["END", "WAIT", "IF"]
    def __init__(self, name, args):
        super().__init__(name, self.options)
        self.type = name
        match name:
            case "END":
                self.command = END_Command()
            case "WAIT":
                self.command = WAIT_Command(args)
            case "IF":
                self.command = IF_Command(args)


class END_Command:
    def __init__(self):
        pass

    def update(self):
        print("AT EOF, HANDLE ACCORDINGLY")


class WAIT_Command:
    def __init__(self, args):
        #TODO: Replace with actual minimum rather than arbitrary "1"
        offset = 0


        # Ensures that wait command is valid
        if len(args) < 1:
            raise Exception(f"WAIT operation requires at least one arguments")

        # Increases offset of enemy values to account for time value
        if args[0] == "time":
            self.duration = args[1]
            offset = 1
        else:
            self.duration = args[0]

        # Extracts the enemy values
        self.enemy_values = args[1 + offset]

        #Removes leading and trailing curly braces
        self.path_followers = [self.enemy_values.strip("{}").split(",")]

        self.path_followers = tools.char_array_to_array(self.path_followers[0], '[', ']')


        buff = []
        for i in range(len(self.path_followers)):
            buff.append(PathFollower(self.path_followers, i))
        self.path_followers = buff
        self.duration_arg = Duration_Argument(args[0], self.duration, self.path_followers)



        # print(self.enemy_values)


    def get_path_followers(self):
        return self.path_followers

    # Updates checks duration and updates enemy paths
    def update(self):
        for follower in self.path_followers:
            follower.update()

class Duration_Argument(Token):
    options = ["time", "call", "end"]


    def __init__(self, name, duration, path_followers):
        super().__init__(name, self.options)
        self.path_followers = path_followers
        self.condition_desired = duration
        self.current_state = None
        self.start_time = Timer.get_time_s()


    def condition_met(self):
        match super().get_name():
            case 'end':
                if len(self.path_followers) == 0:
                    return True

                else:
                    return False
            case 'call':
                pass
            case 'time':
                pass

    def update(self):
        if self.name == "time":
            self.current_state = self.condition_desired if Timer.get_time() - self.start_time > int(self.condition_desired) else Timer.get_time() - self.start_time



    def call(self):
        self.current_state = "call"


class IF_Command:
    def __init__(self, *args):
        pass