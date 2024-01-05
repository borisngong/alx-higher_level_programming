#!/usr/bin/python3


class LockedClass:
    allowed_attributes = ["first_name"]

    def __setattr__(self, name, value):
        if name not in self.allowed_attributes:
             error_message = "'LockedClass' object has no attribute '{}'"
             raise AttributeError(error_message.format(name))
        super().__setattr__(name, value)
