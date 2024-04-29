import psycopg2
from config import load_config

def create_function():
    sql = """
        CREATE OR REPLACE FUNCTION search_by_pattern(par VARCHAR(255))
        RETURNS TABLE(name VARCHAR(255), surname VARCHAR(255), phone_number VARCHAR(15)) AS
        $$
        BEGIN
            RETURN QUERY

            SELECT *
            FROM phone_book
            WHERE phone_book.name LIKE '%' || par || '%'
            OR phone_book.surname LIKE '%' || par || '%'
            OR phone_book.phone_number LIKE '%' || par || '%';

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
        

def run_function(patt):
    
    found = []
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.callproc('search_by_pattern', (patt,))
                row = cur.fetchone()
                while row is not None:
                    found.append(row)
                    row = cur.fetchone()
    except(psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return found    



if __name__ == "__main__":
    create_function()
    search = input("Insert the pattern: ")
    found = run_function(search)
    print("{:<29}{:<29}{:<29}".format("\033[94mName\033[0m", "\033[94mSurname\033[0m", "\033[94mPhone number\033[0m"))
    for val in found:
            print("{:<20}{:<20}{:<20}".format(val[0],val[1], val[2]))