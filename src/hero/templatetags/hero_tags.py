from django import template

register = template.Library()


@register.simple_tag
def hero_set(player, group):
    return player.hero_set.filter(group=group)
