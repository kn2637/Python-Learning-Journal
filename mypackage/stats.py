
def mean(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return round(total/len(numbers), 2)

def max_(numbers):
    return max(numbers)
