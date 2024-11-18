import pytest
from rest_framework.test import APIClient
from api.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_register_user(api_client):
    """TestCase for the /api/register endpoint"""

    request_data = {
        'username': 'testuser1',
        'password': 'test',
        'email': 'test@nextbige.com',
        'first_name': 'testy',
        'date_of_birth': '1999-07-01', 
        'phone_number': '+91 8123456789'
    }
    
    count_before_request = User.objects.all().count()
    assert count_before_request == 0
    response = api_client.post('/api/register/', data=request_data, format='json')
    count_after_request = User.objects.all().count()
    print(response.status_code, response.data)
    assert count_after_request == count_before_request + 1 and User.objects.filter(username=request_data['username']).exists()


