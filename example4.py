def process_data(numbers):
    def calculate_average():
        if not numbers:  # Handling division by zero within function
            return 0  
        total = sum(numbers)
        count = len(numbers)
        return total / count  

    if not numbers:
        return "No numbers provided"
    
    avg = calculate_average()  # Correctly calling the function
    return f"Average: {avg}"
print(process_data([1,2,3]))


