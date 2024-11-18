import pytest
from rest_framework.authtoken.models import Token
from api.models import User
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user_with_token():
    user = User.objects.create_user(username='testuserwithtoken', password='test', email='testwithtoken@nextbige.com')
    token, created = Token.objects.get_or_create(user=user)
    return user, token

@pytest.mark.django_db
def test_profile_unauthorized(api_client, create_user_with_token):
    """ TestCase for checking the unauthorized access validation for /api/profile/ endpoint """
    actual_token = Token.objects.get(user__username='testuserwithtoken')
    fake_token = '6KBb9Gq7GFeZSASpNlca7kwEKHeLVj'
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + fake_token)
    response = api_client.get('/api/profile/')

    print(response.data, response.status_code)
    assert response.status_code == 401

@pytest.mark.django_db    
def test_profile_authorized(api_client, create_user_with_token):
    """ TestCase for checking the unauthorized access validation for /api/profile/ endpoint """
    token = Token.objects.get(user__username='testuserwithtoken')
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    response = api_client.get('/api/profile/')
    print(response.data)
    assert response.status_code == 200 and response.data['profile']['username'] == 'testuserwithtoken'


