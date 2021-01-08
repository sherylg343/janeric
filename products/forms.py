from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Product_Family


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        model = Product_Family
        model = Category
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        cat_names = [(c.id, c.get_name()) for c in categories]
        div_names = [(c.id, c.get_division()) for c in categories]
        product_families = Product_Family.objects.all()
        pf_names = [(pf.id, pf.get_name()) for pf in product_families]
        brand_names = [(pf.id, pf.get_brand_name()) for pf in product_families]

        self.fields['category'].choices = cat_names
        self.fields['division'].choices = div_names
        self.fields['product_family'].choices = pf_names
        self.fields['brand_name'].choices = brand_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-border rounded-0'

