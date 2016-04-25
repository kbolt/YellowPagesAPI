#! python3
# Pull business listings from YP using their API
import requests,json,csv,pprint

yp_api = open('yp_api.txt', 'r').read()

def bizSearch(query):
	api_key = yp_api
	url = 'http://api2.yp.com/listings/v1/search?'
	searchLoc = query.replace(' ', '%20')
	searchUrl = url + 'searchloc=' + searchLoc + '&term=restaurant' + '&format=json' + '&sort=distance' + '&radius=50' + '&listingcount=50' + '&key=' + api_key
	json_data = requests.get(searchUrl)
	data = json_data.json()
	outputFile = open('results.csv', 'w', newline='')
	outputWriter = csv.writer(outputFile)

	for item in data['searchResult']['searchListings']['searchListing']:
			outputWriter.writerow(
				[item['businessName'],item['street'],item['city'],item['state'],item['zip'],
				item['phone'],item['email'],item['websiteURL']])

	outputFile.close()	

bizSearch('port saint lucie')