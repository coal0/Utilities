from cached import cached


class Double:
    def __init__(self, x):
        self._x = x
    
    @cached("_double_x")
    def value(self):
        return self._x * 2
