#!/usr/bin/python3
"""
Console for AirBnB clone
"""
import cmd
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.review import Review
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand processor
    """
    prompt = '(hbnb) '

    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def do_EOF(self, line):
        """
        Method to exit with EOF command
        """
        return True

    def do_quit(self, line):
        """
        Method to exit with quit command
        """
        return True

    def emptyline(self):
        """
        Nothing happened if empty line passed (ENTER pressed)
        """
        pass

    def check_class(cls):
        """
        Method helper to identify cls is valid
        """
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        for key, value in classes.items():
            if cls == key:
                return value
            else:
                return None

    def do_create(self, line):
        """
        Method creates new instance of obj
        """
        if not line:
            print("** class name missing **")
        elif line in self.classes:
            instance = eval(line)()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")
            """        else:
            args = line.split()
            if args[0] is None:
                print("** class name missing **")
            else:
                valid_cls = check_class(args[0])
                if valid_cls is not None:
                    instance = valid_class()
                    instance.save()
                    print(instance.id)
                else:
                    print("** class doesn't exist **") """

    def do_show(self, line):
        """
        Method show str rep of instance using cls name and id
        """

        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            if args[0] is not None:
                obj = storage.all()
                key = str(args[0]) + '.' + str(args[1])
                try:
                    print(obj[key])
                except:
                    print("** no instance found **")

        """else:
            args = line.split()
            if not args[0]:
                print("** class name missing **")
            try:
                args[1]
            except Exception:
                print("** instance id missing **")
            else:
                valid_class = check_class(args[0])
                if valid_class is not None:
                    obj = storage.all()
                    key = str(args[0]) + '.' + str(args[1])
                    try:
                        print(obj[key])
                    except:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")"""

    def do_destroy(self, line):
        """
        Method destroys an instance
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            if args[0] is not None:
                obj = storage.all()
                #key = str(args[0]) + '.' str(args[1])
                try:
                    del obj[key]
                    storage.save()
                except:
                    print("** no instance found **")
        """else:
            if not args[0]:
                print("** class name missing **")
            try:
                args[1]
            except:
                print("** instance id missing **")
            else:
                valid_class = check_class(args[0])
                if valid_class is not None:
                    obj = storage.all()
                    print("-----{}".format(args[0]))
                    print("-----{}".format(args[1]))
                    #key = str(args[0]) + '.' str(args[1])
                    try:
                        del obj[key]
                        storage.save()
                    except:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")"""

    def do_all(self, line):
        """
        Method print str rep based on class name or not
        """
        args = line.split()
        obj = storage.all()
        list = []
        if line == "" or line in self.classes:
            for key, value in (obj.items()):
                list.append(value)
            print(list)
        else:
            print("** class doesn't exist **")
        """counter = 0
        try:
            args[0]
            valid_class = check_class(args[0])
            if valid_class is None:
                print("** class doesn't exist **")
            for key in obj.keys():
                obj_class = (obj[k].__class__.__name__)
                if obj_class == args[0]:
                    print(obj[k])
                    counter += 1
            if counter == 0 and valid_class is not None:
                print([])
        except:
            for key in obj.keys():
                print(obj[key])
                counter += 1
            if counter == 0:
                print([])"""

    def do_update(self, line):
        """
        Method update values based on instance
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if not args[0]:
                print("** class name missing **")
            try:
                args[1]
            except:
                print("** instance id missing **")
            try:
                args[2]
            except:
                print("** attribute name missing **")
            try:
                args[3]
            except:
                print("** value missing **")
            else:
                valid_class = check_class(args[0])
                if valid_class is not None:
                    obj = storage.all()
                    key = str(args[0]) + '.' + str(args[1])
                    try:
                        if args[3].isdigit():
                            args[3] = int(args[3])
                        else:
                            args[3] = args[3].replace('"', '')
                        setattr(obj[key], args[2], args[3])
                        setattr(obj[key], "updated_at", datetime.now())
                        storage.save()
                    except:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def create_updatestr(line):
        """
        Method create string for update method using class name
        """
        args = line.split()
        args0 = args[0].replace('"', "")
        tmp = args0.replace(',', "")
        attribute = args[1].replace('"', "")
        attribute = attribute.replace(',', "")
        value = args[2].replace('"', "")
        value = value.replace(',', "")
        returnvalue = tmp + " " + attribute + " " + value
        return returnvalue

    def do_BaseModel(self, line):
        """
        Method handling BaseModel
        """
        if line == '.all()':
            self.do_all("BaseModel")
        elif line == '.count()':
            print(self.get_instanceCount("BaseModel"))
        elif line[0:5] == '.show':
            argument = 'BaseModel' + " " + line[7:-2]
            self.do_show(argument)
        elif line[0:8] == '.destroy':
            argument = "BaseModel" + " " + line[10:-2]
            self.do_destroy(argument)
        elif line[0:7] == '.update':
            rtrn = build_updatearg(line[8:-1])
            argument = "BaseModel" + " " + rtrn
            self.do_update(argument)

    def do_User(self, line):
        """
        Method handling User
        """
        if line == '.all()':
            self.do_all("User")
        elif line == '.count()':
            print(self.get_instanceCount("User"))
        elif line[0:5] == '.show':
            argument = 'User' + " " + line[7:-2]
            self.do_show(argument)
        elif line[0:8] == '.destroy':
            argument = "User" + " " + line[10:-2]
            self.do_destroy(argument)
        elif line[0:7] == '.update':
            rtrn = build_updatearg(line[8:-1])
            argument = "User" + " " + rtrn
            self.do_update(argument)

    def do_City(self, line):
        """
        Method handling City
        """
        if line == '.all()':
            self.do_all("City")
        elif line == '.count()':
            print(self.get_instanceCount("City"))
        elif line[0:5] == '.show':
            argument = 'City' + " " + line[7:-2]
            self.do_show(argument)
        elif line[0:8] == '.destroy':
            argument = "City" + " " + line[10:-2]
            self.do_destroy(argument)
        elif line[0:7] == '.update':
            rtrn = build_updatearg(line[8:-1])
            argument = "City" + " " + rtrn
            self.do_update(argument)

    def do_State(self, line):
        """
        Method handling State
        """
        if line == '.all()':
            self.do_all("State")
        elif line == '.count()':
            print(self.get_instanceCount("State"))
        elif line[0:5] == '.show':
            argument = 'State' + " " + line[7:-2]
            self.do_show(argument)
        elif line[0:8] == '.destroy':
            argument = "State" + " " + line[10:-2]
            self.do_destroy(argument)
        elif line[0:7] == '.update':
            rtrn = build_updatearg(line[8:-1])
            argument = "State" + " " + rtrn
            self.do_update(argument)

    def do_Place(self, line):
        """
        Method handling Place
        """
        if line == '.all()':
            self.do_all("Place")
        elif line == '.count()':
            print(self.get_instanceCount("Place"))
        elif line[0:5] == '.show':
            argument = 'Place' + " " + line[7:-2]
            self.do_show(argument)
        elif line[0:8] == '.destroy':
            argument = "Place" + " " + line[10:-2]
            self.do_destroy(argument)
        elif line[0:7] == '.update':
            rtrn = build_updatearg(line[8:-1])
            argument = "Place" + " " + rtrn
            self.do_update(argument)

    def do_Amenity(self, line):
        """
        Method handling Amenity
        """
        if line == '.all()':
            self.do_all("Amenity")
        elif line == '.count()':
            print(self.get_instanceCount("Amenity"))
        elif line[0:5] == '.show':
            argument = 'Amenity' + " " + line[7:-2]
            self.do_show(argument)
        elif line[0:8] == '.destroy':
            argument = "Amenity" + " " + line[10:-2]
            self.do_destroy(argument)
        elif line[0:7] == '.update':
            rtrn = build_updatearg(line[8:-1])
            argument = "Amenity" + " " + rtrn
            self.do_update(argument)

    def do_Review(self, line):
        """
        Method handling Reviews
        """
        if line == '.all()':
            self.do_all("Review")
        elif line == '.count()':
            print(self.get_instanceCount("Review"))
        elif line[0:5] == '.show':
            argument = 'Review' + " " + line[7:-2]
            self.do_show(argument)
        elif line[0:8] == '.destroy':
            argument = "Review" + " " + line[10:-2]
            self.do_destroy(argument)
        elif line[0:7] == '.update':
            rtrn = build_updatearg(line[8:-1])
            argument = "Review" + " " + rtrn
            self.do_update(argument)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
