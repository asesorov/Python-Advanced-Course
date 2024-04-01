import math
import logging
import time
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from pathlib import Path


ARTIFACTS_PATH = Path(__file__).resolve().parents[1] / 'artifacts' / '4.2'
logging.basicConfig(filename='integrate_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        return result, execution_time
    return wrapper


def worker(f, start, end, step):
    acc = 0
    x = start
    while x < end:
        acc += f(x) * step
        x += step
    return acc


@measure_time
def integrate(f, a, b, n_jobs=1, n_iter=1000, executor_type='thread'):
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs
    futures = []

    with (ThreadPoolExecutor(max_workers=n_jobs) if executor_type == 'thread'
          else ProcessPoolExecutor(max_workers=n_jobs)) as executor:
        for i in range(n_jobs):
            start = a + i * chunk_size * step
            end = start + chunk_size * step if i < n_jobs - 1 else b
            logging.info(f"Job {i+1} started.")
            futures.append(executor.submit(worker, f, start, end, step))

        results = [future.result() for future in concurrent.futures.as_completed(futures)]
        logging.info("All jobs completed.")
        return sum(results)


def run_integration_tests(f, a, b, max_jobs, n_iter, executor_type):
    cpu_num = max_jobs // 2
    times = {}
    for n_jobs in range(1, cpu_num * 2 + 1):
        result, execution_time = integrate(f, a, b, n_jobs=n_jobs, n_iter=n_iter, executor_type=executor_type)
        times[n_jobs] = execution_time
        print(f"Result: {result}, Time taken with {n_jobs} jobs ({executor_type}): {times[n_jobs]} seconds")
    return times


def run_integration_tests(f, a, b, max_jobs, n_iter, executor_type):
    cpu_num = max_jobs // 2
    times = {}
    for n_jobs in range(1, cpu_num * 2 + 1):
        start_time = time.time()
        result = integrate(f, a, b, n_jobs=n_jobs, n_iter=n_iter, executor_type=executor_type)
        end_time = time.time()
        times[n_jobs] = end_time - start_time
        print(f"Result: {result}, Time taken with {n_jobs} jobs ({executor_type}): {times[n_jobs]} seconds")
    return times


if __name__ == "__main__":
    max_jobs = 6
    n_iter = 10000

    thread_times = run_integration_tests(math.cos, 0, math.pi / 2, max_jobs, n_iter, 'thread')
    process_times = run_integration_tests(math.cos, 0, math.pi / 2, max_jobs, n_iter, 'process')

    with open(f'{ARTIFACTS_PATH}/timing_comparison.txt', 'w') as file:
        file.write("ThreadPoolExecutor times:\n")
        for n_jobs, time_taken in thread_times.items():
            file.write(f"{n_jobs} jobs: {time_taken} seconds\n")

        file.write("\nProcessPoolExecutor times:\n")
        for n_jobs, time_taken in process_times.items():
            file.write(f"{n_jobs} jobs: {time_taken} seconds\n")
