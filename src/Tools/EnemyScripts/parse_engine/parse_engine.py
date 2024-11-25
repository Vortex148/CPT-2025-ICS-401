from src.Tools.EnemyScripts.parse_engine.enemy_script import enemy_script


class engine:

    @staticmethod
    def read_script(path):
        if path[len(path) - 8: len(path)] != ".emscrpt":
            raise Exception("Invalid extension")
        file = open(path, 'r')

        return enemy_script(file)