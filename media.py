# Author: Aniekan Akai
# Contains all media related objects

#Libraries to be used are imported
import os
import sys

################################################
# Movie object containing the following fields: #
#	1. Title								   #
#	2. Poster URL							   #
#	3. Trailer YouTube URL					   #
################################################

class Movie:
	def __init__(self, title, posterUrl, trailerUrl):
		self.title = title
		self.posterUrl = posterUrl
		self.trailerUrl = trailerUrl
