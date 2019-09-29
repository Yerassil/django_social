import pytest
from datetime import datetime
from django_social.models import User

@pytest.fixture
def data():
    user = User.objects.create_user(
        username='user', password='useruser',
        first_name='first_name', last_name='last_name',
        birthday=datetime(1988, 3, 19)
    )
    return user
