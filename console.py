#!/usr/bin/python3
""" Console module
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """AirBnB clone console"""
    prompt = '(hbnb)'

    def emptyline(self):
        """command to execute when an empty line is provided"""
        pass

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        sys.exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
