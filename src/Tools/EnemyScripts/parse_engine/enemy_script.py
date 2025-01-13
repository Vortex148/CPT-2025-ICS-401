from src.Tools.EnemyScripts.parse_engine.tokens import Operator, IF_Command, END_Command



class enemy_script:

    def __init__(self, file):
        self.file = file
        self.text = self.file.read()
        self.index = 0
        self.current_line = ""
        self.current_operation = None

    def get_script(self):
        return self.file

    def get_projectile_sprite_group(self):
        projectile_groups = []

        if self.current_operation.command != END_Command:
            for i in self.current_operation.command.path_followers:
                projectile_groups.append(i.get_projectile_group())
            return projectile_groups
        return False

    def get_operation(self):
        seperated_line = self.current_line.split()
        if self.current_operation is None:
            self.current_operation = Operator(seperated_line[0], seperated_line[1:])

        if self.current_operation.command.duration_arg.condition_met():
            self.current_operation = Operator(seperated_line[0], seperated_line[1:])

        return self.current_operation

    def update(self):
        done = self.read_next_line()
        if not done:
            self.get_operation()
            self.current_operation.command.update()
        return done

    def read_next_line(self):
        buffer = ""
        x = 0
        if self.current_line[0:3] == "END":
            return True

        if self.current_operation is not None and not self.current_operation.command.duration_arg.condition_met():
            return False

        while True:
            buffer += self.text[self.index + x]
            x += 1
            if self.text[self.index + x] == ';':
                break

        self.current_line = buffer.strip()
        self.index += x + 1
        return False

    def check_collision(self, rect):
        for i in range(len(self.current_operation.command.path_followers)):
            if self.current_operation.command.path_followers[i].follower.check_collision(rect):
                del self.current_operation.command.path_followers[i]
                break
