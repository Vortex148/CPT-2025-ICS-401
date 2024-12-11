from src.Tools.EnemyScripts.parse_engine.tokens import Operator


class enemy_script:

    def __init__(self, file):
        self.file = file
        self.text = self.file.read()
        self.index = 0
        self.current_line = ""
        self.current_operation = None

    def get_script(self):
        return self.file

    def read_next_line(self):
        buffer = ""
        x = 0
        if self.current_line[0:3] == "END":
            raise Exception("At end of file!")


        if self.current_operation is not None and not self.current_operation.command.duration_arg.condition_met():
            return
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
        if self.current_operation is None:
            self.current_operation = Operator(seperated_line[0], seperated_line[1:])

        if self.current_operation.command.duration_arg.condition_met():
            self.current_operation = Operator(seperated_line[0], seperated_line[1:])

        return self.current_operation

    def check_collision(self, rect):
        for i in range(len(self.current_operation.command.path_followers)):
            if self.current_operation.command.path_followers[i].follower.check_collision(rect):
                print("COLLISION")
                del self.current_operation.command.path_followers[i]
                break

    def update(self):
        self.read_next_line()
        self.get_operation()
        self.current_operation.command.update()
