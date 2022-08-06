#!/usr/bin/python3
""" The console module """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ The console HBNB class """
    prompt = "(hbnb)"

    __classes = ["basemodel"]

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Used to quit the console - Used by typing - Control + D """
        print()
        return True

    def emptyline(self):
        """ The console shouldn't do anything if nothing is entered """
        pass

    def do_create(self, line):
        """
        Creates a new instance of Model,
        saves it (to the JSON file) and prints the id
        """
        if line:
            if line.lower() in self.__classes:
                if line.lower() == 'basemodel':
                    model = BaseModel()
                    model.save()
                    print(model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


    def do_show(self, line):
        """
         Prints the string representation of an
         instance based on the class name and id
        """
        pass

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        """
        pass

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        pass

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        pass




if __name__ == '__main__':
    HBNBCommand().cmdloop()
