from django.shortcuts import render
from django.http import JsonResponse
import requests

def place_search(request):
	key = "AIzaSyB1f_SvjBMaVeVzfPgI-h37ZdX89rPhXvg"
	query = request.GET.get('query', '')
	print (query)
	# query = "Starbucks"
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&query=%s&region=kw"%(key, query)


	


	token = request.GET.get('pt')
	if token:
		url += "&pagetoken=%s"%(token)

	response = requests.get(url).json()

	context = {
	'response': response,
	}

	# return JsonResponse(response, safe=False)
	return render (request, 'places.html', context)



def place_detail(request):
	key = "AIzaSyB1f_SvjBMaVeVzfPgI-h37ZdX89rPhXvg"
	map_key = "AIzaSyCMmBQGXllXlyypFzElc86ZRbswxCwL4ug"
	place_id = request.GET.get('id')
	print(place_id)

	url = "https://maps.googleapis.com/maps/api/place/details/json?placeid=%s&key=%s"%(place_id, key)

	response = requests.get(url).json()
	context = {
	'response': response,
	'map': map_key,
	}

	return render (request, 'detail.html', context)
	# return JsonResponse(response, safe=False)


