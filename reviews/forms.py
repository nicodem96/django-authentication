from django import forms
from .models import Review
'''class ReviewForm(forms.Form):
    user_name = forms.CharField(label = "Il tuo nome", max_length=50, error_messages={
        "required" : "Questo campo è obbligatorio",
        "max_length" : "Per favore inserisci un nome piu corto!"
    })
    title = forms.CharField(label = "Titolo")
    review_text = forms.CharField(label = "Il tuo feedback", widget=forms.Textarea,
                                  max_length=200)
    rating = forms.IntegerField(label = "Il tuo Rating", min_value=1, max_value=10)
# alternativa al creare un form e un modello separati è utilizzare la classe modelForm che popola automaticamente
# il database con gli stessi campi del form'''

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['author']
        labels = {
            "title" : "Titolo",
            "review_text" : "Il tuo feedback",
            "rating" : "Il tuo rating",
        }
        error_messages = {
            "title" : {
                "required" : "Questo campo è obbligatorio",
                "max_length" : "Per favore inserisci un nome piu corto!"
            }
        }