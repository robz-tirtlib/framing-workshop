from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from workshopapp.models import Feedback
from workshopapp.forms import FeedbackForm


def get_contacts_response(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return get_contacts_get_response(request)
    return get_contacts_post_response(request)


def get_contacts_get_response(request: HttpRequest) -> HttpResponse:
    context = {"form": FeedbackForm()}
    return render(request, "workshopapp/contacts.html", context)


def get_contacts_post_response(request: HttpRequest) -> HttpResponse:
    form = FeedbackForm(request.POST)

    if form.is_valid():
        feedback = Feedback(
            name=form.cleaned_data.get("name"),
            email=form.cleaned_data.get("email"),
            text=form.cleaned_data.get("text"),
            )
        feedback.save()
        return render(request, "workshopapp/contacts.html")
    return render(request, "workshopapp/contacts.html", {"form": form})
