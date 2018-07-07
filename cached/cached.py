def cached(name):
    def wrapper(function):
        def call(self, *args, **kwargs):
            if not hasattr(self, name):
                return_value = function(self, *args, **kwargs)
                setattr(self, name, return_value)
            return getattr(self, name)
        return call
    return wrapper
