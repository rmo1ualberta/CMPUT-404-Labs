#!/usr/bin/env python3
import cgi
import cgitb

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

def main():
    # setting up cgi form
    form = cgi.FieldStorage()
    username = form.getfirst("username")
    password = form.getfirst("password")



    # setting up cookie
    cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
    cookie_username = None
    cookie_password = None
    if cookie.get("username"):      # if there is a cookie that already has a username, retrieve it
        cookie_username = cookie.get("username").value
    if cookie.get("password"):
        cookie_password = cookie.get("password").value

    # check if login info provided by the cookie is correct
    cookie_ok = cookie_username == secret.username and cookie_password == secret.password
    # if so, set username and password to the cookie's login info
    if cookie_ok:
        username = cookie_username
        password = cookie_password

    print("Content-type: text/html")
    # if login is correct, set the cookie login info
    if form_ok(username, password):
        print(f"Set-Cookie: username={username}")
        print(f"Set-Cookie: password={password}")

    print()
    
    # load html pages according to the situation
    if not username and not password:
        print(login_page())
    elif form_ok(username, password):
        print(secret_page(username, password))
    else:
        print(after_login_incorrect())
        print(f"username & password: {username} {password}")

def form_ok(username, password):
    # check if the login info provided by user is correct
    return username == secret.username and password == secret.password

if __name__ == '__main__':
    cgitb.enable()
    main()
