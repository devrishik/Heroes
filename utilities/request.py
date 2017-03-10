import json
import requests

from django.conf import settings

from .models import Token


def check_token(token):
	resp = requests.get(settings.HEROES_URL.format(token))
	if resp.status_code == 404:
		return False
	return True

def new_token():
	resp = requests.get(settings.GET_API_KEY_URL)
	resp = json.loads(resp.content)
	try:
		return resp['apiKey']
	except KeyError:
		return ''

def get_token():
	'''
	Utility to get the current unexpired token
	If expired, it fetches a new one.
	'''
	try:
		token = Token.objects.get(pk=1)
		if not check_token(token):
			token.token = new_token()
			token.save()
	except Token.DoesNotExist:
		_token = new_token()
		token = Token.objects.create(token=_token)

	return token

def get_heroes():
	'''
	Function to fetch all the heroes
	'''
	token = get_token()
	resp = requests.get(settings.HEROES_URL.format(token.token))
	d_resp = json.loads(resp.content)

	from heroes.heroes.functions import create_from_dict
	if resp.status_code == 200:
		create_from_dict(d_resp)


def post_hero(hero):
	'''
	function to post a new hero to the API
	'''
	token = get_token()

	from heroes.heroes.serializers import HeroSerializer

	serializer = HeroSerializer(hero)

	resp = requests.post(setttings.HEROES_URL.format(token.token),
						data=serializer.data)

	if resp.status_code == 201:
		return True
	return False
