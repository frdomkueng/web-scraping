from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# creating the file where i will store all th records
filename = "products.csv"
f = open(filename, "w")

# setting the headers file which willl describe the data store
headers = "product_name, price_ship\n" 
f.write(headers)

for i in range(1,20):
	# my url from where i will retreive the data i fancy
	# note that the srt(i) will help me go forward in pages results 1, 2 ... since the structure changes less 
	my_url = 'https://www.newegg.com/p/pl?d=graphic+card&page='+str(i)
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	#parsing the page in html 
	page_soup = soup(page_html,"html.parser")
	#find all element item-container 
	#in fact i inspect the source code(of html) then precisely wrap the div containing the data i fancy on each item here graphic card
	containers = page_soup.findAll("div",{"class":"item-container"})
	# all the div catch then i iterate on each div 
	for container in containers:
		title_container = container.findAll("a",{"class":"item-title"})
		product_name = title_container[0].text
		price_shipping_container = container.findAll("li",{"class":"price-ship"})
		price_ship = price_shipping_container[0].text
		#removing some none usefull characters 
		chars = ["(",")"]
		# writting the data in my file 
		f.write(product_name.replace(",", "|") + "," + price_ship + "\n" )
#closing the file open 
f.close()