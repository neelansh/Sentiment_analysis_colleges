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


def get_link_viewed(query):
	search_query=query.replace(' ' , '+')
	i=requests.get("https://www.youtube.com/results?&q="+search_query+"&sp=CAM%253D")
	soup=BeautifulSoup(i.text)
	res_div = soup.find("ol", {"class": "item-section"})
	count = 0
	links = []
	for tag in res_div.find_all("a", {"class": ["yt-uix-sessionlink", "yt-uix-tile-link", "yt-ui-ellipsis", "yt-ui-ellipsis-2", "spf-link"]}):
		if count >= 10:
			break
		if "watch" in tag.get("href"):
			link = "http://www.youtube.com/embed/" + tag.get("href").replace("/watch?v=" , "")
			links.append(link)
			count = count+1;
	return list(set(links))

def get_link_relevant(query):
	search_query=query.replace(' ' , '+')
	i=requests.get("https://www.youtube.com/results?search_query="+search_query)
	soup=BeautifulSoup(i.text)
	res_div = soup.find("ol", {"class": "item-section"})
	count = 0
	links = []
	for tag in res_div.find_all("a", {"class": ["yt-uix-sessionlink", "yt-uix-tile-link", "yt-ui-ellipsis", "yt-ui-ellipsis-2", "spf-link"]}):
		if count >= 10:
			break
		if "watch" in tag.get("href"):
			link = "http://www.youtube.com/embed/" + tag.get("href").replace("/watch?v=" , "")
			links.append(link)
			count = count+1;
	return list(set(links))
#"&sp=CAM%253D"
