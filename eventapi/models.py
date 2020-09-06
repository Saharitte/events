from django.db import models


from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.conf import settings



PARTICIPATION_STATUSES = (
    (0, 'No, thanks'),
    (1, 'I may attend'),
    (2, 'I\'ll be there'),
)


class Event(models.Model):
    title = models.CharField( max_length=200)
    location = models.CharField( max_length=200)
    description = RichTextField()
    organizers = models.ManyToManyField(
    settings.AUTH_USER_MODEL, related_name='organized_events', verbose_name='organizers' )
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through='Participation', related_name='in_events', verbose_name='participants')

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['-start_datetime']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', args=[self.pk])



class Participation(models.Model):
    event = models.ForeignKey(Event, verbose_name='event', related_name='event_participations',on_delete=models.PROTECT )
    person = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='person', related_name='person_participations',on_delete=models.PROTECT)
    status = models.PositiveIntegerField(
        'participation status', choices=PARTICIPATION_STATUSES)
    date_registered = models.DateTimeField(
        'date registered', auto_now_add=True)

    def __str__(self):
        return '{} - {} ({})'.format(self.person, self.event, self.get_status_display())


class Participant(AbstractUser):
    location = models.CharField('location', max_length=200, blank=True)
    website = models.URLField('website', blank=True)
    bdate = models.DateField('birthday date', blank=True, null=True)

    class Meta:
        verbose_name = "Participant"
        verbose_name_plural = "Participants"

    def get_absolute_url(self):
        return reverse('account_profile', args=[self.pk, self.username])


