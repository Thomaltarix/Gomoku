class Parser:
    def __init__(self, queue):
        self.map_size = 0
        self.queue = queue

    def start_cmd(self, args: list[str]) -> int:
        if len(args) != 1:
            return 1
        try:
            x = int(args[0])
            if x < 0:
                return 1
            self.map_size = x
            print("OK")
            return 0
        except ValueError:
            return 1

    def turn_cmd(self, args: list[str]) -> int:
        if len(args) != 2:
            return 1
        try:
            x, y = map(int, args)
            if 0 <= x < self.map_size and 0 <= y < self.map_size:
                self.queue.put(("enemi", x, y))
                print("us 0 0")
                return 0
            return 1
        except ValueError:
            return 1

    def begin_cmd(self, args: list[str]) -> int:
        if args:
            return 1
        print("us 0 0")
        return 0

    def end_cmd(self, args: list[str]) -> int:
        if args:
            return 1
        print("End")
        return 0

    def error_cmd(self, args: list[str]) -> int:
        if args:
            return 1
        print("ERROR")
        return -1

    def about_cmd(self, args: list[str]) -> int:
        if args:
            return 1
        print('name="brain", version="0.0", author="oui-oui"')
        return 0

    POSSIBLE_COMMANDS = {
        "START": start_cmd,
        "TURN": turn_cmd,
        "BEGIN": begin_cmd,
        "END": end_cmd,
        "ERROR": error_cmd,
        "ABOUT": about_cmd
    }

    def parse(self, message: str) -> int:
        parts = message.split()
        command = parts[0]
        action = self.POSSIBLE_COMMANDS.get(command, self.error_cmd)
        return action(self, parts[1:])

def Communication(queue):
    print("Communication program started")
    parser = Parser(queue)
    while True:
        message = input().strip()
        if parser.parse(message) == -1:
            break
