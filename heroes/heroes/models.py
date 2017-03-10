# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from utilities.models import TimeStampedModel


class Heroes(TimeStampedModel):
	GENDER_CHOICES = (
		('MALE', 'M'),
		('FEMALE', 'F'))
	hero_name = models.CharField(_("Hero name"), max_length=255, unique=True)
	real_name= models.CharField(_("Real name"), max_length=255)
	gender = models.CharField(
		_("Gender"),
		choices=GENDER_CHOICES,
		default='F',
		max_length=1)
	
	powers = models.ManyToManyField('Power')
	weaknesses = models.ManyToManyField('Weakness')
	api_pk = models.PositiveIntegerField(null=True)

	def __str__(self):
		return self.hero_name

	@property
	def power_list(self):
		return list(self.powers.values_list('name', flat=True))

	@property
	def weakness_list(self):
		return list(self.weaknesses.values_list('name', flat=True))


class Attributes(TimeStampedModel):
	hero = models.OneToOneField(Heroes, 
						        on_delete=models.CASCADE,
						        primary_key=True)
	intelligence = models.PositiveIntegerField(null=True)
	strength = models.PositiveIntegerField(null=True)
	speed = models.PositiveIntegerField(null=True)
	durability = models.PositiveIntegerField(null=True)
	power = models.PositiveIntegerField(null=True)
	combat = models.PositiveIntegerField(null=True)

	def __str__(self):
		return '{0} attr'.format(self.hero)


class Power(TimeStampedModel):
	name = models.CharField(_("Name"), max_length=255, unique=True)

	def __str__(self):
		return self.name

class Weakness(TimeStampedModel):
	name = models.CharField(_("Name"), max_length=255, unique=True)

	def __str__(self):
		return self.name
