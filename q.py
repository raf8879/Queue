
class Queue:
    def __init__(self, *args):
        self.args = [str(i) for i in args]

    def __repr__(self):
        return f"{' -> '.join(self.args)}"

    def add(self, *other):
        self.args.extend(map(str, other))

    def pop(self):
        if self.args:
            return self.args.pop(0)
        return None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.args == other.args
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.args != other.args
        return True

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(*self.args, *other.args)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.add(*other.args)
            return self
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            return self.__class__(*self.args[other:])
        return NotImplemented
