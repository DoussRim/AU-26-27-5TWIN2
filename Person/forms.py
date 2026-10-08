from django.contrib.auth.forms import UserCreationForm
from .models import Person
class FormRegistration(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Person
        # fields="__all__"
        
        fields=('cin','username','email')
        