def rearrange_alphabetically(input_file, output_file):
    # Read the content of the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Sort the lines alphabetically
    sorted_lines = sorted(lines)

    # Write the sorted content to the output file
    with open(output_file, 'w') as file:
        file.writelines(sorted_lines)

# Example usage:
input_file = "/full/path/to/your/input.txt'" # Replace '/full/path/to/your/input.txt' with the full path to your input file
output_file = "/full/path/to/your/input.txt'"  # Replace '/full/path/to/your/output.txt' with the full path to your desired output file
rearrange_alphabetically(input_file, output_file)
