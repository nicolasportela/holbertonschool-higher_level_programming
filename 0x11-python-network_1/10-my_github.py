#!/usr/bin/python3
"""Python script that takes your GitHub credentials"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    user = r.json()
    print(user.get('id'))
