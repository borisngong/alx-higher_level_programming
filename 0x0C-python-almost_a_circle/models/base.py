#!/usr/bin/python3
"""Module that defines a class base model"""
import json
import csv


class Base:
    """Base class with private class attribute __nb_objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): represents list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        to_json = json.dumps(list_dictionaries)

        return to_json

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Responsible for writing the JSON string representation of
        list_objs to a file
        Args: list_objs:
            list of instances who inherits of Base
        """
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                jsonfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Responsible for returning an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        Responsible for returning a list of instances
        """
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                list_instances = []

                for k in list_dicts:
                    list_instances.append(cls.create(**k))
                return list_instances
        except FileNotFoundError:
            return []

    def save_to_file_csv(cls, list_objs):
        """CSV serialization of object lists to a file"""
        file_name = {}.json.format(cls.__name__)
        with open(file_name, "w") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    name_of_fields = ["id", "width", "height", "x", "y"]
                else:
                    name_of_fields = ["id", "size", "x", "y"]
                    writer = csv.DictWriter(
                        csvfile,
                        fieldnames=name_of_fields
                    )
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    def load_from_file_csv(cls):
        """
        Responsible for returning list of objects instantiated from csv file
        """
        file_name = {}.json.format(cls.__name__)
        try:
            with open(file_name, "r") as csvfile:
                if cls.__name__ == "Rectangle":
                    name_of_fields = ["id", "width", "height", "x", "y"]
                else:
                    name_of_fields = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(
                    csvfile, 
                    fieldnames=name_of_fields)
                new_dict_list = []
                dict_conversion = {}
                for k in dict_list:
                    for key, value in k.items():
                        dict_conversion[key] = int(value)
                    new_dict_list.append(dict_conversion)
                dict_list = new_dict_list
                instance_list = []
                for k in dict_list:
                    instance_list.append(cls.create(**k))
                return instance_list
        except FileNotFoundError:
            return []



