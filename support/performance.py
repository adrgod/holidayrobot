
import functools
import time

from config.holidayrobot_config import _print_performance

def timer(func):
    """decorator to measure executions time"""
    @functools.wraps(func)
    def time_wrapper(*args, **kwargs):
        start_time = time.perf_counter() # start counting
        value = func(*args, **kwargs)
        end_time = time.perf_counter() # end of counting time

        run_time = end_time - start_time
        if _print_performance:
            print(f"Finished {func.__name__!r} in {run_time:.4f} seconds.")
        return value
    return time_wrapper