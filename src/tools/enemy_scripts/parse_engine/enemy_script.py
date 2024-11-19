import io

from src.base_classes.enemy import beeEnemy
from src.tools.enemy_scripts.parse_engine.tokens import Operator


class enemy_script:

    def __init__(self, file):
        self.file = file
        self.text = self.file.read()
        self.index = 0
        self.current_line = ""

    def get_script(self):
        return self.file

    def read_next_line(self):
        buffer = ""
        x = 0
        if self.current_line[0:3] == "END":
            raise Exception("At end of file!")
        while True:
            buffer += self.text[self.index + x]
            x += 1
            if self.text[self.index + x] == ';':
                break

        self.current_line = buffer.strip()
        self.index += x + 1
        return self.current_line

    def get_operation(self):
        seperated_line = self.current_line.split()

        return Operator(seperated_line[0], seperated_line[1:])
