from django.forms import (
    Form, ModelForm, BaseForm,
    Field,
    CharField, URLField, ChoiceField, Textarea,
    IntegerField, RadioSelect, BooleanField,
    ValidationError
)

class ArticleForm(Form):
    annotation = CharField(widget=Textarea(), label="Anotace")
    content = CharField(widget=Textarea(), label="Obsah")
