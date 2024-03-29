import urllib.request
import urllib.error
import sys


def fetch_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            return body
    except urllib.error.HTTPError as err:
        return 'Error code: {}'.format(err.code)


if __name__ == "__main__":
    url = sys.argv[1]
    response_body = fetch_url(url)
    print(response_body)
