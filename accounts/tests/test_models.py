import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


@pytest.mark.django_db  # Marks the test as using database
def test_create_user():
    User = get_user_model()

    # Create user
    user = User.objects.create_user(
        full_name='Test User',
        role='collector',
        email='testemail@mail.com',
        phone='+254724564321',
        location='Machakos',
        password='testpassword'
    )

    assert user.full_name == 'Test User'
    assert user.role == 'collector'
    assert user.email == 'testemail@mail.com'
    assert user.phone == '+254724564321'
    assert user.location == 'Machakos'
    assert user.is_active
    assert not user.is_staff
    assert user.check_password('testpassword')


@pytest.mark.django_db
def test_create_superuser():
    User = get_user_model()

    # Create superuser
    superuser = User.objects.create_superuser(
        full_name='Test Superuser',
        email='supertestemail@mail.com',
        phone='+254724564321',
        location='Machakos',
        password='testpassword'
    )
    assert superuser.is_staff
    assert superuser.is_superuser
    assert superuser.is_active
    assert superuser.role == 'admin'
    assert superuser.email == 'supertestemail@mail.com'
    assert superuser.phone == '+254724564321'
    assert superuser.location == 'Machakos'
    assert superuser.check_password('testpassword')


@pytest.mark.django_db
def test_add_user_invalid_email():
    User = get_user_model()
    with pytest.raises(ValueError):
        User.objects.create_user(
            full_name='Test User',
            role='collector',
            email='test',
            phone='+254724564321',
            location='Machakos',
            password='testpassword'
        )
