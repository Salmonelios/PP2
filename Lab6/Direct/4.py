for i in range(65, 91):
    with open(r"./Alpha/" + f'{chr(i)}.txt', 'w') as file:
        file.write(f"File with {chr(i)} letter")