import time

import eventlet;eventlet.monkey_patch(all=True)
from funboost import boost, ConcurrentModeEnum
from funboost.concurrent_pool.custom_evenlet_pool_executor import CustomEventletPoolExecutor

"""
这个是演示多个不同的函数消费者，使用同一个全局的并发池。
如果一次性启动的函数过多，使用这种方式避免每个消费者创建各自的并发池，减少线程/协程资源浪费。
"""

# 总共那个有5种并发池，用户随便选。
pool = CustomEventletPoolExecutor(2)  # 指定多个消费者使用同一个线程池，


@boost('test_f1_queue', specify_concurrent_pool=pool, qps=3, concurrent_mode=ConcurrentModeEnum.EVENTLET)
def f1(x):
    print('============================')
    time.sleep(0.5)
    print(f'x : {x}')
    print('============================')


if __name__ == '__main__':
    f1.clear()
    for i in range(10):
        f1.push(i)
    f1.consume()