from bottle import route, get, post, request, redirect, static_file

import model

user_details = {}                   # User details kept for us
session = {}                        # Session information (logged in state)
page = {}                           # Determines the page information

# -----------------------------------------------------------------------------
'''
    This file will handle our typical Bottle requests and responses
    You should not have anything beyond basic page loads, handling forms and
    maybe some simple program logic
'''


# -----------------------------------------------------------------------------
# Static file paths
# -----------------------------------------------------------------------------

# Allow image loading
@route('/img/<picture:path>')
def serve_pictures(picture):
    return static_file(picture, root='img/')


# -----------------------------------------------------------------------------

# Allow CSS
@route('/css/<css:path>')
def serve_css(css):
    return static_file(css, root='css/')


# -----------------------------------------------------------------------------

# Allow javascript
@route('/js/<js:path>')
def serve_js(js):
    return static_file(js, root='js/')


# -----------------------------------------------------------------------------
# Pages
# -----------------------------------------------------------------------------

# Redirect to login
@get('/')
@get('/home')
def get_index():
    return model.index_page()


# -----------------------------------------------------------------------------

# Display the login page
@get('/register')
def get_register_controller():
    return model.register_page()

# -----------------------------------------------------------------------------

# Attempt the login
@post('/register')
def post_register():
    # Handle the form processing
    ids = request.POST.get('ids')
    username = request.POST.get('username')
    password = request.POST.get('password')
    role = request.POST.get('role')
    donecodes = request.POST.get('donecode')
    doingcodes = request.POST.get('doingcode')
    programming_languages = request.POST.get('programming_languages')
    email = request.POST.get('email')

    # Call the appropriate method
    return model.register_add(username, password, role, donecodes, doingcodes, programming_languages, email)


# -----------------------------------------------------------------------------

# Display the login page
@get('/login')
def get_login_controller():
    return model.login_page()


# -----------------------------------------------------------------------------

# Attempt the login
@post('/login')
def post_login():
    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')

    # Call the appropriate method
    return model.login_check(username, password)

# -----------------------------------------------------------------------------

# Display the forgotPassword page
@get('/password')
def get_password_controller():
    return model.password_page()


# # -----------------------------------------------------------------------------

# Attempt the forgotPassword
@post('/password')
def post_forgotPassword():
    # Handle the form processing
    username = request.forms.get('username')
    email = request.forms.get('email')
    newPassword = request.forms.get('password')

    # Call the appropriate method
    return model.password_change(username, email, newPassword)


# -----------------------------------------------------------------------------

# Display the discussion page
@get('/discussion')
def get_discussion_controller():
    return model.discussion_page()


# -----------------------------------------------------------------------------

# Display the resource page
@get('/resource')
def get_resource_controller():
    return model.resource_page()


# -----------------------------------------------------------------------------

# Display the message page
@get('/message')
def get_message_controller():
    return model.message_page()


# -----------------------------------------------------------------------------

@get('/about')
def get_about():
    return model.about_page()


# -----------------------------------------------------------------------------
@get('/mainpage')
def get_main_page():
    return model.main_page()


# -----------------------------------------------------------------------------
@get('/logout')
def get_logout_page():
    return model.logout_page()

# -----------------------------------------------------------------------------
@get('/chats')
def get_chats_page():
    return model.chats_page()
