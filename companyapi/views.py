
from django.http import JsonResponse

def home_page(request):
    print("home page requested")
    friends=[
        'Rahul',
        'Shivam',
        'Akash'
    ]
    return JsonResponse(friends,safe=False)