#   BasicLinkScraper
#   (c)2021 Trevor D. Brown.
#   Distributed under the MIT license.
#
#   BasicLinkScraper.py -   scrapes a specified base URL's specified pages for
#                           specified links with specified extensions. Adapted
#                           from the GeeksForGeek's article:
#                           https://www.geeksforgeeks.org/python-program-to-recursively-scrape-all-the-urls-of-the-website/
#
#   History:
#       02/16/2021 - Trevor D. Brown
#           Created file.
#           Began adapting script for my specific use cases.
#
#   Known Issues/TODOs:
#       TODO 1: Work on handling special links (i.e. mailto, tel, etc.)
#       TODO 2: Work on URLs with relative addressing (i.e. ./page.html, ./../another-page.html)
#       TODO 3: Find a better approach for try/except statement in scrape function.
#       TODO 4: Add support for file exports, instead of depending on shell output redirection.

import sys                          # used for argument parsing.
from bs4 import BeautifulSoup       # used for HTML parsing.
import requests                     # used to retrieve web pages.
   
# scrape - scrapes a specified site
def scrape (site, base, extensions, linksOnly): 
    # lists 
    urls = [] 

    if (not linksOnly):
        urls.append("%s:" % (site))

    # GET request to the specified site.
    request = requests.get(site)
       
    # Parsing the returned HTML.
    parsedHTML = BeautifulSoup(request.text,"html.parser") 
    
    # For all anchor tags found on the page, extract their href attribute.
    for element in parsedHTML.find_all("a"):
        # Reference: TODO 3
        try:
            href = element.attrs['href'] 
            
            # Reference: TODO 2
            if (str(href).startswith("./")):
                site = base + str(href).replace("./", "")
            else:
                site = base + href
            
            # If the site ends with a requested extension, or the user has specified any extension, add it to the list.
            if ((site.endswith(tuple(extensions))) or (extensions == ["*"])):
                if (site not in urls):
                    # Get the format of the URL, based on the "linksonly" argument's status.
                    urlString = ""

                    if (not linksOnly):
                        urlString = ("\t%s" % (site))
                    else:
                        urlString = ("%s" % (site))

                    urls.append("%s" % (urlString))

        except:
            # We're not too concerned with exceptions...
            # but, this had to bere here to work. So...
            # yeah...
            1==1
    
    return urls

# parseArgs - determine what has been defined
def parseArgs ():
    # Variables that are passed via command line arguments:
    baseURL = ""            # The base URL for the website (i.e. https://www.example.com/)
    pages = []              # The list of pages requested for parsing, delimited by commas. (i.e. index.html,contacts.htm)
    extensions = []         # The list of extensions to look for during parsing, delimited by commas. (i.e. .pdf,.jpg)
    linksOnly = False       # Determining if only the retrieved links are to be printed, or all extra statements.

    for i, arg in enumerate(sys.argv):
        if (i > 0):
            if ((arg == "--baseURL") or (arg == "-u")):
                baseURL = sys.argv[i+1]
            elif ((arg == "--pages") or (arg == "-p")):
                pages = sys.argv[i+1].split(",")
            elif ((arg == "--extensions") or (arg == "-e")):
                extensions = sys.argv[i+1].split(",")
            elif ((arg == "--linksonly")):
                linksOnly = True
    
    return baseURL, pages, extensions, linksOnly

# main - the primary driver for the script.
def main ():
    
    allScrapedURLs = []
    baseURL, pages, extensions, linksOnly = parseArgs()
    
    if (baseURL):
        if (len(pages) <= 0):
            pages = ["index.html"]  # Check only the index page of the site, if no specific page is given.

        if (len(extensions) <= 0):
            extensions = ["*"]  # Get every href link, if no specific extension is given. 

        for page in pages:
            site = baseURL + page
    
            # Scrape the page
            scrapedURLs = scrape(site, baseURL, extensions, linksOnly)

            allScrapedURLs.extend(scrapedURLs)

        if (len(allScrapedURLs) > 0):
            for url in allScrapedURLs:
                print(url)
    else:
        if (not linksOnly):
            print("No base URL defined.")

# Calling the main function...
main()