from django import forms

from recipes.recipes_app.models import Recipe


class RecipeFormBase(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class CreateRecipeForm(RecipeFormBase):
    # def clean_ingredients(self):
    #     value = self.cleaned_data['ingredients'].split(', ')
    #     pass
    pass


class EditRecipeForm(RecipeFormBase):
    pass


class DeleteRecipeForm(RecipeFormBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

    # def save(self, commit=True):
    #     self.instance.delete()
    #     return self.instance
