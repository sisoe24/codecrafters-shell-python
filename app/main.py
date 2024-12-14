import sys
from dataclasses import dataclass

COMMANDS = ['type', 'pwd', 'echo', 'cd', 'exit']

@dataclass
class Command:
    bin: str
    args: list[str]


def parseInput(text: str) -> Command:
    parts = text.split(' ')
    return Command(bin=parts[0], args=parts[1:])


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
                else:
                    print(f'{str_args}: not found')
            case "exit":
                sys.exit(0)
            case "echo":
                print(str_args)
            case _:
                print(f'{result}: command not found')

        sys.stdout.write("$ ")


if __name__ == "__main__":
    main()
