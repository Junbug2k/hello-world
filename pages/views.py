from django.http  import HttpResponse




def homePageView(request):
	return HttpResponse('Hello, Jerry and Welcome to our Universe!')


# Create your views here.
