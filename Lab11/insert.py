import psycopg2
from config import load_config

def create_procedure():
    sql = """
        CREATE OR REPLACE PROCEDURE insert(name VARCHAR(255), surname VARCHAR(255), phone VARCHAR(15))
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
        

def run_procedure(n, s, p):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL insert(%s, %s, %s)', (n, s, p))
    except(psycopg2.DatabaseError, Exception) as error:
        print(error)   



if __name__ == "__main__":
    create_procedure()
    user = input("Insert name, surname, phone number: ")
    s_user = user.split()
    run_procedure(s_user[0], s_user[1], s_user[2])