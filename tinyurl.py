from bs4 import BeautifulSoup
from urllib.request import urlopen
def shorten(long_url, alias):
	URL = "http://tinyurl.com/create.php?source=indexpage&url=" + long_url + "&submit=Make+TinyURL%21&alias=" + alias
	response = urlopen(URL)
	soup = BeautifulSoup(response, 'html.parser')
	check_error = soup.p.b.string
	if "The custom alias" in check_error:
		return "Alias you have selected is already used by someone else."
	else:
		return soup.find_all('div', {'class': 'indent'})[1].b.string

