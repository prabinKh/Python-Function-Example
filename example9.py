"""
1. first function to calcultate the mean
2. second function to calculate the median
3. third function to calculate the mode
"""

def mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

def median(numbers):
    numbers_short = sorted(numbers)
    n = len(numbers_short)
    mid = n // 2
    if n % 2 == 0:
        return (numbers_short[mid -1] + numbers_short[mid]) / 2
    else:
        return numbers_short[mid]
    
def mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    mode = count.most_common(1)[0][0]
    return mode

def __main__(numbers):
    mean_a = mean(numbers)
    median_a = median(numbers)
    mode_a = mode(numbers)
    returns={
        'mean': mean_a,
        'median': median_a,
        'mode': mode_a,
    }
    return returns

if __name__ == "__main__":
    number = [1,2,4,4,5,6,9]
    final_result = __main__(number)

    for r, i in final_result.items():
        print(f"{r} :{i}")