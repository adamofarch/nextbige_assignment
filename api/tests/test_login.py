import pytest
from rest_framework.test import APIClient
from api.models import User
from rest_framework.authtoken.models import Token

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_and_use_test_user():
    return User.objects.create_user(username='testuser', password='test', email='test@token.com')

@pytest.mark.django_db
def test_login(api_client, create_and_use_test_user):
    """TestCase for the /api/login/ endpoint"""
    assert User.objects.filter(username='testuser').exists()
    request_data = {'username': 'testuser', 'password': 'test'}
    response = api_client.post('/api/login/', data=request_data, format='json')
    assert response.status_code == 200 and 'token' in response.data

