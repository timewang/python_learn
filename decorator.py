import functools

def log(func):
    def wrapper():
        print('begin call')
        func()
        print('end call')
    return  wrapper


def log(text):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin call %s %s' %(text, func.__name__))
                func(*args, **kw)
                print('end call %s %s' % (text, func.__name__))
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('begin call %s' % text.__name__)
            text(*args, **kw)
            print('end call %s' % text.__name__)
        return wrapper

@log('let`s go')
def gogogogogo():
    print('2017-02-13')

@log
def now():
    print('2017-2-14')
now()

gogogogogo()