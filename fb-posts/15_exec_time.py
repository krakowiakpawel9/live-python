import time


start = time.time()
tmp = [i ** i for i in range(10000)]
execution_time = time.time() - start
print(f'execution time: {execution_time:.10f}')
