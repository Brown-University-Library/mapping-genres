import  json

'''myFile = open("../data/JosiahPre1800Locations2-6-13.json")
#bookFile = open("../data/BookTitlesWithLocationsAndYear.json")
data = json.load(myFile)
bookData = json.load(bookFile)
for location in data['rows']:
	location['SliderDict'] = {}
	for book in bookData['rows']:
		if book['GeoPlace'] == location["Name"]:
			location['SliderDict'][book["TITLE"][0:10]] = book["Year"]
myFile.close()
bookFile.close()'''

with open('../data/JosiahSliderData.json') as infile:
	with open('../data/JosiahSliderDataTwo.json','w') as outfile:
		jsonData = json.load(infile)
		for location in jsonData['rows']:
			location["bookTitles"] = sorted(location['SliderDict'], key=location['SliderDict'].get)			
  		json.dump(jsonData,outfile)

#need to write this to a file now
