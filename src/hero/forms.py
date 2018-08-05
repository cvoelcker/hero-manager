from django.contrib.auth.models import User
from django.forms import ModelForm, Form, ModelChoiceField, FileField
from .models import Group, Hero


class GroupForm(ModelForm):
    """

    """

    class Meta:
        model = Group
        fields = ['name', 'rule_version', 'players',
                  'description']


class HeroAddForm(ModelForm):
    """

    """

    class Meta:
        model = Hero
        fields = ['name', 'char_sheet', 'player', 'group']

    def __init__(self, *args, **kwargs):
        player = kwargs.pop('player', None)
        group = kwargs.pop('group', None)
        super(HeroAddForm, self).__init__(*args, **kwargs)
        self.initial['player'] = player
        self.initial['group'] = group
        print(self.fields)


class CharsheetUploadForm(Form):
    """

    """

    charsheet = FileField()
