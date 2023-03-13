from Tests.testAll import run_all_tests
from UI.commandLine import run_command_line
from UI.console import run_meniu


def print_choose_UI():
    print("1. Console")
    print("2. Command line (functionalitati limitate)")
    print("x. Exit")


def main():
    run_all_tests()
    while True:
        print_choose_UI()
        choose_UI = input("Alegeti optiunea: ")
        if choose_UI == "1":
            run_meniu([])
        elif choose_UI == "2":
            run_command_line([])
        elif choose_UI == "x":
            break
        else:
            print("Optiune invalida!")


if __name__ == "__main__":
    main()
