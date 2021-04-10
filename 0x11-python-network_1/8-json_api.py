#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter"""

if __name__ == "__main__":
    import requests
    import sys

    if not argv[1]:
        letter = ""
    else:
        letter = sys.argv[1]
    dic = {'q': letter}
    r = requests.post("http://0.0.0.0:5000/search_user", data=dic)
    try:
        result = r.json()
        if 'id' in result and 'name' in result:
            print("[{}] {}" .format(result['id'], result['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
