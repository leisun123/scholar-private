import orcid
from orcid import Q
john = orcid.search('zi wang')
print (next(john).biography)