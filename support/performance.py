"""decorator to calculate the execution time."""
import logging
import functools
import time

from config import holidayrobot_config as conf

def _to_bool(v):
    if isinstance(v, bool):
        return v
    if v is None:
        return False
    return str(v).strip().lower() in ("true", "1", "yes", "y")

def timer(func):
    """decorator to print ut execution times"""
    @functools.wraps(func)
    def time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = (end_time - start_time) * 1000

        # prefer instance-level settings
        print_perf = None
        if args:
            inst = args[0]
            # check common attribute names that may hold the flag or config
            if hasattr(inst, "config"):
                print_perf = getattr(inst.config, "print_performance", None)
            if print_perf is None and hasattr(inst, "HRConfig"):
                print_perf = getattr(inst.HRConfig, "print_performance", None)
            if print_perf is None and hasattr(inst, "print_performance"):
                print_perf = getattr(inst, "print_performance", None)
            if print_perf is None and hasattr(inst, "perf"):
                print_perf = getattr(inst, "perf", None)

        # fallback to module-level config
        if print_perf is None:
            print_perf = getattr(conf, "PRINT_PERFORMANCE", False)

        print_perf = _to_bool(print_perf)

        if print_perf:
            logging.info("Finished %r in %.4f milliseconds.", func.__name__, run_time)
        return value
    return time_wrapper

def retry(max_retries=3, delay=1.0, backoff=2.0, exceptions=(Exception,)):
    """retry decorator"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            wait = delay
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempts > max_retries:
                        logging.error("Reached max retries for funciont %s with %s retries", func.__name__, attempts)
                        raise
                    logging.warning("Attempt %s/%s for %s failed (%s). Retrying in %.1fs",
                                    attempts, max_retries, func.__name__, exc, wait)
                    time.sleep(wait)
                    attempts += 1
                    wait *= backoff
        return wrapper
    return decorator
    



