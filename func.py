from multiprocessing import Pool, cpu_count
import time

def factorize_number(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def factorize_sync(*numbers):
    result = []
    for num in numbers:
        result.append(factorize_number(num))
    return result

def factorize_parallel(*numbers):
    num_cores = cpu_count()
    with Pool(num_cores) as pool:
        result = pool.map(factorize_number, numbers)
    return result

# # Testing the synchronous version
# start_time = time.time()
# a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
# end_time = time.time()
# print("Synchronous version time:", end_time - start_time, "seconds")

# Testing the parallel version
start_time = time.time()
a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
end_time = time.time()
print("Parallel version time:", end_time - start_time, "seconds")