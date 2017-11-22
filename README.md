# brewersdict
Brewer's Dictionary of Phrase and Fable - Text Cleaning and Analysis

### Purpose
To convert a really messy public domain text file of Brewer's Dictionary into a clean `csv` file with the columns: `Entry`, `Definition` With the text more cleanly parsed in this structure, the text is ready for further analysis.

### Background
Brewer's Dictionary of Phrase and Fable, as its title states, is a reference for phrases and fables. It was first published in 1890 by John Brewer and contains countless stimulating tidbits. More information about the dictionary can be found on its wiki page:
https://en.wikipedia.org/wiki/Brewer%27s_Dictionary_of_Phrase_and_Fable

A public domain version of this dictionary is available on archive.org:
https://archive.org/details/brewersdictionar000544mbp

### Methodology
Python and NLTK's tokenizers are leveraged to clean up this text. Some general heuristics are used to define definitions in the text. Some of the definition text appears as entries because of idiosyncracies with the document. If you have some clever ways of further cleaning the text please contribute!

### Main Files
1. `brewers_trim.txt` - Raw text with beginning text manually removed from document.  
2. `text2entry.py` - Script to parse out entries from the text  
3. `clean_brewers.csv` - Output comma separated file with format `entry, definition`  

