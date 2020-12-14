# Importing the libraries to be used
import requests                             # The request libraries used to connect to the site
from bs4 import BeautifulSoup               # This library is used to scrape the data from the link from the data gotten from the request library


# The Scrape funcitons that performs the scraping
def scrape(url):
    # The page
    page = requests.get(url)
    # The page  content is gotten here
    soup = BeautifulSoup(page.content, 'html.parser')
    # The title of the article is gotten here
    title = soup.find('title').text
    # Open an new article file for each link
    article = open(f'cnn travel news/{title}.txt', 'w')
    # write the article topic
    article.write('*********************Article Topic********************************\n\n')
    # write the article title in the new file
    article.write(title)
    article.write('\n\n\n*********************Article Content********************************\n\n')
    # Fetch the content from the data gotten from the site
    paragraphs = soup.find_all('div', class_='Paragraph__component')
    # iterate through the reault and write the each into the new file
    for i in paragraphs:
        article.write(i.text)
        article.write('\n')
    article.close
    # return the article
    return article

# The main function
def main():
    # it promts the user to input the site link
    try:
        site = str(input('Enter the Cnn Artcle to Scrape:  '))
        scrape(site)
    except ValueError:
        print('Please paste your Cnn Artcle link')
        site = str(input('Enter a Cnn Artcle link to Scrape:  '))
        scrape(site)  
    

if __name__ == "__main__":
    main()