from django.shortcuts import render
from django.http import JsonResponse
import requests

def place_search(request):
	key = "AIzaSyB1f_SvjBMaVeVzfPgI-h37ZdX89rPhXvg"
	query = "Starbucks"
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&query=%s&region=kw"%(key, query)

	response = requests.get(url).json()
	
	context = {
	'response': response,
	}

	# return JsonResponse(response, safe=False)
	return render (request, 'places.html', context)