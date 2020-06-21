import sys

from .filter import SporFilter


def main(argv=None):
    """Run spor filter with specified command line args.

    Args:
        argv: Command-line arguments to use.
    """
    return SporFilter().main(argv)


if __name__ == '__main__':
    sys.exit(main())
