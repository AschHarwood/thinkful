phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}


try:
	phone_book["Sarah Hughes"]
except KeyError:
	print "couldnt find it"