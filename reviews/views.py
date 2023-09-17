from django.shortcuts import render
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from .models import Review
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView
# Create your views here.
#class based:
'''class ReviewView(LoginRequiredMixin, FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    def form_valid(self, form) -> HttpResponse:
        form.save()
        return super().form_valid(form)'''
        
#funzionale:
@login_required
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = Review(author = request.user,
                            review_text = form.cleaned_data['review_text'],
                            title = form.cleaned_data['title'],
                            rating = form.cleaned_data['rating'])
            review.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
    "form" : form
    })
        
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Grazie per la tua recensione!"
        return context

class ReviewsListView(ListView):
    model = Review
    template_name = "reviews/review_list.html"
    context_object_name = "reviews"

class DetailListView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
 
    
