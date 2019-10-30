# -*- coding:utf-8 -*-

class Decorators():
    def retry(times):
        def outer(f):
            def inner(*args, **kwargs):
                for i in range(times):
                    try:
                        return f(*args, **kwargs)
                    except Exception as e:
                        if (i + 1) < times:
                            print('第{}次执行失败，再次执行'.format(i+1))
                        else:
                            raise e
            return inner
        return outer