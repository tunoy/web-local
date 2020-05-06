import sqlite3
import sys

# This class is a simple handler for all of our SQL database actions
# Practicing a good separation of concerns, we should only ever call
# These functions from our models

# If you notice anything out of place here, consider it to your advantage and don't spoil the surprise

class SQLDatabase():

    # Get the database running
    def __init__(self, database_arg="my_database.sqlite"):
        self.conn = sqlite3.connect(database_arg)
        self.cur = self.conn.cursor()

    # SQLite 3 does not natively support multiple commands in a single statement
    # Using this handler restores this functionality
    # This only returns the output of the last command
    def execute(self, sql_string):
        out = None
        for string in sql_string.split(";"):
            try:
                out = self.cur.execute(string)
            except:
                pass
        return out

    # Commit changes to the database
    def commit(self):
        self.conn.commit()

    #-----------------------------------------------------------------------------

    # Sets up the database
    # Default admin password
    def database_setup(self):
# , admin_password='admin'
        # Clear the database if needed
        # self.execute("DROP TABLE IF EXISTS Users")
        # self.commit()

        # Create the users table
        # self.execute("""CREATE TABLE Users(
        #     username varchar(20) Primary key,
        #     password varchar(20),
        #     role varchar(20),
        #     donecodes varchar(100),
        #     doingcodes varchar(100),
        #     programming_languages varchar(100),
        #     email varchar(20)
        # )""")

        sql = """CREATE TABLE IF NOT EXISTS Users(
            username varchar(20) Primary key,
            password varchar(20),
            role varchar(20),
            donecodes varchar(100),
            doingcodes varchar(100),
            programming_languages varchar(100),
            email varchar(20)
        )"""

        self.cur.execute(sql)
        self.commit()

# admin INTEGER DEFAULT 0
        # # Add our admin user
        # self.add_user('admin', admin_pasword, admin=1)
        # self.add_user('123', '123','student','COMP2123','INFO2222','HTML','yoli0439@uni.sydney.edu.au')


    #-----------------------------------------------------------------------------
    # User handling
    #-----------------------------------------------------------------------------

    # Add a user to the database
    def add_user(self, username, password, role, donecodes, doingcodes, programming_languages, email):

        sql_query = """
                SELECT *
                FROM Users
                WHERE username = '{username}'
            """.format(username=username)


        self.execute(sql_query)
        r = self.cur.fetchone()



        if r is not None:

            self.commit()

            return False
        else:
            sql_cmd = """
                    INSERT INTO Users
                    VALUES('{username}', '{password}','{role}','{donecodes}','{doingcodes}','{programming_languages}','{email}')
                """.format(username=username, password=password, role=role, donecodes=donecodes, doingcodes=doingcodes, programming_languages=programming_languages, email=email)

            self.execute(sql_cmd)

            self.commit()

            return True

    #-----------------------------------------------------------------------------

    # Check login credentials
    def check_credentials(self, username, password):

        sql_query = """
                SELECT *
                FROM Users
                WHERE username = '{username}' AND password = '{password}'
            """.format(username=username, password=password)

        self.execute(sql_query)

        self.commit()

        # If our query returns
        if self.cur.fetchone():
            return True
        else:
            return False

    #-----------------------------------------------------------------------------

    # Check login credentials
    def change_password(self, username, email, password):

        sql = """
                SELECT *
                FROM Users
                WHERE username = '{username}' AND email = '{email}'
            """.format(username=username, email=email)

        self.execute(sql)

        self.commit()

        # If our query returns
        if self.cur.fetchone():
            sql_query = """
                    UPDATE Users
                    SET password = '{password}'
                    WHERE username = '{username}' AND email = '{email}'
                """.format(password=password, username=username, email = email)

            self.execute(sql_query)

            self.commit()

            return True
        else:
            return False
