#!/usr/bin/env python3

class Prepend(object):
    """Prints each line passed to write() with a fixed prefix.

    Prepend(prefix) stores the prefix. Each call to write(text) should
    print prefix + text to stdout, e.g.:

        p = Prepend("+++ ")
        p.write("Hello")    # prints "+++ Hello"
        p.write("Goodbye")  # prints "+++ Goodbye"
    """
    # TODO: implement __init__(self, prefix) and write(self, text)


def main():
    p = Prepend("+++ ")
    p.write("Hello")
    p.write("Goodbye")


if __name__ == "__main__":
    main()
