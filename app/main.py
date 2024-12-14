import os
import sys
import shlex
from dataclasses import dataclass
import subprocess

PATH = os.environ['PATH']
COMMANDS = ['type', 'pwd', 'echo', 'cd', 'exit']


@dataclass
class Command:
    bin: str
    args: list[str]


def parseInput(text: str) -> Command:
    args = shlex.split(text)
    return Command(bin=args[0], args=args[1:])


def get_executable_path(bin: str) -> str | None:
    for path in PATH.split(os.pathsep):
        fp = os.path.join(path, bin)
        if os.path.exists(fp):
            return fp
    return None


def main():
    sys.stdout.write('$ ')

    while True:
        result = input()

        command = parseInput(result)
        str_args = ' '.join(command.args)

        match command.bin:
            case 'type':
                if str_args in COMMANDS:
                    print(f'{str_args} is a shell builtin')
                elif path := get_executable_path(str_args):
                    print(f'{str_args} is {path}')
                else:
                    print(f'{str_args}: not found')

            case 'exit':
                sys.exit(0)
            case 'echo':
                print(str_args)
            case 'cd':
                if str_args == '~':
                    os.chdir(os.path.expanduser('~'))
                elif os.path.exists(str_args):
                    os.chdir(str_args)
                else:
                    print(f'cd: {str_args}: No such file or directory')
            case 'pwd':
                print(os.getcwd())
            case _:
                try:
                    subprocess.run([command.bin, *command.args])
                except Exception:
                    print(f'{result}: command not found')

        sys.stdout.write('$ ')


if __name__ == '__main__':
    main()
