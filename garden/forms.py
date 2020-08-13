from django import forms


# add a new project
class addProject(forms.Form):
    time = forms.CharField(label="time",
                           max_length=100,
                           widget=forms.TextInput(attrs={
                               'placeholder': 'YYYY (MM)',
                               'id': 'timeInp'
                           }))

    title = forms.CharField(
        label="title",
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'eg. MCM Competition',
            'id': 'titleInp',
        }))

    description = forms.CharField(
        label="description",
        max_length=1000,
        widget=forms.TextInput(
            attrs={
                'placeholder':
                'eg. Build a mathematical model after Analyzing',
                'id': 'descriptionInp'
            }))

    role1 = forms.CharField(label="role1",
                            max_length=100,
                            widget=forms.TextInput(attrs={'id': 'role1Inp'}))

    role2 = forms.CharField(label="role2",
                            max_length=100,
                            widget=forms.TextInput(attrs={'id': 'role2Inp'}))


# add a new education
class addEducation(forms.Form):
    start = forms.CharField(label='start',
                            max_length=100,
                            widget=forms.TextInput(attrs={
                                'placeholder': 'YYYY.MM',
                                'id': 'startInp'
                            }))

    end = forms.CharField(label='end',
                          max_length=100,
                          widget=forms.TextInput(attrs={
                              'placeholder': 'YYYY.MM (present)',
                              'id': 'endInp'
                          }))

    uni = forms.CharField(
        label='uni',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'eg. University of Birmingham',
            'id': 'uniInp'
        }))

    major = forms.CharField(
        label='major',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'eg. BSc Computer Science',
            'id': 'majorInp'
        }))

    perform = forms.CharField(
        label='perform',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'eg. 1st class degree',
            'id': 'performInp'
        }))

    module = forms.CharField(
        label='module',
        max_length=1000,
        widget=forms.TextInput(attrs={
            'placeholder': 'eg. Machine Learning',
            'id': 'moduleInp'
        }))


# add a new interest
class addInterest(forms.Form):
    title = forms.CharField(
        label='title',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'eg. Travel and Photographing',
            'id': 'titleInp'
        }))

    description = forms.CharField(
        label='description',
        max_length=1000,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'eg. I love having trips to a new place.',
                'id': 'descriptionInp'
            }))


# add a new interest
class userValidation(forms.Form):
    user = forms.CharField(label='user',
                           max_length=100,
                           widget=forms.TextInput(attrs={'id': 'userInp'}))

    password = forms.CharField(
        label='Password',
        max_length=100,
        widget=forms.PasswordInput(attrs={'id': 'passwordInp'}))
