class Movie():
	''' 
	A movie class to store movie details 
	'''
	def __init__(self, title, poster_image_url, trailer_youtube_url):

		'''
		Constructor Args 
			title - String
			poster_image_url - String
			trailer_youtube_url -String
		'''

		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url