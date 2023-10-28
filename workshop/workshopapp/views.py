from django.http import Http404
from django.shortcuts import render

from .models import Frame


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

    context = {
        "frame": frame,
    }

    return render(request, "workshopapp/frame.html", context)
