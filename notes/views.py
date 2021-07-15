from rest_framework import viewsets
from . import serializers
from . import models

class NoteApi(viewsets.ModelViewSet):
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()

    def get_queryset(self):
        queryset = models.Note.objects.filter(
            title__icontains=self.request.GET.get("search", "")
        ).order_by("-created_at")
        return queryset
