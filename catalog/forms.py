from django.db.models import BooleanField
from django.forms import ModelForm, forms
from .models import Product
from django.core.exceptions import ValidationError


class StyleFormMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    BANNED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


    class Meta:
        model = Product
        fields = ('name', 'description', 'images', 'category', 'price')

    def clean_name(self):
        name = self.cleaned_data['name']
        name_lower = name.lower()
        for word in self.BANNED_WORDS:
            if word in name_lower:
                raise forms.ValidationError(f"Название содержит запрещенное слово: '{word}'.")
        return name


    def clean_description(self):
        description = self.cleaned_data['description']
        description_lower = description.lower()

        for word in self.BANNED_WORDS:
            if word in description_lower:
                raise forms.ValidationError(f"Описание содержит запрещенное слово: '{word}'.")
        return description

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError(f"цена не может быть отрицательной.")
        return price


