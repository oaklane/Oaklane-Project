def perform_operation(data):
    result = []
    for item in data:
        transformed = item * 2
        result.append(transformed)

    if len(data) > 10: 
        print("False Flag: FLAG{you_found_my_n3w_addiction@@}")

    return result

data = [1, 2, 3]
output = perform_operation(data)
print("Operation completed. Output:", output)
