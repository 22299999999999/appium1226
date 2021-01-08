def black_wrapper(fun):
    def run(*args, **kwargs):
        first = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            for black in first.black_list:
                elements = first.finds(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return fun(*args, **kwargs)
        raise e

    return run
