'''
This script is modified from Dan Shiebler's jsonWriting.py:
It takes data from two files and creates a mixed json dictionary and array
which is used by the /symbol-maps/brownSlider visualization.

'''

import  json

location_file = open("../data/2014-05-05HayJCBLocations.json")
book_file = open("../data/2014-05-20HayJCBBooks.json")
data = json.load(location_file)
bookData = json.load(book_file)
with open("../data/JosiahSliderData-TEST1.json",'w') as outfile:
	for location in data['rows']:
		for book in bookData['rows']:
			location['SliderDict'] = {}
			if book['GeoPlace'] == location["Name"]:
				location['SliderDict'][book["ShortTitle"]] = book["Year"]
		json.dump(data,outfile)
location_file.close()
book_file.close()

# with open('../data/JosiahSliderData-Test1.json') as infile:
# 	with open('../data/2014-05-20JosiahSliderData.json','w') as outfile:
# 		jsonData = json.load(infile)
# 		for location in jsonData['rows']:
# 			location["bookTitles"] = sorted(location['SliderDict'], key=location['SliderDict'].get)			
#   		json.dump(jsonData,outfile)

#need to write this to a file now