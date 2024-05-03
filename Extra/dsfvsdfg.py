lis =  [
    "http://www.ualberta.ca/~rjia/Math215/Hwks/prob1.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/sol1.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/prob2.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/sol2.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/prob3.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/sol3.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/prob4.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/sol4.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/prob5.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/sol5.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/prob6.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/sol6.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/prob7.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/sol7.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/prob8.pdf",
    "http://www.ualberta.ca/~rjia/Math215/Hwks/sol8.pdf"
]
import urllib.request
for i in lis:
    urllib.request.urlretrieve(i, i.split("/")[-1])