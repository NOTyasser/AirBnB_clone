#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
import cmd
import sys
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

import shlex


class HBNBCommand(cmd.Cmd):
    """Class definition HBNBCommand which inherits from cmd.Cmd"""
    prompt = "(hbnb)"
    classes_map = ["BaseModel", "User", "Amenity",
                   "City", "Place", "Review", "State"]

    def do_quit(self, arg):
        """Exit the program with the Quit command"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print()
        return True

    def emptyline(self):
        """To do nothing when an empty line is the entry."""
        pass

    def do_create(self, arg):
        """Create method that creats an object"""
        if arg:
            if hasattr(sys.modules[__name__], arg):
                cls = getattr(sys.modules[__name__], arg)
                instance = cls()
                models.storage.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in self.classes_map:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = class_name + "." + instance_id
            objects = models.storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy method that destroys an object."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in self.classes_map:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = class_name + "." + instance_id
            objects = models.storage.all()
            if key in objects:
                del objects[key]
                models.storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    # ... (Previous code remains unchanged)
    def do_all(self, arg):
        objects = models.storage.all()
            args = arg.split()
        if not args:
            for val in objects.values():
                print(f"{str(val)}", end="")
            print()
        else:
            class_name = args[0]
            if class_name not in self.classes_map:
                print("** class doesn't exist **")
            else:
                class_objects = [str(obj) for obj in objects.values() if type(obj).__name__ == class_name]
                print("\n".join(class_objects))
    def do_count(self, arg):
        class_name = arg.split('.')[0]
        count = sum(1 for obj in models.storage.all().values() if type(obj).__name__ == class_name)
        print(count)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in self.classes_map:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = class_name + "." + instance_id
            objects = models.storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in self.classes_map:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = class_name + "." + instance_id
            objects = models.storage.all()
            if key in objects:
                del objects[key]
                models.storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes_map:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in objects.keys():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                instance = objects[key]
                attribute_type = type(getattr(instance, args[2], ''))
                setattr(instance, args[2], attribute_type(args[3]))
                instance.save()

    def do_update_dict(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes_map:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in objects.keys():
                print("** no instance found **")
            elif len(args) == 2:
                print("** dictionary missing **")
            else:
                instance = objects[key]
                try:
                    dictionary = eval(args[2])
                    if type(dictionary) is dict:
                        for k, v in dictionary.items():
                            attribute_type = type(getattr(instance, k, ''))
                            setattr(instance, k, attribute_type(v))
                        instance.save()
                    else:
                        print("** not a dictionary **")
                except:
                    print("** invalid dictionary **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
