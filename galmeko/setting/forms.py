from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from setting.models import Vehicle,VehicleCategory


class CustomVehicleCreationForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ('vehicle_no','chassis_no',)

class CustomCategoryCreationForm(forms.ModelForm):

    class Meta:
        model = VehicleCategory
        fields = ('category_name','status',)
