from reporting.admin import UserCreationForm
from reporting import models


class UserAddForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ['email', 'role', 'password1', 'password2']
