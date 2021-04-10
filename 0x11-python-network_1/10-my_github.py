#!/usr/bin/python3
"""Python script that takes your GitHub credentials"""

if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get('https://api.github.com/user',
                     auth=('username', 'password'))
    user = r.json()
    print(user.get('id'))
