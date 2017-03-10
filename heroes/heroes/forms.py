from django import forms

from .models import Heroes, Power

class HeroForm(forms.Form):
    hero1 = forms.CharField(label='Hero1 Name')
    hero2 = forms.CharField(label='Hero2 Name')

    def clean_hero1(self):
        form_hero1 = self.cleaned_data.get("hero1")
        existing = Heroes.objects.filter(
                       hero_name=form_hero1.lower()
                   ).exists()
        if not existing:
            raise forms.ValidationError(u"%(name)s Does not exist",
                code='invalid',
                params={'name': str(form_hero1)})

        return form_hero1

    def clean_hero2(self):
        form_hero2 = self.cleaned_data.get("hero2")
        existing = Heroes.objects.filter(
                       hero_name=form_hero2.lower()
                   ).exists()
        if not existing:
            raise forms.ValidationError(u"%(name)s Does not exist",
                code='invalid',
                params={'name': str(form_hero2)})

        return form_hero2

class CreateForm(forms.Form):
    hero_name = forms.CharField(required=True)
    real_name = forms.CharField(required=True)

    powers = forms.MultipleChoiceField(choices=(), required=False, widget=forms.CheckboxSelectMultiple())
    weaknesses = forms.MultipleChoiceField(choices=(), required=False, widget=forms.CheckboxSelectMultiple())

    # Attributes
    intelligence = forms.IntegerField(min_value=0, max_value=100)
    strength = forms.IntegerField(min_value=0, max_value=100)
    speed = forms.IntegerField(min_value=0, max_value=100)
    durability = forms.IntegerField(min_value=0, max_value=100)
    power = forms.IntegerField(min_value=0, max_value=100)
    combat = forms.IntegerField(min_value=0, max_value=100)
    



class MergeForm(forms.Form):
    hero_name = forms.CharField(required=True)
    real_name = forms.CharField(required=True)

    powers = forms.MultipleChoiceField(choices=(), required=False, widget=forms.CheckboxSelectMultiple())

    # Attributes
    intelligence = forms.MultipleChoiceField(choices=(), required=False, widget=forms.CheckboxSelectMultiple())
    strength = forms.MultipleChoiceField(choices=(), required=False, widget=forms.CheckboxSelectMultiple())
    speed = forms.MultipleChoiceField(choices=(), required=False, widget=forms.CheckboxSelectMultiple())
    durability = forms.MultipleChoiceField(choices=(), required=False, widget=forms.CheckboxSelectMultiple())
    power = forms.MultipleChoiceField(choices=(), required=False, widget=forms.CheckboxSelectMultiple())
    combat = forms.MultipleChoiceField(choices=(), required=False, widget=forms.CheckboxSelectMultiple())

    def clean_powers(self):
        value = self.cleaned_data['powers'] 
        if len(value) > 5: 
            raise forms.ValidationError("You can't select more than 5 powers") 
        return value 

    def clean_intelligence(self):
        value = self.cleaned_data['intelligence'] 
        if len(value) > 1: 
            raise forms.ValidationError("You can't select more than 1 intelligence") 
        return value 

    def clean_strength(self):
        value = self.cleaned_data['strength'] 
        if len(value) > 1: 
            raise forms.ValidationError("You can't select more than 1 strength") 
        return value 

    def clean_speed(self):
        value = self.cleaned_data['speed'] 
        if len(value) > 1: 
            raise forms.ValidationError("You can't select more than 1 speed") 
        return value 

    def clean_durability(self):
        value = self.cleaned_data['durability'] 
        if len(value) > 1: 
            raise forms.ValidationError("You can't select more than 1 durability") 
        return value 

    def clean_power(self):
        value = self.cleaned_data['power'] 
        if len(value) > 1: 
            raise forms.ValidationError("You can't select more than 1 power") 
        return value 

    def clean_combat(self):
        value = self.cleaned_data['combat'] 
        if len(value) > 1: 
            raise forms.ValidationError("You can't select more than 1 combat") 
        return value 