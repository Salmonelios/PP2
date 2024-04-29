import psycopg2
from config import load_config

def create_procedure():
    sql = """
        CREATE OR REPLACE PROCEDURE delete(phone VARCHAR(15))
        AS
        $$ 
        BEGIN
            IF EXISTS (SELECT 1 FROM phone_book WHERE phone_book.phone_number = phone) THEN
                DELETE FROM phone_book
                WHERE phone_number = delete.phone;
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
        

def run_procedure(p):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL delete(%s)', (p,))
    except(psycopg2.DatabaseError, Exception) as error:
        print(error)   



if __name__ == "__main__":
    create_procedure()
    user = input("Insert phone number: ")
    run_procedure(user)