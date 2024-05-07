def read_file_in_reverse(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines.reverse()  # Reverse the order of lines

    for line in lines:
        print(line.rstrip())  # Print each line in reverse order

file_name = 'example.txt'  # Replace 'example.txt' with your file name
read_file_in_reverse(file_name)
