import time
import threading
import multiprocessing
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool


ARTIFACTS_PATH = Path(__file__).resolve().parents[1] / 'artifacts' / '4.1'


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        return result, execution_time
    return wrapper

@measure_time
def run_fibonacci_sync(n):
    return fibonacci(n)

@measure_time
def run_fibonacci_threading(n):
    with ThreadPoolExecutor(max_workers=10) as executor:
        return list(executor.map(fibonacci, [n]*10))

@measure_time
def run_fibonacci_multiprocessing(n):
    with Pool(processes=10) as pool:
        return pool.map(fibonacci, [n]*10)

if __name__ == "__main__":
    n = 30

    sync_results = run_fibonacci_sync(n)
    threading_results = run_fibonacci_threading(n)
    multiprocessing_results = run_fibonacci_multiprocessing(n)

    with open(f"{ARTIFACTS_PATH}/benchmark_results.txt", "w") as file:
        file.write(f"Sync time: {sync_results[1]}\n")
        file.write(f"Threading time: {threading_results[1]}\n")
        file.write(f"Multiprocessing time: {multiprocessing_results[1]}\n")
