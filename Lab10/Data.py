import psycopg2
import csv
import os

conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'postgres',
    user = 'postgres',
    password = 'roma2005ass'
)

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS phone_book (
            name VARCHAR(255),
            surname VARCHAR(255),
            phone_number VARCHAR(15) PRIMARY KEY
);
""")
conn.commit()

done  = True

while done:
    print("What do you want to do? ")
    typ = input()
    if typ == 'm':
        a = input("Name: ")
        b = input("Surname: ")
        c = input("Phone number: ")
        cur.execute(f"SELECT * FROM phone_book WHERE phone_number = '{c}'")
        existing_entry = cur.fetchone()
        if existing_entry:
            print('\033[91mPhone number already exits!\033[0m', end = "\n\n")
        else:
            cur.execute(f"""INSERT INTO phone_book (name, surname, phone_number) VALUES
                    ('{a}', '{b}', '{c}');
                    """)
            conn.commit()
            print('\033[92mUser added!\033[0m', end = "\n\n")
    elif typ == "csv":
        print("Write the name of csv file: ")
        name = input()
        if os.access(name + '.csv', os.F_OK):
            with open (name + '.csv', 'r') as file:
                rfile = csv.reader(file)
                for i in rfile:
                    Name, Surname, Phone = i
                    cur.execute(f"SELECT * FROM phone_book WHERE phone_number = '{Phone}'")
                    existing_entry = cur.fetchone()
                    if existing_entry:
                        print(f'\033[91mPhone number of {Name} {Surname} already exits!\033[0m')
                    else:
                        cur.execute(f"""INSERT INTO phone_book (name, surname, phone_number) VALUES
                                ('{Name}', '{Surname}', '{Phone}');
                                """)
                        conn.commit()
                        print(f'\033[92mUser {Name} {Surname} added!\033[0m')
        else: print("\033[91mFile was not found!\033[0m")
        print("")
    elif typ == 'c':
        ph = input("Enter the phone number: ")
        cur.execute(f"SELECT * FROM phone_book WHERE phone_number = '{ph}'")
        exist = cur.fetchone()
        if exist:
            mode = input("What do you whant to change: ")
            if mode == 'n':
                    new_name = input(f"The current name is {exist[0]}, enter new one: ")
                    cur.execute(f"""UPDATE phone_book
                                SET name = '{new_name}'
                                WHERE phone_number = '{ph}'
                                """)
                    conn.commit()
                    print('\033[92mName has been changed!\033[0m')
            if mode == 's':
                new_surname = input(f"The current surname is {exist[1]}, enter new one: ")
                cur.execute(f"""UPDATE phone_book
                            SET surname = '{new_surname}'
                            WHERE phone_number = '{ph}'
                            """)
                conn.commit()
                print('\033[92mSurname has been changed!\033[0m')
            if mode == 'p':
                new_ph = input(f"The current phone number is {exist[2]}, enter new one: ")
                cur.execute(f"""UPDATE phone_book
                            SET  phone_number = '{new_ph}'
                            WHERE phone_number = '{ph}'
                            """)
                conn.commit()
                print('\033[92mPhone number has been changed!\033[0m')
        else:
            print("\033[91mNo phone number found!\033[0m")
        print("")
    elif typ == "s":
        order = input("By which parameter should phone book be sorted? ")
        cur.execute(f"""SELECT * FROM phone_book
                    ORDER BY {order} ASC;""")
        tab = cur.fetchall()
        print("{:<29}{:<29}{:<29}".format("\033[94mName\033[0m", "\033[94mSurname\033[0m", "\033[94mPhone number\033[0m"))
        for val in tab:
            print("{:<20}{:<20}{:<20}".format(val[0],val[1], val[2]))
        print("")
    elif typ == "d":
        ph = input("Enter the phone number: ")
        cur.execute(f"SELECT * FROM phone_book WHERE phone_number = '{ph}'")
        existing_entry = cur.fetchone()
        if existing_entry:
            cur.execute(f"SELECT * FROM phone_book WHERE phone_number = '{ph}'")
            deleted = cur.fetchone()
            cur.execute(f"DELETE FROM phone_book WHERE phone_number = '{ph}'")
            conn.commit()
            print(f"\033[92mUser {deleted[0]} {deleted[1]} has been deleted!\033[0m")
        else:
            print("\033[91mNo phone number found!\033[0m")
    elif typ == "e":
        done = False
