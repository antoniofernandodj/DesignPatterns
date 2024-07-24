import random


def singleton(func):
    instances = {}
    print(instances)

    def get_instance(*args, **kwargs):
        if func not in instances:
            instances[func] = func(*args, **kwargs)
        return instances[func]

    return get_instance


@singleton
def get_config():
    return {
        "host": "localhost",
        "port": random.randint(10, 100)
    }


config1 = get_config()
print('config1:', config1)

config2 = get_config()
print('config2:', config2)

config2['host'] = '127.0.0.1'

config3 = get_config()
print('config3:', config3)

config4 = get_config()
print('config4:', config4)
