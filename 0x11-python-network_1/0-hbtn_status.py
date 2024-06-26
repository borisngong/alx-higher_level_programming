#!/usr/bin/python3
"""
A Python script responsible for fetching https://alx-intranet.hbtn.io/status
"""

url = 'https://alx-intranet.hbtn.io/status'

if __name__ == '__main__':

    import urllib.request

    with urllib.request.urlopen(url) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
