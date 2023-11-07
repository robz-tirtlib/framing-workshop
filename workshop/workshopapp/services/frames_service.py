from django.http import (
    Http404, HttpRequest, HttpResponse, HttpResponseNotAllowed)
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User

from workshopapp.models import Frame, Review, Feedback
from workshopapp.forms import FeedbackForm


def get_frame_response(request: HttpRequest, frame_id: int) -> HttpResponse:
    if request.method not in ["GET", "POST"]:
        return HttpResponseNotAllowed(["GET", "POST"])

    frame = get_frame(frame_id=frame_id)

    if request.method == "GET":
        return get_frame_get_response(request, frame)

    review_content = request.POST.get("review_content")
    return get_frame_post_response(review_content, frame, request.user)


def get_frame(frame_id: int) -> Frame | None:
    try:
        frame = Frame.objects.get(id=frame_id)
    except Frame.DoesNotExist:
        raise Http404(f"Frame with id={frame_id} not found.")
    return frame


def get_frame_get_response(
        request: HttpRequest,
        frame: Frame) -> HttpResponse:
    reviews = Review.objects.filter(
        frame=frame.id).order_by("-created_at")
    context = {
        "frame": frame,
        "reviews": reviews,
    }
    return render(request, "workshopapp/frame.html", context)


def get_frame_post_response(
        review_content: str,
        frame: Frame,
        user: User) -> HttpResponse:
    review_obj = Review(content=review_content, frame=frame)

    if user.is_authenticated:
        review_obj.author = user
    review_obj.save()

    kw = {"frame_id": frame.id}
    return redirect(reverse("workshopapp:frame", kwargs=kw))


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
