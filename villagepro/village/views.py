
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Village

class Add_village(CreateView):
    model = Village
    fields = "__all__"


class List_village(ListView):
    model = Village

class Detail_village(DetailView):
    model = Village


class Update_village(UpdateView):
    model = Village

    fields = "__all__"
    success_url = "/"

class Delete_village(DeleteView):
    model = Village
    success_url = "/"
    template_name = "village/Village_confirm.html"
