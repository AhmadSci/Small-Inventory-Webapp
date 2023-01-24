from django import forms

class ItemForm(forms.Form):
    name = forms.CharField(label='Item name',max_length=200,widget = forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Item Name'}))
    quantity = forms.IntegerField(label='Quantity', widget = forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Item Quantity'}))
    price = forms.DecimalField(label='Price',max_digits=10, decimal_places=2, widget = forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Item Price'}))
    description = forms.CharField(label='Description', max_length=500, widget = forms.Textarea(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Item Description'}))

class UpdateItemForm(forms.Form):
    quantity = forms.IntegerField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)