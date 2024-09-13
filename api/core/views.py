from .serializers import PersonSerializer
from .models import Person
from rest_framework import viewsets

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer