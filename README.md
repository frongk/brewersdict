# brewersdict
Brewer's Dictionary of Phrase and Fable - Text Cleaning and Analysis

### Purpose
To convert a really messy public domain text file of Brewer's Dictionary into a clean `csv` file with the columns: `Entry`, `Definition` With the text more cleanly parsed in this structure, the text is ready for further analysis.

### About the Dictionary
Brewer's Dictionary of Phrase and Fable, as its title states, is a reference for phrases and fables. It was first published in 1890 by John Brewer and contains countless stimulating tidbits. More information about the dictionary can be found on its wiki page:
https://en.wikipedia.org/wiki/Brewer%27s_Dictionary_of_Phrase_and_Fable

A public domain version of this dictionary is available on archive.org:
https://archive.org/details/brewersdictionar000544mbp

### Background
We were driving on a cool November night and a 30-year-old recording of Casey Kasem's American Top 40 was playing on the 80s station. To preface the next song, Stevie Wonder's Skeletons (https://youtu.be/u94yWGkoA6o), he read an excerpt from Brewer's Dictionary about skeletons
> The family skeleton, or the skeleton  in the cupboard.Some domestic secret that the  whole family conspires to keep to itself; every  family is said to have at least one.The story is that someone without a single  care or trouble in the world had to be found.After long and unsuccessful search a lady was  discovered whom all thought would "fill the  bill"; but to the great surprise of the inquirers,  after she had satisfied them on aH points and  the quest seemed to be achieved, she took them  upstairs and there opened a closet which con-tained a human skeleton."I try,*' said she, "to  keep niy trouble to myself, but every night rny  husband compels me to kiss that skeleton."She then explained that the skeleton was once  her husband's rival, killed in a duel.

After hearing that, I felt like I needed more useless but interesting trivia in my life so I went searching for the Brewer's Dictionary of Phrase and Fable online. There's a lot more stuff like that in the dictionary. Hopefully this project should make it a little easier to track down entries, use the text for your own projects, and perform your own analysis (NLP??).

### Methodology
Python and NLTK's tokenizers are leveraged to clean up this text. Some general heuristics are used to define definitions in the text. Some of the definition text appears as entries because of idiosyncracies with the document. If you have some clever ways of further cleaning the text please contribute!

### Main Files
1. `brewers_trim.txt` - Raw text with beginning text manually removed from document.  
2. `text2entry.py` - Script to parse out entries from the text  
3. `clean_brewers.csv` - Output comma separated file with format `entry, definition`  

