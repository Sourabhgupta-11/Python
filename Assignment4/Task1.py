try:
    file=open('sample.txt','r')
    fileContent=file.readlines()
    for i in range(len(fileContent)):
        print(f'Line {i+1}: {fileContent[i].strip()}')
except FileNotFoundError:
    print('Error: The file sample.txt was not found')