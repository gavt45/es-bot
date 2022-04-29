class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Test:
        >>> flag = False
        >>> class A(metaclass=Singleton):
        ...     def __init__(self):
        ...         global flag
        ...         assert not flag
        ...         flag = True
        ...
        >>> class B(metaclass=Singleton): pass
        ...
        >>> a = A();b = B();a1 = A();b1 = B()
        >>> id(a) == id(a1) and id(b) == id(b1) and id(a) != id(b)
        True

        :param args:
        :param kwargs:
        :return:
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]