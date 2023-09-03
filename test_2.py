
import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)
    username = data['username']
    password = data['password']
    url = data['url']
    url1 = data['url1']


def token_auth(token):
    response = requests.get(url=url1, headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
    content_var = [item['content'] for item in response.json()['data']]
    return content_var


def test_step2(login):
    assert 'ContentNew' in token_auth(login)


def test_step3(post_post):
    assert 'Описание' in post_post


