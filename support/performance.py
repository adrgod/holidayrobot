import logging
import functools
import time

from config.holidayrobot_config import *

def timer(func):
    """decorator to measure executions time"""
    @functools.wraps(func)
    def time_wrapper(*args, **kwargs):
        start_time = time.perf_counter() # start counting
        value = func(*args, **kwargs)
        end_time = time.perf_counter() # end of counting time

        run_time = (end_time - start_time) * 1000
        if print_performance:
            logging.info(f"Finished {func.__name__!r} in {run_time:.4f} miliseconds.")
        return value
    return time_wrapper