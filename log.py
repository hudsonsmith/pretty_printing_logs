class Log(object):
    def __init__(self) -> None:
        self.reset: str = "\033[0m"
        self.bold: str = "\033[1m"
        self.italic: str = "\033[3m"
        self.underline: str = "\033[4m"
        self.blinking: str = "\033[5m"
        self.reverse: str = "\033[7m"
        self.black: str = "\033[30m"
        self.red: str = "\033[31m"
        self.green: str = "\033[32m"
        self.brown: str = "\033[33m"
        self.blue: str = "\033[34m"
        self.purple: str = "\033[35m"
        self.cyan: str = "\033[36m"
        self.grey: str = "\033[37m"
        self.yellow: str = "\033[1;33m"
    
    def fail(self, string: str) -> None:
        print(f"{self.red}{self.bold}[x]{self.reset} {self.red}{self.italic}{string}{self.reset}")

    def info(self, string: str) -> None:
        print(f"{self.blue}{self.bold}[i]{self.reset} {self.blue}{self.italic}{string}{self.reset}")
    
    def warn(self, string: str) -> None:
        print(f"{self.yellow}{self.bold}[!]{self.reset} {self.yellow}{self.italic}{string}{self.reset}")

    def succeed(self, string: str) -> None:
        print(f"{self.green}{self.bold}[*]{self.reset} {self.green}{self.italic}{string}{self.reset}")
