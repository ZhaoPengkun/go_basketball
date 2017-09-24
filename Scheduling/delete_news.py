import requests


def delete(delete_url):
    requests.delete(delete_url)

if __name__ == "__main__":
    url = "http://localhost:8088/api/v1/news/"
    delete(url)
