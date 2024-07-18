from color_coding_tests import run_tests
from color_reference_manual_generator import create_reference_manual


def main():
    # Running tests
    run_tests()

    # Generating and printing the reference manual
    create_reference_manual()


if __name__ == '__main__':
    main()
