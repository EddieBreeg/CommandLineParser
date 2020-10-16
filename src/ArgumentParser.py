from re import sub
from sys import argv

class InvalidArgumentException(Exception):
    def __init__(self, message):
        self.message = message
class MissingArgumentException(Exception):
    def __init__(self, message):
        self.message = message
class IllegalValueException(Exception):
    def __init__(self, message):
        self.message = message
class Argument:
    def __init__(self, name, valueType:type, default, choices):
        self.name = name
        self.valueType = valueType
        self.default = default
        self.choices = choices
class ArgumentParser:
    def __init__(self):
        self.args = []
    def addArgument(self, name, valueType, default=None, choices = None):
        self.args.append(Argument(name, valueType, default, choices))

    def parseArguments(self):
        pattern = r"-{1,2}"
        class Arguments:
            pass

        result = Arguments()
        for arg in self.args:
            name = sub(pattern, lambda m: "", arg.name)
            if arg.name in argv:
                i = argv.index(arg.name)
                
                try:
                    value = arg.valueType(argv[i+1])
                except IndexError:
                    raise MissingArgumentException("Missing required argument: {0}"
                        .format(arg.name))
                except ValueError:
                    raise IllegalValueException("Argument {0}: expected value of type {1}"
                        .format(arg.name, arg.valueType))
                if (arg.choices is not None and value not in arg.choices):
                    raise IllegalValueException("{0} is not a valid value for argument {1}"
                        .format(value, arg.name))

                result.__setattr__(name, value)
            elif arg.default is not None:
                result.__setattr__(name, arg.default)
            else:
                raise MissingArgumentException("Missing required argument: {0}"
                    .format(arg.name))
        return result