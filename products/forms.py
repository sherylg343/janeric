from django import forms
from .models import Product, Category, Product_Family


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            categories = Category.ovjects.all()
            cat_names = [(c.id, c.get_name()) for c in categories]
            product_families = Product_Family.objects.all()
            pf_names = [(pf.id, pf.get_name()) for pf in product_families]

            self.fields['category'].choices = name
            self.fields['product_family'] = name
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-border rounded-0'
