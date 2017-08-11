from django.forms import ModelForm
from hero.models import Group


class GroupForm(ModelForm):
    """

    """
    class Meta():
        model = Group
        fields = ['name', 'rule_version', 'game_master', 'players',
                  'description']
