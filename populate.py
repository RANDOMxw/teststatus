import random
from users.models import CustomUser
from contacts.models import Contact
from spam.models import SpamNumber

# Create users
for i in range(10):
    user = CustomUser.objects.create_user(
        username=f'user{i}',
        email=f'user{i}@example.com',
        phone_number=f'123456789{i}',
        password='password'
    )

# Create contacts
for i in range(50):
    user = random.choice(CustomUser.objects.all())
    contact = Contact.objects.create(
        user=user,
        name=f'Contact {i}',
        phone_number=f'987654321{i}'
    )

# Create spam numbers
for i in range(10):
    spam_number = SpamNumber.objects.create(
        phone_number=f'555123456{i}',
        spam_count=random.randint(1, 10)
    )
