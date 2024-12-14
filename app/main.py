import sys


def main():

    sys.stdout.write("$ ")

    while True:
        result = input()
        print(f'{result}: command not found')
        sys.stdout.write("$ ")


if __name__ == "__main__":
    main()
