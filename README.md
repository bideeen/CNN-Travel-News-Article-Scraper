# CNN-Travel-News-Article-Scraper

## Introduction
I built a simple web scraper that will return the content of cnn travel news article when given a specific URL. Some examples of real products which use similar technologies include price-tracking websites and SEO audit tools which may scrape top search results. This project may took me around 4 hours to complete.

## How To Run The Script
Simple as it is, just run the following codes:
  - python cnn.py

  That's all you need to do, and the file get saved on the cnn travel news folder.

## Libraries
The python libraries used where:
  - Request library
    - This was used to connect tot the news site.
  - Beautifulsoup library
    - This was used to scrape the content in the articles from the site link.

## Output
The articles where stored in .txt format

## Note
This code only applies to CNN travel news alone. Any links used will not be scraped.

## Further Works
I intend on improving the code to perform the following:
  - Scrape all news link
  - Scrape each news per link
  - Deploy the script using Flask
  - Extend the Script functionality to Scrape other form of News on CNN