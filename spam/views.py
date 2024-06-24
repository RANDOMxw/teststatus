from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SpamNumber
from .serializers import SpamNumberSerializer

class SpamView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        spam_number, created = SpamNumber.objects.get_or_create(phone_number=phone_number)
        if created:
            spam_number.spam_count = 1
        else:
            spam_number.spam_count += 1
        spam_number.save()
        return Response({'message': 'Spam number marked successfully'})

class SearchView(APIView):
    def get(self, request):
        query = request.GET.get('query')
        if query.isdigit():  # search by phone number
            contacts = Contact.objects.filter(phone_number=query)
        else:  # search by name
            contacts = Contact.objects.filter(name__icontains=query)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
