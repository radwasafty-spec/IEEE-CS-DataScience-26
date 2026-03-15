def get_numbers():
    while True:
        try:
            input_str = input("Enter heart rate readings separated by spaces: ")
            if not input_str.strip():
                continue
            numbers = []
            for val in input_str.split():
                numbers.append(float(val))
            return numbers
        except ValueError:
            print("Error: Invalid input.")

def manual_sort(numbers):
    arr = list(numbers)
    n = 0
    for _ in arr: n += 1
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def get_count(numbers):
    count = 0
    for _ in numbers:
        count += 1
    return count

def get_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def get_min(numbers):
    if not numbers: return None
    minimum = numbers[0]
    for n in numbers:
        if n < minimum:
            minimum = n
    return minimum

def get_max(numbers):
    if not numbers: return None
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum

def get_mean(numbers):
    count = get_count(numbers)
    if count == 0: return 0
    return get_sum(numbers) / count

def get_median(numbers):
    count = get_count(numbers)
    if count == 0: return None
    sorted_list = manual_sort(numbers)
    mid = count // 2
    if count % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    return sorted_list[mid]

def get_range(numbers):
    if not numbers: return 0
    return get_max(numbers) - get_min(numbers)

def get_variance(numbers):
    count = get_count(numbers)
    if count == 0: return 0
    mean = get_mean(numbers)
    sum_sq_diff = 0
    for n in numbers:
        sum_sq_diff += (n - mean) ** 2
    return sum_sq_diff / count

def get_std_dev(numbers):
    variance = get_variance(numbers)
    return variance ** 0.5

def get_quartiles(numbers):
    count = get_count(numbers)
    if count == 0: return None, None, None
    sorted_list = manual_sort(numbers)
    
    def find_median(data):
        c = get_count(data)
        m = c // 2
        if c % 2 == 0:
            return (data[m-1] + data[m]) / 2
        return data[m]

    mid = count // 2
    if count % 2 == 0:
        q1 = find_median(sorted_list[:mid])
        q3 = find_median(sorted_list[mid:])
    else:
        q1 = find_median(sorted_list[:mid])
        q3 = find_median(sorted_list[mid+1:])
    
    return q1, get_median(numbers), q3

def main():
    data = get_numbers()
    if not data:
        print("Empty list provided.")
        return

    q1, q2, q3 = get_quartiles(data)
    
    print(f"\n--- Health Monitoring Report ---")
    print(f"Count: {get_count(data)}")
    print(f"Min: {get_min(data)}")
    print(f"Max: {get_max(data)}")
    print(f"Mean: {get_mean(data):.2f}")
    print(f"Median: {q2}")
    print(f"Range: {get_range(data)}")
    print(f"Standard Deviation: {get_std_dev(data):.2f}")
    print(f"Q1: {q1}, Q3: {q3}")

if __name__ == "__main__":
    main()