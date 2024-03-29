#!/usr/bin/python3
"""Module for working with the base class"""
import json
import csv


class Base:
    """Base Class with private class attribute __nb_objects"""

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Class constructor: Initializes id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
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
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or not json_string:
            return []
        else:
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to a CSV file"""
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, "w", newline="") as csv_file:
            if list_objs is None or not list_objs:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=field_names)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from a CSV file"""
        file_name = "{}.csv".format(cls.__name__)
        try:
            with open(file_name, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                list_dict = csv.DictReader(csv_file, fieldnames=field_names)
                next(list_dict)

                list_of_instances = []
                for row in list_dict:
                    converted_dict = {}
                    for key, value in row.items():
                        converted_dict[key] = int(value)
                    list_of_instances.append(cls.create(**converted_dict))
                return list_of_instances
        except FileNotFoundError:
            return []
