from functools import wraps
from time import perf_counter

# ---------------------------------------------------------
# Decorator para medição de tempo
# ---------------------------------------------------------

def timed(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = perf_counter()

        result = func(*args, **kwargs)

        end = perf_counter()

        elapsed = end - start

        print(
            f"[TIMER] {func.__name__}: "
            f"{elapsed:.6f} segundos"
        )

        return result

    return wrapper