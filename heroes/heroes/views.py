# # -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json

from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect

from .models import *
from .forms import HeroForm, MergeForm, CreateForm
from .functions import _create_from_dict


def index(request):
    heroes = Heroes.objects.all()
    context = {
        'heroes': heroes
    }
    template = 'heroes.html'
    return render(request, template, context)


def create(request):
    '''
    Create a new hero
    '''
    template = 'create.html'
    context = {}

    form = CreateForm()
    weaknesses = Weakness.objects.values_list('name', flat=True)
    powers = Power.objects.values_list('name', flat=True)

    w_choices = [(weakness,weakness) for weakness in weaknesses]
    form.fields['weaknesses'].choices = w_choices

    p_choices = [(power,power) for power in powers]
    form.fields['powers'].choices = p_choices

    context.update({'form': form})
    if request.method == 'GET':
        return render(request, template, context)

    form = CreateForm(request.POST)
    form.fields['weaknesses'].choices = w_choices
    form.fields['powers'].choices = p_choices
    if form.is_valid():
        data = form.cleaned_data
        data['attributes'] = {}
        if data['combat']:
            data['attributes'].update({'combat': data['combat']})
            data.pop('combat')
        if data['intelligence']:
            data['attributes'].update({'intelligence': data['intelligence']})
            data.pop('intelligence')
        if data['strength']:
            data['attributes'].update({'strength': data['strength']})
            data.pop('strength')
        if data['speed']:
            data['attributes'].update({'speed': data['speed']})
            data.pop('speed')
        if data['durability']:
            data['attributes'].update({'durability': data['durability']})
            data.pop('durability')
        if data['power']:
            data['attributes'].update({'power': data['power']})
            data.pop('power')

        data['gender'] = 'M'
        _create_from_dict(data)
        return redirect('home')
    context.update({'form': form})
    return render(request, template, context)

def merge(request):
    '''
    Merge two existing heroes
    '''
    heroes = Heroes.objects.all()
    context = {'heroes': heroes}
    template = 'merge.html'

    if request.method == 'GET':
        context.update({'form': HeroForm()})
    else:
        form = HeroForm(request.POST)
        if form.is_valid():
            # redirect
            return redirect('merge_heroes', hero1=form.cleaned_data['hero1'], hero2=form.cleaned_data['hero2'])
        context.update({'form': form})
    return render(request, template, context)

def merge_heroes(request, hero1, hero2):
    hero1 = Heroes.objects.get(hero_name=hero1)
    hero2 = Heroes.objects.get(hero_name=hero2)
    
    form = MergeForm()

    weaknesses = hero1.weakness_list + hero2.weakness_list

    qs = hero1.power_list + hero2.power_list
    p_choices = [(power,power) for power in qs]
    form.fields['powers'].choices = p_choices

    combats = [hero1.attributes.combat, hero2.attributes.combat]
    intelligences = [hero1.attributes.intelligence, hero2.attributes.intelligence]
    strengths = [hero1.attributes.strength, hero2.attributes.strength]
    speeds = [hero1.attributes.speed, hero2.attributes.speed]
    durabilities = [hero1.attributes.durability, hero2.attributes.durability]
    a_power = [hero1.attributes.power, hero2.attributes.power]

    form.fields['combat'].choices = [(str(combat), str(combat)) for combat in combats]
    form.fields['intelligence'].choices = [(str(intelligence), str(intelligence)) for intelligence in intelligences]
    form.fields['strength'].choices = [(str(strength), str(strength)) for strength in strengths]
    form.fields['speed'].choices = [(str(speed), str(speed)) for speed in speeds]
    form.fields['durability'].choices = [(str(durability), str(durability)) for durability in durabilities]
    form.fields['power'].choices = [(str(power), str(power)) for power in a_power]

    context = {'form': form}
    template = 'mergeform.html'

    if request.method == 'GET':
        return render(request, template, context)

    form = MergeForm(request.POST)
    form.fields['powers'].choices = p_choices
    form.fields['combat'].choices = [(str(combat), str(combat)) for combat in combats]
    form.fields['intelligence'].choices = [(str(intelligence), str(intelligence)) for intelligence in intelligences]
    form.fields['strength'].choices = [(str(strength), str(strength)) for strength in strengths]
    form.fields['speed'].choices = [(str(speed), str(speed)) for speed in speeds]
    form.fields['durability'].choices = [(str(durability), str(durability)) for durability in durabilities]
    form.fields['power'].choices = [(str(power), str(power)) for power in a_power]

    if form.is_valid():
        data = form.cleaned_data
        data['attributes'] = {}
        if data['combat']:
            data['attributes'].update({'combat': int(data['combat'][0])})
            data.pop('combat')
        if data['intelligence']:
            data['attributes'].update({'intelligence': int(data['intelligence'][0])})
            data.pop('intelligence')
        if data['strength']:
            data['attributes'].update({'strength': int(data['strength'][0])})
            data.pop('strength')
        if data['speed']:
            data['attributes'].update({'speed': int(data['speed'][0])})
            data.pop('speed')
        if data['durability']:
            data['attributes'].update({'durability': int(data['durability'][0])})
            data.pop('durability')
        if data['power']:
            data['attributes'].update({'power': int(data['power'][0])})
            data.pop('power')

        data['weaknesses'] = weaknesses
        data['gender'] = 'M'
        _create_from_dict(data)
        return redirect('home')
    context.update({'form': form})
    return render(request, template, context)

