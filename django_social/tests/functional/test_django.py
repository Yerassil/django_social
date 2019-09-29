from lxml import html


def test_django(client, db):
    response = client.get('/')
    assert response.status_code == 200


def test_user_not_logged_in(client, db):
    response = client.get('/')
    assert response.status_code == 200
    response = response.content.decode('utf-8')
    response = html.fromstring(response)

    a = response.cssselect(
        'body > div > nav > a'
    )
    assert 'Hi, please log in :)' in a[0].text
    assert 'welcome to the Social Stuff' not in a[0].text


def test_login(client, db, data):
    user = data
    response = client.post(
        'login/',
        {'username': 'user', 'password': 'useruser'}
    )
    login = client.login(username='user', password='useruser')
    assert login is True
    assert user.is_authenticated is True
    response = client.get('/')
    response = response.content.decode('utf-8')
    response = html.fromstring(response)
    a = response.cssselect(
        'body > div > nav > a'
    )
    assert 'welcome to the Social Stuff' in a[0].text
