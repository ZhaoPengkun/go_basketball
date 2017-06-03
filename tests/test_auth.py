from requests import post
from test_config import host_url


def test_register():
    url = host_url + "/auth/register"
    print url
    params = {'email': 'zhao_pengkun@foxmail.com', 'password': '123456'}
    r = post(url, params=params)
    print r.text


def test_login():
    url = host_url + "/auth/login"
    print url
    params = {'email': 'zhao_pengkun@foxmail.com', 'password': '12345'}
    r = post(url, params=params)
    print r.text

if __name__ == "__main__":
    test_login()
