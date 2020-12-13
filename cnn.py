import requests
from bs4 import BeautifulSoup


def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('title').text
    # Article file
    article = open(f'cnn travel news/{title}.txt', 'w')
    article.write('*********************Article Topic********************************\n\n')
    article.write(title)
    article.write('\n\n\n*********************Article Content********************************\n\n')
    paragraphs = soup.find_all('div', class_='Paragraph__component')
    for i in paragraphs:
        article.write(i.text)
        article.write('\n')
    article.close
    return article

def main():
    try:
        site = str(input('Enter the Cnn Artcle to Scrape:  '))
        scrape(site)
    except ValueError:
        print('Please paste your Cnn Artcle link')
        site = str(input('Enter a Cnn Artcle link to Scrape:  '))
        scrape(site)  
    

if __name__ == "__main__":
    main()