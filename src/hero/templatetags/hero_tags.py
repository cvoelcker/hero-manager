from django import template
from models import Group

register = template.Library()

@register.simple_tag
def hero_set(player, group):
    return player.hero_set.filter(group=group)

@register.simple_tag
def groups(user):
    return Group.objects.filter(player=user).all()
