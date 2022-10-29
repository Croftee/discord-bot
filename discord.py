from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
from bs4 import BeautifulSoup
import re


def getHTMLdocument(url):
      
    # request for HTML document of given url
    response = requests.get(url)
      
    # response will be provided in JSON format
    return response.text
  
    
# assign required credentials
# assign URL
url_to_scrape = "https://store.steampowered.com/specials/"
  
# create document
html_document = getHTMLdocument(url_to_scrape)
  
# create soap object
soup = BeautifulSoup(html_document, 'html.parser')
  
  
# find all the anchor tags with "href" 
# attribute starting with "https://"
for link in soup.find_all('a', 
                          attrs={'href': re.compile("^https://")}):
    # display the actual urls
    print(link.get('href'))  



""" webhook = DiscordWebhook(url='REDACTED')

# create embed object for webhook
embed = DiscordEmbed(title='Your Title', description='Lorem ipsum dolor sit', color='03b2f8')

# set author
embed.set_author(name='Author Name', url='author url', icon_url='author icon url')

# set image
embed.set_image(url='your image url')

# set thumbnail
embed.set_thumbnail(url='your thumbnail url')

# set footer
embed.set_footer(text='Embed Footer Text', icon_url='URL of icon')

# set timestamp (default is now)
embed.set_timestamp()

# add fields to embed
embed.add_embed_field(name='Field 1', value='Lorem ipsum')
embed.add_embed_field(name='Field 2', value='dolor sit')

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute() """