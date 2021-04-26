from django.contrib.auth.models import User

# Create user and save to the database
user = User.objects.create_user('qays', 'qays.shreda@gmail.com', 'mypassword')

# Update fields and then save again
user.first_name = 'Qais '
user.last_name = 'Shreda'
user.save()