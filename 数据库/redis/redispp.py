import redis
#建立连接
r = redis.StrictRedis(host="localhost", port=6379)

#方法1：根据数据不同调用方法
r.set('p1', 'good')
print(r.get('p1'))
#方法二 pipline
#缓冲多条命令，然后依次执行，减少服务器-客户端之阿金的TCP数据报
pipe = r.pipeline()
pipe.set("p2", 'nice')
pipe.set('p3', 'nisdaf')
pipe.set('p4', 'nisdaf')
pipe.set('p5', 'nisdaf')
pipe.set('p6', 'nisdaf')
pipe.set('p7', 'nisdaf')
pipe.set('p3', 'nisdaf')