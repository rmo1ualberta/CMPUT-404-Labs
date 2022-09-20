#!/usr/bin/env python3
import os
import json
import cgi

def main():
    show_query_param()

def show_env_var():
    # show all environment variables
    print("Content-type: text/plain")
    print()

    print(os.environ)

def show_env_var_json():
    # show env variables as json
    print("Content-type: application/json")
    print()

    print(json.dumps(dict(os.environ), indent=2))

def show_query_param():
    # show query parameter data and user's browser
    print("Content-type: text/html")
    print()

    print(f"<p>QUERY_STRING: {os.environ['QUERY_STRING']}</p>") 
    print(f"<p>HTTP_USER_AGENT: {os.environ['HTTP_USER_AGENT']}</p>") 

if __name__ == '__main__':
    main()




