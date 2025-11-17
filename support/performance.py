"""decorator to calculate the execution time."""
import logging
import functools
import time

from config.holidayrobot_config import PRINT_PERFORMANCE

def timer(func):
    """decorator to measure executions time"""
    @functools.wraps(func)
    def time_wrapper(*args, **kwargs):
        start_time = time.perf_counter() # start counting
        value = func(*args, **kwargs)
        end_time = time.perf_counter() # end of counting time

        run_time = (end_time - start_time) * 1000
        if PRINT_PERFORMANCE:
            logging.info("Finished %r in %.4f milliseconds.", func.__name__, run_time)
        return value
    return time_wrapper