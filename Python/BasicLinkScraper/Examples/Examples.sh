#/bin/zsh
# Retrieve links to all PDFs on Pixar's Graphics Technical Library, store in a text file.
python3 ./../BasicLinkScraper.py --baseURL "https://graphics.pixar.com/library/" --pages "index.html" --extensions ".pdf" --linksonly > ExampleOutput.txt