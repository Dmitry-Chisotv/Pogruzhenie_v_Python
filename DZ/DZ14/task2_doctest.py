from task2 import replace_variables


def del_symbols(name: str) -> str:
    """
    >>> del_symbols('cycles')
    cycle
    >>> del_symbols('s')
    s
    >>> del_symbols('hello world')
    hello world
    >>> del_symbols('say')
    say
    """

    new_text = replace_variables(name)

    # if name.endswith('s') and len(name) > 1:
    #     new_name = name[:-1]
    #     print(new_name)
    # elif name.endswith('s') and len(name) == 1:
    #     print(name)
    # else:
    #     print(name)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)