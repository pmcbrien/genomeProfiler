import csv
import re
import urllib2
import urllib
import json
from BeautifulSoup import BeautifulSoup
import urllib

clustersGeographic = ["Africa", "Americas", "Asia","Europe", "Oceania"]
#clustersChromosomal =

#used to assign the sex chromo will add more granular later
chromoSexFemale = "XX"
chromoSexMale = "XY"

#please let us traverse throuh all chromosomes and link up to free open DB's online
ncbiUrl = "ftp://ftp.ncbi.nih.gov/genomes/Homo_sapiens/"

firstName = raw_input("What is the first name that you want to search for ? >> ")
firstName = "patrick"

duckUrl = "http://api.duckduckgo.com/?format=json&q="+firstName
#lastName = raw_input("What is the surname that you want to search for ? >> ")
lastName = "mcbrien"
#Sources Config, we scientists must work together 

#popular give names from wiki

popularGiveNamesWikiUrl = "https://en.wikipedia.org/wiki/List_of_most_popular_given_names"

givenNamesByGeo = urllib.URLopener()
givenNamesByGeo.retrieve(popularGiveNamesWikiUrl, "givenNames.html")

#wikipedia
wikiUrlFirstNameUrl = "https://en.wikipedia.org/wiki/" + firstName + "_(given_name)"
#wikiUrlLastNameUrl = "https://en.wikipedia.org/wiki/" + lastName + "_(surname)"

#search engines
duckQueryPrefix = "What country is the name "
duckQuerySuffix = " From" #what country ins the name Patrick From?

#data points for later
duckQueryOriginFirstName = duckQueryPrefix + firstName + duckQuerySuffix
duckQueryOriginLastName = duckQueryPrefix + lastName + duckQuerySuffix
duckQueryGenderOfName = "What gender is the name " + firstName 

#print duckUrlPrefix + duckQueryOriginFirstName

site = urllib.urlopen(duckUrl)
data = site.read()
parsed = BeautifulSoup(data)

first_link = parsed.findAll('div', {'class': re.compile('links_main*')})[0].a['href']
       
print first_link



##query = urllib.urlencode( {'q' : queryPrefix + " " + firstName + " " + querySuffix } )

#googleResponse = urllib2.urlopen (url + query ).read()
#wikiFirstNameResponse = urllib2.urlopen ( wikiUrlFirstNameUrl ) 
#duckResponse = urllib2.urlopen( duckUrl )

#print(wikiFirstNameResponse)
#duckData = json.loads ( duckResponse )
#duckResults = duckData [ 'responseData' ] [ 'results' ]

#inputFbNameFile = "test.input.csv" #"facebook-names-unique.csv"
#outputGenome = "outputGenome.dat"
#fields = ('facebook_name')

#with open(inputFbNameFile) as f:
#    for line in f:
#        print line