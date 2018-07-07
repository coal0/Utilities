from cached import cached


class Double:
    def __init__(self, x, counter):
        self._x = x
        self._counter = counter
    
    @cached("_double_x")
    def value(self):
        self._counter += 1
        return self._x * 2

if __name__ == "__main__":
    c = 0
    d = Double(6, c)
    
    val1 = d.value()
    assert val1 == 12
    assert c == 1
    
    val2 = d.value()
    assert val2 == 12
    assert c == 1
