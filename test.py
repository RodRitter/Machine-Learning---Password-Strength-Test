import re

specialMatch = re.search(r'[^a-zA-Z0-9]', '9a2d$elo,Seien', re.M)
if specialMatch:
	print 'Match! ' + str(specialMatch.group(0))