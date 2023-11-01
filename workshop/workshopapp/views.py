from django.http import Http404, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Frame, Review


def index(request):
    frames = Frame.objects.all()[:10]
    context = {
        "frames": frames,
    }

    return render(request, "workshopapp/index.html", context)


def frame(request, frame_id: int):
    try:
        frame = Frame.objects.get(id=frame_id)
    except Frame.DoesNotExist:
        raise Http404(f"Frame with id={frame_id} not found.")

    if request.method == "GET":
        reviews = Review.objects.filter(frame=frame_id).order_by("-created_at")
        context = {
            "frame": frame,
            "reviews": reviews,
        }

        return render(request, "workshopapp/frame.html", context)
    elif request.method == "POST":
        review_content = request.POST["review_content"]

        if review_content:
            review_obj = Review(content=review_content, frame=frame)
            review_obj.save()

        kw = {"frame_id": frame_id}
        return redirect(reverse("workshopapp:frame", kwargs=kw))

    return HttpResponseNotAllowed(["GET", "POST"])
