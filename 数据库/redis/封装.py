import redis

class Redis(object):
    def __init__(self, passwd='', host="localhost", post=6379):
        self.__redis = redis.StrictRedis(host=host, post=post, password=passed)

    def set(self, ket, value):
        self.__redis.set(key, value)
    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ''