

file = open('output.txt', 'w')
fileContent = file.write(input("Enter text to write to the file: ")+'\n')
print("Data successfully written to output.txt\n")

file = open('output.txt', 'a')
appendContent = file.write(input("Enter additional text to append: ")+'\n')
print("Data successfully appended\n")

file = open('output.txt', 'r')
file_read = file.read().strip()
print("File content of output.txt:")
print(file_read)