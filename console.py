#!/usr/bin/python3
""" Console module
"""
import cmd
import sys
import os
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """AirBnB clone console"""
    prompt = '(hbnb)'
    cls_list = ['BaseModel', 'User']

    def preloop(self):
        """Hook method executed once when cmdloop() is called"""
        if not os.isatty(0):
            HBNBCommand.prompt = '(hbnb)\n'

    def emptyline(self):
        """command to execute when an empty line is provided"""
        pass

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        sys.exit()

    def do_create(self, args):
        """Create command to create a new instance, save it and print the id
        """
        if args == "":
            print("** class name missing **")
        else:
            args_list = args.split(' ')
            cls = args.split(' ')[0]
            if cls not in HBNBCommand.cls_list:
                print("** class doesn't exist **")
            else:
                if len(args_list) == 1:
                    if cls == 'BaseModel':
                        model = BaseModel()
                        storage.save()
                        print(model.id)
                    elif cls == 'User':
                        user = User()
                        storage.save()
                        print(user.id)
                else:
                    print(f"*** Unknown syntax: create {args}")

    def do_show(self, args):
        """Show command to print the string representation of an instance
        based on the class name and id
        """
        if args == "":
            print("** class name missing **")
        else:
            args_list = args.split(' ')
            cls = args_list[0]
            if cls not in HBNBCommand.cls_list:
                print("** class doesn't exist **")
            else:
                if len(args_list) == 1:
                    print("** instance id missing **")
                elif len(args_list) > 1:
                    cls_id = args_list[1]
                    cls_key = f"{cls}.{cls_id}"
                    if cls_key not in storage.all().keys():
                        print("** no instance found **")
                    else:
                        if len(args_list) == 2:
                            print(storage.all()[cls_key])
                        elif len(args_list) > 2:
                            print(f"*** Unknown syntax: show {args}")

    def do_destroy(self, args):
        """Destroy command to delete an instance based on the class name and id
        """
        if args == "":
            print("** class name missing **")
        else:
            args_list = args.split(' ')
            cls = args_list[0]
            if cls not in HBNBCommand.cls_list:
                print("** class doesn't exist **")
            else:
                if len(args_list) == 1:
                    print("** instance id missing **")
                elif len(args_list) > 1:
                    cls_id = args_list[1]
                    cls_key = f"{cls}.{cls_id}"
                    if cls_key not in storage.all().keys():
                        print("** no instance found **")
                    else:
                        if len(args_list) == 2:
                            del storage.all()[cls_key]
                            storage.save()
                        elif len(args_list) > 2:
                            print(f"*** Unknown syntax: destroy {args}")

    def do_all(self, args):
        """All command to print all string representation of all instances
        based or not on the class name
        """
        str_list = []
        if args == "":
            for obj in storage.all().values():
                str_list.append(obj.__str__())
            print(str_list)
        else:
            args_list = args.split(' ')
            cls = args_list[0]
            if cls not in HBNBCommand.cls_list:
                print("** class doesn't exist **")
            else:
                if len(args_list) == 1:
                    for key in storage.all().keys():
                        if cls in key:
                            str_list.append(storage.all()[key].__str__())
                    print(str_list)
                else:
                    print(f"*** Unknown syntax: all {args}")

    def do_update(self, args):
        """Update command to update an instance based on the class name
        and id by adding or updating attribute
        """
        if args == "":
            print("** class name missing **")
        else:
            args_list = args.split(' ')
            cls = args_list[0]
            if cls not in HBNBCommand.cls_list:
                print("** class doesn't exist **")
            else:
                if len(args_list) == 1:
                    print("** instance id missing **")
                elif len(args_list) > 1:
                    cls_id = args_list[1]
                    cls_key = f"{cls}.{cls_id}"
                    if cls_key not in storage.all().keys():
                        print("** no instance found **")
                    else:
                        if len(args_list) == 2:
                            print("** attribute name missing **")
                        elif len(args_list) > 2:
                            cls_attr = args_list[2]
                            if len(args_list) == 3:
                                print("** value missing **")
                            elif len(args_list) > 3:
                                cls_attr_value = args_list[3]
                                if len(args_list) == 4:
                                    setattr(storage.all()[cls_key], cls_attr,
                                            cls_attr_value)
                                    storage.save()
                                elif len(args_list) > 4:
                                    print(f"*** Unknown syntax: update {args}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
