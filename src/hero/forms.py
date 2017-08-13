from django.forms import ModelForm, Form, forms
from .models import Group, Hero


class GroupForm(ModelForm):
    """

    """

    class Meta():
        model = Group
        fields = ['name', 'rule_version', 'game_master', 'players',
                  'description']


class HeroAddForm(ModelForm):
    """

    """

    class Meta():
        model = Hero
        fields = ['name', 'player', 'group', 'char_sheet', ]

class CharsheetUploadForm(Form):
    """

    """

    charsheet = forms.FileField()