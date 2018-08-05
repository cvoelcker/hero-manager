from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Group(models.Model):
    """
    The group is a couple of characters and players regularly playing with each
    other
    """

    name = models.CharField(
        max_length=200,
        primary_key=True,
        unique=True
    )

    rule_version = models.CharField(
        max_length=20,
        choices=xml_hero.RULES_SUPPORTED,
        default='DEFAULT',
    )

    game_master = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='gaming_group_master'
    )

    players = models.ManyToManyField(
        User,
        related_name='gaming_group'
    )

    description = models.CharField(max_length=140)

    def __str__(self):
        return self.name

    def has_charsheets(self):
        return xml_hero.has_charsheet(self.rule_version)


class Hero(models.Model):
    """
    The hero represents a player character in a playing group. It needs to
    be owned by a player.
    """

    class Meta:
        unique_together = ('group', 'name')

    name = models.CharField(max_length=200)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    char_sheet = models.FileField(
        null=True,
        blank=True
    )

    def clean(self):
        if self.player not in self.group.players.all():
            raise ValidationError(
                {'group':
                 'The given player is not part of the group'})

    def __str__(self):
        return self.name

    def get_char_sheet(self):
        return xml_hero.get_hero(self.group.rule_version, self.char_sheet)



class Adventure(models.Model):
    """

    """

    class Meta:
        unique_together = ('group', 'name')

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    ongoing = models.BooleanField(default=False)

    name = models.CharField(max_length=200)

    date_started = models.DateField(default=timezone.now)

    description = models.TextField()

    def __str__(self):
        return self.name


class DiaryEntry(models.Model):
    """
    An entry into a diary
    """

    class Meta:
        unique_together = ('adventure', 'order')
        ordering = ('adventure', 'order')

    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    adventure = models.ForeignKey(Adventure, on_delete=models.SET_NULL,
                                  null=True)
    date_registered = models.DateTimeField(
        'date added',
        default=timezone.now)
    name = models.CharField(max_length=200)
    date = models.CharField('in game date', max_length=200)

    order = models.IntegerField()

    entry = models.TextField('entry')

    # def clean(self):
    #    if self.hero not in self.adventure.group.hero_set.all():
    #        raise ValidationError(
    #            {'hero': 'The hero ' + self.hero +
    #                     ' does not participate in the daventure ' +
    #                     self.adventure})

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "{}: {} {}".format(
                str(self.adventure),
                str(self.hero),
                self.date
            )


class NSCGroup(models.Model):
    """
    Models a group of NSCs united by concurrent
    """

    class Meta:
        unique_together = ('adventure', 'name')

    group = models.ForeignKey(Group)

    name = models.TextField()
    description = models.TextField()

    color = models.CharField(max_length=7)


class NSC(models.Model):
    """

    """

    name = models.TextField()
    description = models.TextField()

    groups = models.ManyToManyField(NSCGroup)
