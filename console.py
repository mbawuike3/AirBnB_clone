#!/usr/bin/python3
""" The console module """
import cmd


class HBNBCommand(cmd.Cmd):
    """ The console HBNB class """

    intro = "Welcome to the HBNB console type help " \
            "to list available commands\n"
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Used to quit the console - Used by typing - Control + D """
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
