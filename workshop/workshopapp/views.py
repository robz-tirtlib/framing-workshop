from django.shortcuts import render
from django.core.paginator import Paginator

from .services.frames_service import get_frame_response
from .services.contacts_service import get_contacts_response

from .models import Frame


def index(request):
    return render(request, "workshopapp/index.html")


def frames(request):
    _frames = Frame.objects.all()
    paginator = Paginator(_frames, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "workshopapp/frames.html", {"page_obj": page_obj})


def frame(request, frame_id: int):
    return get_frame_response(request, frame_id)


def contacts(request):
    return get_contacts_response(request)


def about(request):
    return render(request, "workshopapp/about.html")
