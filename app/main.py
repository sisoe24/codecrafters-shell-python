import os
import sys
from dataclasses import dataclass
import subprocess

PATH = os.environ['PATH']
COMMANDS = ['type', 'pwd', 'echo', 'cd', 'exit']

@dataclass
class Command:
    bin: str
    args: list[str]


def parseInput(text: str) -> Command:
    parts = text.split(' ')
    return Command(bin=parts[0], args=parts[1:])


def get_executable_path(bin: str) -> str | None:
    for path in PATH.split(os.pathsep):
        fp = os.path.join(path, bin)
        if os.path.exists(fp):
            return fp
    return None

def main():

    sys.stdout.write("$ ")

    while True:
        result = input()

        command = parseInput(result)
        str_args = ' '.join(command.args)

        match command.bin:
            case "type":
                if str_args in COMMANDS:
                    print(f'{str_args} is a shell builtin')
                elif path := get_executable_path(str_args):
                    print(f'{str_args} is {path}')
                else:
                    print(f'{str_args}: not found')

            case "exit":
                sys.exit(0)
            case "echo":
                print(str_args)
            case "pwd":
                print(os.getcwd())
            case _:
                try:
                    subprocess.run([command.bin, *command.args])
                except Exception:
                    print(f'{result}: command not found')

        sys.stdout.write("$ ")


if __name__ == "__main__":
    main()
