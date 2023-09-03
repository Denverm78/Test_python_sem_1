import pytest
import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)
username = data['username']
password = data['password']
url = data['url']
url1 = data['url1']
user_token = data['user_token']


@pytest.fixture()
def login(username1=username, password1=password):
    obj_data = requests.post(url=url, data={'username': username1, 'password': password1})
    token = obj_data.json()['token']
    return token


@pytest.fixture()
def post_post():
    obj_data = requests.post(url=url1, headers={"X-Auth-Token": user_token}, data={
        'username': 'Roman83',
        'password': '5a45102d64',
        'title': 'Название',
        'description': 'Описание',
        'content': 'Содержимое'
    })
    return obj_data.json()['description']
