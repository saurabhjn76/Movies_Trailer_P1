from media import Movie

'''
A movies storage list
'''
movies = list()
'''
we append instances of class Movie in movies list.
Movie constructor takes three arguments
  title - String
  poster_image_url - String
  trailer_youtube_url -String
'''
movies.append(Movie("Interstellar",
                    "http://www.interstellarmovie.net/images/downloads/" +
                    "wps/1920/int_wps_1920_farm.jpg",
                    "https://www.youtube.com/watch?v=zSWdZVtXT7E"))
movies.append(Movie("Inception",
                    "https://img.yescdn.ru/2016/07/20/cover/1b5c10d82b89" +
                    "2ba0f2c2e9b42d5df5fe-inception-1469000805.jpeg",
                    "https://www.youtube.com/watch?v=8hP9D6kZseM"))
movies.append(Movie("The Dark Knight",
                    "http://media1.santabanta.com/full1/Hollywood%20Movies/" +
                    "The%20Dark%20Knight/the-dark-knight-24d.jpg",
                    "https://www.youtube.com/watch?v=yQ5U8suTUw0"))
