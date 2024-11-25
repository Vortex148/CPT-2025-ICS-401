from src.Tools.EnemyScripts.parse_engine.conversion_tools import tools

class PathFollower:
    def __init__(self, args: str, index):
        self.args = args.strip("{}").split(",")
        print(tools.char_array_to_enemy_data(self.args, index).type)

