auth.py:
  integrate createUser, getUserInfo, & getUserId into login
  rename showLogin to login
  uncomment line 111 (login_session['email'])
  rename output to response
  refactor response =, response.headers, & return response
  test if (login_session['provider'] = 'google') can/should be removed
  
models.py:
  add email to User

addgammes.py:
  add email to users

apis.py:
  create blueprint for apis
  add routes for items, owner, & catagories
  add functions to jsonify items, owners, & catagories

controls.py:
  write check username function
    include check login in function

views.py:
  import apis.py
  import controls.py
  add blueprint for apis
  add check username to all edit, new, & delete functions

homepage.html:
  render all items seperated by catagory

static/app.css:
  add general background style for all pages
  add style for catagories in homepage