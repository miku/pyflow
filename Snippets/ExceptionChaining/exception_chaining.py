
def run():
    raise RuntimeError('run failed')


def setup():
    try:
        run()
    except RuntimeError as exc:
        print()
        print(exc)
        print("setup", exc.__cause__)
        print("setup", exc.__context__)
        print("setup", exc.__traceback__)
        raise IOError('setup failed')
        # None
        # None
        # <traceback object at 0x7fc26247a380>

def setup_raise_from():
    try:
        run()
    except RuntimeError as exc:
        print()
        print(exc)
        print("setup_from_raise", exc.__cause__)
        print("setup_from_raise", exc.__context__)
        print("setup_from_raise", exc.__traceback__)
        raise IOError('setup_from_raise failed') from exc
    
def main():
    try:
        setup()
    except (RuntimeError, IOError) as exc:
        print()
        print("setup threw: {}".format(exc))
        print("main", exc.__cause__)
        print("main", exc.__context__)
        print("main", exc.__traceback__)

    try:
        setup_raise_from()
    except (RuntimeError, IOError) as exc:
        print()
        print("setup_from_raise threw: {}".format(exc))
        print("main", exc.__cause__)
        print("main", exc.__context__)
        print("main", exc.__traceback__)

if __name__ == '__main__':
    main()