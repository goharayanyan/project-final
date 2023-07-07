from rest_framework import generics
from .models import Creative
from .serializers import CreativeSerializer


class BidResponseList(generics.ListCreateAPIView):
    queryset = Creative.objects.all()
    serializer_class = CreativeSerializer

class BidResponseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Creative.objects.all()
    serializer_class = CreativeSerializer