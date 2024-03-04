with open("test.txt", 'r') as file:
    with open('test2.txt', 'w') as file1:
        file1.write(file.read())