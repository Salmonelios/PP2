import psycopg2
from config import load_config
import re

def create_procedure():
    sql = """
        CREATE OR REPLACE PROCEDURE insert_many(name VARCHAR(255), surname VARCHAR(255), phone VARCHAR(15))
        AS
        $$ 
        BEGIN
            IF EXISTS (SELECT 1 FROM phone_book WHERE phone_book.phone_number = phone) THEN
                UPDATE phone_book
                SET surname = insert.surname, name = insert.name
                WHERE phone_number = insert.phone;
            ELSE
                INSERT INTO phone_book VALUES
                (name, surname, phone);
            END IF;
        END; $$

        LANGUAGE plpgsql;       
        """
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
    except(psycopg2.DatabaseError, Exception) as error:
        print(error)
        

def run_procedure(lst):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for user in lst:
                    if len(user.split()) == 3:
                        n, s, p = user.split()
                        if len(p) == 12 and re.findall("\\+7.*", p) and n and s:
                            cur.execute('CALL insert(%s, %s, %s)', (n, s, p))
                            print(f'\033[92mUser {n} {s} added!\033[0m')
                        else:
                            print(f"\033[91mUser {n}, {s} did not added, check phone number.\033[0m")
                    else:
                        print("\033[91mNot enough data.\033[0m")
    except(psycopg2.DatabaseError, Exception) as error:
        print(error)
        

if __name__ == "__main__":
    create_procedure()
    lst = []
    while True:
        try:
            user = input("Insert name, surname, phone number: ")
        except EOFError:
            break
        lst.append(user)
        
    run_procedure(lst)