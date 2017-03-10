# -*- coding: utf-8 -*-
from .models import *


def create_from_dict(_dict):
	for hero in _dict:
		_create_from_dict(hero)

def _create_from_dict(hero):
	gender = hero['gender']
	if gender == 'Male':
		gender = 'M'
	else:
		gender = 'F'

	powers = []
	for power in hero.get('powers', None):
		_p = str(power).lower()
		p, created = Power.objects.get_or_create(name=_p)
		powers += [p]

	weaknesses = []
	for weakness in hero.get('weaknesses', None):
		_w = str(weakness).lower()
		w, created = Weakness.objects.get_or_create(name=_w)
		weaknesses += [w]

	hero_name = hero['hero_name']
	h, created = Heroes.objects.update_or_create(
		hero_name=hero_name.lower(),
		defaults={
					'api_pk': int(hero.get('id', '0')),
					'real_name': hero['real_name'].lower(),
					'hero_name': hero['hero_name'].lower(),
					'gender': gender})

	Attributes.objects.update_or_create(
		hero=h,
		defaults={
			'combat':hero['attributes'].get('combat', None),
        	'durability':hero['attributes'].get('durability', None),
        	'intelligence':hero['attributes'].get('intelligence', None),
        	'power':hero['attributes'].get('power', None),
        	'strength':hero['attributes'].get('strength', None),
        	'speed':hero['attributes'].get('speed', None)})


	for power in powers:
		h.powers.add(power)

	for weakness in weaknesses:
		h.weaknesses.add(weakness)