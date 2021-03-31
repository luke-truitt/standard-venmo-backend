import psycopg2
import os
import uuid 
from datetime import datetime

CLEAR_CALCULATOR_TABLE = "DELETE FROM Calculator"
CLEAR_WAITLIST_TABLE = "DELETE FROM Waitlist"
DROP_CALCULATOR_TABLE = "DROP TABLE Calculator"
DROP_WAITLIST_TABLE = "DROP TABLE Waitlist"
CREATE_WAITLIST_TABLE = """CREATE TABLE WAITLIST (
    Email varchar(255), 
    ReferToId varchar(255),
    ReferById varchar(255),
    Time varchar(255)
)"""
CREATE_CALCULATOR_TABLE = """CREATE TABLE Calculator ( 
        ApplicantId SERIAL PRIMARY KEY, 
        Email varchar(255), 
        EstimatedIncome int, 
        State varchar(255), 
        Dependent varchar(255), 
        EducationExpenses int,
        LoanPayments int,
        Student varchar(10),
        Citizen varchar(10),
        ReferToId varchar(255),
        ReferById varchar(255),
        Time varchar(255)
        );"""

ADD_EMAIL = "INSERT INTO waitlist (email, referToId, referById, time) values ('{}','{}','{}','{}')"
ADD_CALC  = "INSERT INTO calculator (email, estimatedincome, state, dependent, educationexpenses, loanpayments, student, citizen, referToId, referById, time) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"

def add_email(data):
    email = data.get("email") if data.get("email") is not None else ''
    referToId = str(uuid.uuid4())
    referById = data.get("referById") if data.get("referById") is not None else "n/a"
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        conn = psycopg2.connect(
                database = os.getenv("DATABASE"),
                user = os.getenv("USERNAME"),
                password = os.getenv("PASSWORD"),
                host = os.getenv("HOST"),
                port = os.getenv("DATAPORT"),
            )
        cur = conn.cursor()
        cur.execute(ADD_EMAIL.format(email,referToId, referById, time))
        conn.commit()
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return referToId

def add_calc_result(data):
    # first_name = data.get("firstName") if data.get("firstName") is not None else ''
    # last_name = data.get("lastName") if data.get("lastName") is not None else ''
    # international = data.get("international") if data.get("international") is not None else ''
    # class_year = data.get("classYear") if data.get("classYear") is not None else 0
    # estimated_refund = data.get("estimatedRefund") if data.get("estimatedRefund") is not None else 0
    # tax_credits = data.get("taxCredits") if data.get("taxCredits") is not None else ''
    # how_filed = data.get("howFiled") if data.get("howFiled") is not None else ''
    # phone_number = data.get("phone") if data.get("phone") is not None else ''

    email = data.get("email") if data.get("email") is not None else ''
    state = data.get("state") if data.get("state") is not None else ''
    dependent = data.get("dependent") if data.get("dependent") is not None else ''
    estimated_income = data.get("estimatedIncome") if data.get("estimatedIncome") is not None else 0
    education_payments = data.get("educationExpenses") if data.get("educationExpenses") is not None else 0
    loan_payments = data.get("loanPayments") if data.get("loanPayments") is not None else 0
    student = data.get("student") if data.get("student") is not None else "No"
    citizen = data.get("citizen") if data.get("citizen") is not None else "No"
    referToId = data.get("referToId") if data.get("referToId") is not None else "n/a"
    referById = data.get("referById") if data.get("referById") is not None else "n/a"
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        conn = psycopg2.connect(
                database = os.getenv("DATABASE"),
                user = os.getenv("USERNAME"),
                password = os.getenv("PASSWORD"),
                host = os.getenv("HOST"),
                port = os.getenv("DATAPORT"),
                
            )
        cur = conn.cursor()
        cur.execute(ADD_CALC.format(email,estimated_income,state,dependent,education_payments,loan_payments,student,citizen,referToId, referById,time))
        conn.commit()
        cur.close()
        conn.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()

def create_tables():
    try:
        conn = psycopg2.connect(
                database = os.getenv("DATABASE"),
                user = os.getenv("USERNAME"),
                password = os.getenv("PASSWORD"),
                host = os.getenv("HOdST"),
                port = os.getenv("DATAPORT")
                
            )
        cur = conn.cursor()
        cur.execute(CREATE_WAITLIST_TABLE)
        cur.execute(CREATE_CALCULATOR_TABLE)
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
                database = os.getenv("DATABASE"),
                user = os.getenv("USERNAME"),
                password = os.getenv("PASSWORD"),
                host = os.getenv("HOST"),
                port = os.getenv("DATAPORT")
                
            )
        cur = conn.cursor()
        cur.execute(CLEAR_CALCULATOR_TABLE)
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
        cur.execute(DROP_CALCULATOR_TABLE)
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
# create_tables()