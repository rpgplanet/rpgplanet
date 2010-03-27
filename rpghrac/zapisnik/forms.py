# -*- coding: utf-8 -*-

from django.forms import (
    Form, ModelForm, BaseForm,
    Field,
    CharField, URLField, ChoiceField, Textarea,
    IntegerField, RadioSelect, BooleanField,
    ValidationError
)

class ArticleForm(Form):
    title = CharField(label=u"Název")
    annotation = CharField(widget=Textarea(), label=u"Anotace")
    content = CharField(widget=Textarea(), label=u"Obsah")
    tags = CharField(label=u"Nálepky (oddělené mezerami nebo čárkami)", max_length=255)
