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

import os

def change_extension_to_txt(file_name):
    # Split the file name and extension
    base_name, extension = os.path.splitext(file_name)
    # Change the extension to ".txt"
    new_file_name = base_name + ".txt"
    return new_file_name

def get_file_name():
    file_name = input("Enter the file name: ")
    return file_name

# Step 1: Get the file name from the user
file_name = get_file_name()

# Step 2: Extract the file extension and change it to ".txt"
new_file_name = change_extension_to_txt(file_name)

print(f"The new file name with extension changed to .txt is: {new_file_name}")

import magic

def detect_mime_type(file_path):
    mime = magic.Magic(mime=True)
    return mime.from_file(file_path)

def detect_file_extension(file_path):
    mime = magic.Magic()
    return mime.from_file(file_path)

def get_file_path():
    file_path = input("Enter the file path: ")
    return file_path

# Step 1: Get the file path from the user
file_path = get_file_path()

# Step 2: Detect the MIME type and the real file extension
mime_type = detect_mime_type(file_path)
real_extension = detect_file_extension(file_path)

print("MIME type:", mime_type)
print("Real file extension:", real_extension)



