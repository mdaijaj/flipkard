import requests,pprint
from bs4 import BeautifulSoup

def flipkard(url):
	link=requests.get(url)
	soup=BeautifulSoup(link.text,"html.parser")
	div=soup.findAll("div", class_="_1UoZlX")
	dic={}
	counter=1
	urls=[]
	ur=soup.find("div",class_="_2zg3yZ")
	link=ur.find_all("a") 
	for j in link:
		a=j.get("href")
		urls.append(a)
	for i in div:
		name=i.find("div",class_="_3wU53n").text
		price=i.find("div",class_="_1vC4OE _2rQ-NK").text
		features=i.find("ul",class_="vFw0gD").text
		
		dic["price"]=price
		dic["Position"]=counter
		dic["features"]=features
		dic["product_name"]=name
		counter+=1
		pprint.pprint(dic)

	if user>=len(urls):
		print("There is no data in this page")
	return(dic)

user=int(input("which page you want to scrap:"))
url="https://www.flipkart.com/search?q=apple&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_5&otracker1=&page="+str(user)
pprint.pprint(flipkard(url))