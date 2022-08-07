#!/usr/bin/python3
""" The console module """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ The console HBNB class """
    prompt = "(hbnb)"

    __classes = ["basemodel", "user"]

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
        if line:
            className = None
            instanceId = None
            lines = line.split(" ")
            if len(lines) == 2:
                className = lines[0]
                instanceId = lines[1]
            elif len(lines) == 1:
                className = lines[0]
            if className.lower() in self.__classes:
                if instanceId:
                    objs = storage.all()
                    key = "{}.{}".format(className, instanceId)
                    if key in objs:
                        print(objs[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        """
        if line:
            className = None
            instanceId = None
            lines = line.split(" ")
            if len(lines) == 2:
                className = lines[0]
                instanceId = lines[1]
            elif len(lines) == 1:
                className = lines[0]
            if className.lower() in self.__classes:
                if instanceId:
                    objs = storage.all()
                    key = "{}.{}".format(className, instanceId)
                    if key in objs:
                        del objs[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        objs = storage.all()
        if line:
            if line.lower() in self.__classes:
                class_objs = {}
                for i in objs:
                    if i.startswith(line):
                        class_objs[i] = objs[i]
                for i in class_objs:
                    print(class_objs[i])
            else:
                print("** class doesn't exist **")
        else:
            for i in objs:
                print(objs[i])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
