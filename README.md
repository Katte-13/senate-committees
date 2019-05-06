# senate-committees
A simple scrapper for updating the Romanian Senate Permanent Committees composition.
## Introduction
This is a training project. I'm working for a senator and he wanted this integrated information on the Permanent Committees composition. Thought anyone could retry those data navigating the Senate page, the scraping offer the possibility to update any changes in the resulting file quicker. 
The CSV file that contains the scraping result keeps the hierarchical order, the Committee bord will be displayed first: President, Vice-president, Secretary - then the committee members. 
## Technologies
Python 3.7\
Requests 2.21\
BeautifulSoup 4.6.3\
Pandas 0.23.4
## Launch
I use Spyder and the libraries are via Anaconda.
### Status
I scheduled a task to run the script daily. 
Right now the CSV file is in my computer. Because it should be available and handy for his user I put the file on Drive and sync it with my computer. It didn'n work though. 
If anyone have a clean and easy to use solution for my problem, I kindky ask for it.
### Trivia
I chose Pandas because with it I send my data into a CSV file writing just 2 line o code. Chosing Pandas I've generated from the start dictionaries. Anyone who dislike this aproach can use CSV library and open and write a CSV file that way.
Because Romanian is a language that holds diacritics, I used utf-8-sig encoding for a corect display of names.
## Let me know!
How do you find my project? 





