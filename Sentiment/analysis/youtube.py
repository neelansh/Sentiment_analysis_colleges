import requests
from bs4 import BeautifulSoup
def get_link(query):
	search_query=query.replace(' ' , '+')
	i=requests.get("https://www.youtube.com/results?sp=CAM%253D&q="+search_query)
	soup=BeautifulSoup(i.text)
	youtubelinks=soup.find_all("a")
	count=0;
	for links in youtubelinks:
		youtubehref=links.get('href')
		youtubehrefstring=str(youtubehref)
		if "/watch?v=" in youtubehrefstring:
			print("the link to the  video is "+"www.youtube.com"+youtubehrefstring)
			for s in youtubehrefstring:
				count=count+1;
				if s=="=":
					embedlink="https://www.youtube.com/embed/"+youtubehrefstring[count:]
					result_link = '<iframe width="420" height="315" src="'+embedlink+'"frameborder="0" allowfullscreen></iframe>'
			break
	return result_link


#"&sp=CAM%253D"