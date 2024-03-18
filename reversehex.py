def reverse_hex_file(input_file, output_file):
    try:
        # Read the contents of the input file
        with open(input_file, 'rb') as f:
            data = f.read()
        
        # Convert the data to hexadecimal
        hex_data = data.hex()
        
        # Reverse the hexadecimal string
        reversed_hex_data = hex_data[::-1]
        
        # Write the reversed hexadecimal data to the output file
        with open(output_file, 'w') as f:
            f.write(reversed_hex_data)
        
        print("Hexadecimal data reversed and written to", output_file)
    
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
input_file = 'input.txt'  # Replace 'input.txt' with the name of your input file
output_file = 'reversed_hex.txt'  # Output file name
reverse_hex_file(input_file, output_file)
