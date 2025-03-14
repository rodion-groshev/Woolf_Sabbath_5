from colorama import init, Fore


class Color:
    def __init__(self):
        init(autoreset=True)
        self.current_color = Fore.LIGHTWHITE_EX

    def set_current_color(self, color):
        self.current_color = color

    def print_text(self, text):
        print(f"{self.current_color}{text}")
