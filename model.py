import random
from bottle import run, route, template, request, response

'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view
import sql

# Initialise our views, all arguments are defaults
page_view = view.View()
database = sql.SQLDatabase()

database.database_setup()

# login = False

session = {"logged_in":False}    #Session  information(logged in state)

# -----------------------------------------------------------------------------
# Index
# -----------------------------------------------------------------------------

def index_page():

    return page_view("index")


# -----------------------------------------------------------------------------
# register
# -----------------------------------------------------------------------------

def register_add(username, password, role, donecodes, doingcodes, programming_languages, email):

    if username is None or password is None or role is None or email is None:

        err_str = "Username or Password or Role or Email cannot be null"

        return page_view("invalid_Register", reason=err_str)

    else:

        falg = database.add_user(username, password, role, donecodes, doingcodes, programming_languages, email)

        if falg:
            return page_view("login", name = username)
        else:
            err_str = "Username alreay exist"
            return page_view("invalid_Register", reason=err_str)



# -----------------------------------------------------------------------------
# register
# -----------------------------------------------------------------------------

def register_page():
    return page_view("register")


# -----------------------------------------------------------------------------
# Login
# -----------------------------------------------------------------------------

def login_page():

    # username = request.get_cookie('username', secret = 'usafe')
    # password = request.get_cookie('password', secret = 'psafe')
    #
    # if username and password:
    #     return page_view("already_login")

    # Check if the user is logged in, if not: back to login.
    if(session["logged_in"]):
        return page_view("already_login")

    return page_view("login")

# def check_login():
#     # username = request.get_cookie('username',secret = 'usafe')
#     # password = request.get_cookie('password', secret = 'psafe')
#
#     login_page()
#     if database.check_credentials(username, password):
#         return page_view("already_login")
#     return page_view("login")


# -----------------------------------------------------------------------------

# Check the login credentials
def login_check(username, password):
    # By default assume bad creds

    if database.check_credentials(username, password):

        # response.set_cookie('username', username, secret = 'usafe', httponly = True, max_age = 600)
        # response.set_cookie('password', password, secret = 'psafe', httponly = True, max_age = 600)

        session["logged_in"] = True

        # login = True
        return page_view("discussion", name=username)
    else:
        # login = False
        err_str = "Incorrect Password"
        return page_view("invalid_Login", reason=err_str)



# def check_login(username, password):
#     # By default assume bad creds
#
#     if database.check_credentials(username, password):
#         return True
#     else:
#         return False



# -----------------------------------------------------------------------------
# Change Password
# -----------------------------------------------------------------------------

def password_page():
    return page_view("password")



# # -----------------------------------------------------------------------------

# Change password
def password_change(username, email, newPassword):
    # By default assume bad creds
    credentials = database.change_password(username, email, newPassword)


    if credentials:
        return page_view("login", name=username)
    else:
        err_str = "Username or Email not correct"
        return page_view("invalid_change", reason=err_str)


# -----------------------------------------------------------------------------
# discussion
# -----------------------------------------------------------------------------

def discussion_page():

    # username = request.get_cookie("account", secret= 'some-secret-key')
    # if username:
    #     return page_view("discussion")
    #
    # return page_view("NotLogin")
    if(not session["logged_in"]):
        return page_view("NotLogin")

    return page_view("discussion")
    #
    # if login:
    #     return page_view("discussion")
    # else:
    #     return page_view("login")


# -----------------------------------------------------------------------------
# resource
# -----------------------------------------------------------------------------

def resource_page():
    if(not session["logged_in"]):
        return page_view("NotLogin")

    return page_view("resource")



# -----------------------------------------------------------------------------
# Message
# -----------------------------------------------------------------------------

def message_page():

    if(not session["logged_in"]):
        return page_view("NotLogin")

    return page_view("message")


# -----------------------------------------------------------------------------
# About
# -----------------------------------------------------------------------------

def about_page():

    if(not session["logged_in"]):
        return page_view("NotLogin")

    return page_view("about", garble=about_garble())



# -----------------------------------------------------------------------------
# Main page
# -----------------------------------------------------------------------------

def main_page():
    return page_view("mainpage")


# -----------------------------------------------------------------------------
# Logout page
# -----------------------------------------------------------------------------

def logout_page():

    if(not session["logged_in"]):
        return page_view("NotLogin")


    session["logged_in"] = False

    return page_view("logout")


# -----------------------------------------------------------------------------


def chats_page():

    if(not session["logged_in"]):
        return page_view("NotLogin")

    return page_view("chats")



# -----------------------------------------------------------------------------

# Returns a random string each time
def about_garble():
    garble = ["leverage agile frameworks to provide a robust synopsis for high level overviews.",
              "iterate approaches to corporate strategy and foster collaborative thinking to further the overall "
              "value proposition.",
              "organically grow the holistic world view of disruptive innovation via workplace diversity and "
              "empowerment.",
              "bring to the table win-win survival strategies to ensure proactive domination.",
              "ensure the end of the day advancement, a new normal that has evolved from generation X and is on the "
              "runway heading towards a streamlined cloud solution.",
              "provide user generated content in real-time will have multiple touchpoints for offshoring."]
    return garble[random.randint(0, len(garble) - 1)]

# -----------------------------------------------------------------------------
