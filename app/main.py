import sys


def main():

    sys.stdout.write("$ ")

    while True:
        result = input()

        match result:
            case "exit 0":
                sys.exit(0)
            case _:
                print(f'{result}: command not found')

        sys.stdout.write("$ ")


if __name__ == "__main__":
    main()
