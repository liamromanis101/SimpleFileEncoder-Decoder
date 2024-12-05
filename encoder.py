import sys
import binascii

if len(sys.argv) != 3:
    print("Usage: python encode.py <input_file> <output_file>")
    sys.exit(1)
  
input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, "rb") as infile:
        binary_data = infile.read()
    hex_data = binascii.hexlify(binary_data).decode("ascii")
    with open(output_file, "w") as outfile:
        outfile.write(hex_data)
    print(f"File encoded successfully to {output_file}")
except Exception as e:
    print(f"Error: {e}")
