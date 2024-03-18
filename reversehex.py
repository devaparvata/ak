def reverse_hex(data):
    # Convert data to hexadecimal
    hex_data = data.hex()
    # Reverse the hexadecimal string
    reversed_hex_data = hex_data[::-1]
    # Convert the reversed hexadecimal data back to bytes
    reversed_data = bytes.fromhex(reversed_hex_data)
    return reversed_data

def get_initial_file():
    file_name = input("Enter the initial file name: ")
    return file_name

def save_to_file(data, file_name):
    with open(file_name, 'wb') as f:
        f.write(data)

# Step 1: Get the initial file name from the user
initial_file_name = get_initial_file()

# Step 2: Read the content of the initial file
try:
    with open(initial_file_name, 'rb') as f:
        initial_data = f.read()
except FileNotFoundError:
    print("Initial file not found.")
    exit()

# Step 3: Reverse the hex value of the initial file and save it as the second file
second_file_name = "reversed_" + initial_file_name
reversed_data = reverse_hex(initial_data)
save_to_file(reversed_data, second_file_name)
print(f"Reversed hex value of {initial_file_name} saved as {second_file_name}")

# Step 4: Reverse the hex value of the second file and save it as the third file
third_file_name = "reversed_" + second_file_name
reversed_reversed_data = reverse_hex(reversed_data)
save_to_file(reversed_reversed_data, third_file_name)
print(f"Reversed hex value of {second_file_name} saved as {third_file_name}")
