from django.contrib import admin

# Creating a user programmatically
from django.contrib.auth.models import User

try:
    # Create a new user with a unique username
    user = User.objects.create_user(username='unique_username', email='user@example.com', password='password123')
    print("User created successfully!")
except Exception as e:
    print("Error creating user:", e)
