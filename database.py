import psycopg2
import os
import uuid 
from datetime import datetime

CLEAR_WAITLIST_TABLE = "DELETE FROM Waitlist"

DROP_WAITLIST_TABLE = "DROP TABLE Waitlist"
CREATE_WAITLIST_TABLE = """CREATE TABLE WAITLIST (
    Email varchar(255), 
    LandingPageID int,
    Time varchar(255)
)"""

ADD_EMAIL = "INSERT INTO waitlist (email, landingPageId, time) values ('{}','{}','{}')"

def add_email(data):
    email = data.get("email") if data.get("email") is not None else ''
    landingPageId = data.get("landingPageId") if data.get("landingPageId") is not None else ''
    waitlist_spot = get_waitlist_position(landingPageId) + 1000
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        conn = psycopg2.connect(
                # database = os.getenv("DATABASE"),
                # user = os.getenv("USERNAME"),
                # password = os.getenv("PASSWORD"),
                # host = os.getenv("HOST"),
                # port = os.getenv("DATAPORT"),
                database = "der447s69tcb66",
                user = "veirluzsqkanmi",
                password = "0e01540c042256fae0efbfb765bd5377c60c54b56c2df6192598d380c45d928d",
                host = "ec2-54-237-143-127.compute-1.amazonaws.com",
                port = "5432"
            )
        cur = conn.cursor()
        cur.execute(ADD_EMAIL.format(email,landingPageId, time))
        conn.commit()
        cur.close()
        conn.close()
        return waitlist_spot

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def get_waitlist_position(num):
    try:
        conn = psycopg2.connect(
                # database = os.getenv("DATABASE"),
                # user = os.getenv("USERNAME"),
                # password = os.getenv("PASSWORD"),
                # host = os.getenv("HOST"),
                # port = os.getenv("DATAPORT"),
                database = "der447s69tcb66",
                user = "veirluzsqkanmi",
                password = "0e01540c042256fae0efbfb765bd5377c60c54b56c2df6192598d380c45d928d",
                host = "ec2-54-237-143-127.compute-1.amazonaws.com",
                port = "5432"
            )
        cur = conn.cursor()
        cur.execute("SELECT email FROM waitlist WHERE landingPageId={}".format(num))
        waitlist = cur.fetchall()
        waitlist_len = len(waitlist)
        spot = waitlist_len + 1
        cur.close()
        conn.close()
        return spot

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
def create_table():
    try:
        conn = psycopg2.connect(
                # database = os.getenv("DATABASE"),
                # user = os.getenv("USERNAME"),
                # password = os.getenv("PASSWORD"),
                # host = os.getenv("HOST"),
                # port = os.getenv("DATAPORT")
                database = "der447s69tcb66",
                user = "veirluzsqkanmi",
                password = "0e01540c042256fae0efbfb765bd5377c60c54b56c2df6192598d380c45d928d",
                host = "ec2-54-237-143-127.compute-1.amazonaws.com",
                port = "5432"
            )
        cur = conn.cursor()
        cur.execute(CREATE_WAITLIST_TABLE)
        conn.commit()
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def clear_table() :
    try:
        conn = psycopg2.connect(
                # database = os.getenv("DATABASE"),
                # user = os.getenv("USERNAME"),
                # password = os.getenv("PASSWORD"),
                # host = os.getenv("HOST"),
                # port = os.getenv("DATAPORT")
                database = "der447s69tcb66",
                user = "veirluzsqkanmi",
                password = "0e01540c042256fae0efbfb765bd5377c60c54b56c2df6192598d380c45d928d",
                host = "ec2-54-237-143-127.compute-1.amazonaws.com",
                port = "5432"
            )
        cur = conn.cursor()
        cur.execute(CLEAR_WAITLIST_TABLE)
        conn.commit()
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def drop_tables():
    try:
        conn = psycopg2.connect(
                database = os.getenv("DATABASE"),
                user = os.getenv("USERNAME"),
                password = os.getenv("PASSWORD"),
                host = os.getenv("HOST"),
                port = os.getenv("DATAPORT")
            )
        cur = conn.cursor()
        cur.execute(DROP_WAITLIST_TABLE)
        conn.commit()
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

# drop_tables()
# create_table()