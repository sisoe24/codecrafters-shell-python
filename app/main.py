import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    result = input()
    print(f'{result}: command not found')


if __name__ == "__main__":
    main()
