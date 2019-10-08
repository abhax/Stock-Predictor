from rauth import OAuth1Service

def EstablishOAuth():
	allyBank = OAuth1Service(
	    name='Invest Magic',
	    consumer_key='aN91TS2OaHIzoD1ejh6FwVtwjL4gGFs5e08edlumcsg7',
	    consumer_secret='l6cT12lm2pcWabi5sRCg2LOXcxDR3T3CYisEVN4lPno6',
	    request_token_url='https://developers.tradeking.com/oauth/request_token',
	    access_token_url='https://developers.tradeking.com/oauth/access_token',
	    authorize_url='https://developers.tradeking.com/oauth/authorize',
	    base_url='https://api.tradeking.com/v1/')

	request_token, request_token_secret = allyBank.get_request_token()
	authorize_url = allyBank.get_authorize_url(request_token)

	print ('Visit this URL in your browser: ' + authorize_url)
	pin = input('Enter PIN from browser: ')  # `input` if using Python 3!
	session = allyBank.get_auth_session(request_token,
	                                   request_token_secret,
	                                   method='POST',
	                                   data={'oauth_verifier': pin})
	return session


sess = EstablishOAuth()
json = sess.get('account',params={'format':'json'})
print(json.json()) 
