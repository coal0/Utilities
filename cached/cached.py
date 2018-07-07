import functools

def cached(name):
    def wrapper(function):
        @functools.wraps(function)
        def call(self, *args, **kwargs):
            if not hasattr(self, name):
                return_value = function(self, *args, **kwargs)
                setattr(self, name, return_value)
            return getattr(self, name)
        return call
    return wrapper


def cached_auto(function):
    @functools.wraps(function)
    def call(self, *args, **kwargs):
        name = "__cached::{}".format(function.__name__)
        if not hasattr(self, name):
            return_value = function(self, *args, **kwargs)
            setattr(self, name, return_value)
        return getattr(self, name)
    return call
