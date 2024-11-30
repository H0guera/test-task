def strict(func):
    def wrapper(*args, **kwargs):
        expected_types_of_func_params = func.__annotations__
        params = list(expected_types_of_func_params.keys())

        for key, value in zip(params, args):
            if not isinstance(value, expected_types_of_func_params[key]):
                raise TypeError(
                    f"Argument {key!r} must be {expected_types_of_func_params[key]}"
                )

        for key, value in kwargs.items():
            if not isinstance(value, expected_types_of_func_params[key]):
                raise TypeError(
                    f"Argument {key!r} must be {expected_types_of_func_params[key]}"
                )
        return func(*args, **kwargs)

    return wrapper
