from functools import wraps

def greeter(func):
    @wraps(func)
    def inner():
        data_from_function = func().title()
        result = "Aloha " + data_from_function
        return result
    
    return inner


def sums_of_str_elements_are_equal(func):
    @wraps(func)
    def inner():
        data_from_func = func().split()
        first = 0
        second = 0
        if data_from_func[0][0] == '-':
            for value in data_from_func[0][1:]:
                first -= int(value)
        else:
            for value in data_from_func[0]:
                first += int(value)
        if data_from_func[1][0] == '-':
            for value in data_from_func[1][1:]:
                second -= int(value)
        else:
            for value in data_from_func[1]:
                second += int(value)
        if first == second:
            result = f"{first} == {second}"
        else:
            result = f"{first} != {second}"
        return result
    
    return inner


def format_output(*required_keys):
    def outer_wrapper(f):
        def inner(*args, **kwargs):
            result = f(*args, **kwargs)
            result_dict = {}
            for key in required_keys:
                values = []
                for value in key.split('__'):
                    if value not in result.keys():
                        raise ValueError
                    if result[value] != '':
                        values.append(result[value])
                    else:
                        values.append('Empty value')
                result_dict[key] = ' '.join(values)
            return result_dict

        return inner

    return outer_wrapper


def add_method_to_instance(klass):
    def decorator(f):
        @wraps(f)
        def inner(_, *args, **kwargs):
            return f(*args, **kwargs)
        setattr(klass, inner.__name__, inner)
        return f
    
    return decorator
