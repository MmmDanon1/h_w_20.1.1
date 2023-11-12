from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'image', 'price',)

        def clean_name(self):
            stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                         'радар']
            cleaned_data = self.cleaned_data.get('name')

            for item in stop_list:
                if item in cleaned_data:
                    raise forms.ValidationError(f'Слово "{item}" запрещено к использованию, выберите другое')

            return cleaned_data

        def clean_description(self):
            stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                         'радар']
            cleaned_data = self.cleaned_data.get('description')

            for item in stop_list:
                if item in cleaned_data:
                    raise forms.ValidationError(f'Слово "{item}" запрещено к использованию, выберите другое')

            return cleaned_data
