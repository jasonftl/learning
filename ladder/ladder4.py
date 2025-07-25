# ladder4.py - Ladder problem: basic recursion
# Author: Jason (jasonftl) - 25th July 2025
# https://github.com/jasonftl/learning

import time
from ladder1 import ladder1            # imported functions are lower snake_case
from ladder2 import Ladder as Ladder2  # imported classes are PascalCase
from ladder3 import Ladder as Ladder3  # imported classes are PascalCase

if __name__ == "__main__":
    step_count = 36
    
    print(f"Working out number of 1 and 2 step combinations for a ladder with {step_count} rungs.")

    # Test function approach (ladder1.py)
    start_time = time.perf_counter_ns()
    result1 = ladder1(step_count)
    end_time = time.perf_counter_ns()
    function_time = end_time - start_time
    
    # Test class without cache (ladder2.py)
    ladder2 = Ladder2()
    start_time = time.perf_counter_ns()
    result2 = ladder2.calculate(step_count)
    end_time = time.perf_counter_ns()
    class_no_cache_time = end_time - start_time
    
    # Test class with cache (ladder3.py)
    ladder3 = Ladder3()
    start_time = time.perf_counter_ns()
    result3 = ladder3.calculate(step_count)
    end_time = time.perf_counter_ns()
    class_with_cache_time = end_time - start_time
    
    # Output Results
    print(f"Time taken: {function_time:.0f} nanoseconds to provide {result1} result (uncached function).")
    print(f"Time taken: {class_no_cache_time:.0f} nanoseconds to provide {result2} result (uncached class).")
    print(f"Time taken: {class_with_cache_time:.0f} nanoseconds to provide {result3} result (cached class).")
