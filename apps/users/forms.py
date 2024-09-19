from django.contrib.auth.models import User
from core.forms import BaseModelForm


class UserUpdateForm(BaseModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
