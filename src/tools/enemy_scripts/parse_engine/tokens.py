

from src.tools.time_handler import Timer


class Token:

    def __init__(self, name, options):
        self.options = options
        if name not in self.options:
            raise Exception(f"Token \"{name}\" does not follow syntax")
        self.name = name


class Operator(Token):
    options = ["END", "WAIT", "IF"]
    def __init__(self, name, args):
        super().__init__(name, self.options)
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


class WAIT_Command:
    def __init__(self, args):
        #TODO: Replace with actual minimum rather than arbitrary "1"
        if len(args) < 1:
            raise Exception(f"WAIT operation requires at least one arguments")

        if args[0] == "time":
            self.duration = args[1]
        else:
            self.duration = args[0]
        self.duration_arg = Duration_Argument(args[0], self.duration)




class Duration_Argument(Token):
    options = ["time", "call", "condition"]


    def __init__(self, name, duration):
        super().__init__(name, self.options)
        self.condition_desired = duration
        print(duration)
        self.current_state = None
        self.start_time = Timer.get_time()


    def condition_met(self):
        if self.condition_desired == self.current_state:
            print(self.condition_desired, self.current_state)
            return True
        else:
            return False

    def update(self):
        if self.name == "time":
            self.current_state = self.condition_desired if Timer.get_time() - self.start_time > int(self.condition_desired) else Timer.get_time() - self.start_time

    def call(self):
        self.current_state = "call"


class IF_Command:
    def __init__(self, *args):
        pass