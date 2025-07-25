# ladder1.py - Ladder problem: basic recursion
# Author: Jason (jasonftl) - 25th July 2025
# https://github.com/jasonftl/learning

def ladder1(input_number):
    if input_number > 2:
        return ladder1(input_number -1) + ladder1(input_number -2)
    elif input_number == 2:
        return 2
    elif input_number == 1:
        return 1

if __name__ == "__main__":
    step_count = 36
    ladder_result = ladder1(step_count)
    print(f"For {step_count} steps there are this many 1 and or 2 step options: {ladder_result}")