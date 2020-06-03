
from django import forms
from django.forms import ModelForm
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from .models import Profile

class UpdateProfileImgForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    
        


ACCOUNT_TYPE_CHOICES = [
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
    ('Bookseller', 'Boolseller')
]


class SignupForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Full name')
    account_type = forms.ChoiceField(label='Account Type',
                                     choices=ACCOUNT_TYPE_CHOICES)
    
    image = ProcessedImageField(default='default.png', upload_to='users/profile_images', processors=[ResizeToFill(300, 200)],
                                    format='JPEG', options={'quality': 95})

    def signup(self, request, user):
        profile = user.profile
        profile.full_name = self.cleaned_data['full_name']
        profile.account_type = self.cleaned_data['account_type']
        user.save()
        profile.save()


