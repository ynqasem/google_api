from django.http import JsonResponse
from urllib.parse import quote
import oauth2
import json

CONSUMER_KEY  = "unbZlVXgVrKt8NOlOTLHzxVpX"
CONSUMER_SECRET = "w4H4yoYX8Ak13yMwweaPoWz3JblEaR5g881iAuJ4XajicofJaU"

def oauth_req(url, key, secret, http_method="GET", post_body='', http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, http_method, bytes(post_body, 'utf-8'), headers=http_headers )
    return content

def tweet_search(request):
	query = "django"
	enc_q = quote(query)
	url = "https://api.twitter.com/1.1/search/tweets.json?q=%s"%(enc_q)

	person = request.user
	social_account = person.socialaccount_set.get(user=person.id)
	social_token = social_account.socialtoken_set.get(account=social_account.id)

	token = social_token.token
	print(token)
	token_secret = social_token.token_secret
	print (token_secret)
	response = oauth_req(url, token, token_secret, "GET")
	stuff = json.loads(response)
	return JsonResponse(stuff, safe=False)

def tweet_post(request):
	user = request.user 
	social_account = user.socialaccount_set.get(user=user.id)
	app_token = social_account.socialtoken_set.get(account=social_account.id)
	token = app_token.token
	token_secret = app_token.token_secret

	query = "Hi my name is ___"
	enc_q = quote(query)
	url = "https://api.twitter.com/1.1/statuses/update.json?status=%s"%(enc_q)

	response = oauth_req(url,token, token_secret, "POST")
	stuff = json.loads(response.decode("utf-8"))
	return JsonResponse(stuff, safe=False)