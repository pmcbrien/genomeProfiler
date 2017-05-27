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

SNPediaUrl = "http://www.snpedia.com" #genetic db
spornyFileLocal = "sporny.txt"  #https://github.com/msporny/dna

duckUrl = "http://api.duckduckgo.com/?format=json&q=" + firstName
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

#first_link = parsed.findAll('div', {'class': re.compile('links_main*')})[0].a['href']
       
rsids = [x[0] for x in csv.reader(open(spornyFileLocal,'r'),delimiter='\t')]
chromosomes  = [x[1] for x in csv.reader(open(spornyFileLocal,'r'),delimiter='\t')]
positions = [x[2] for x in csv.reader(open(spornyFileLocal,'r'),delimiter='\t')]
genotypes = [x[3] for x in csv.reader(open(spornyFileLocal,'r'),delimiter='\t')]

print rsids[0]

for rsid in rsids:
    url = "https://api.23andme.com/3/marker/" + rsid
    print url
    response = urllib2.urlopen(url)
    data = response.read()
    values = json.loads(data)    
    print ', '.join(values)


#with open("sporny.txt") as geneRecord: 
#    LoL=[x.strip().split('\t') for x in geneRecord]
#    print LoL[0]
#    print zip(*(line.strip().split('\t') for line in geneRecord))

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