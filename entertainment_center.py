# Author: Aniekan Akai
# Main script to launch site

# Libraries to be used are imported
import os
import sys
import fresh_tomatoes
import media

greenStreetHooligans = media.Movie(
    "Green Street Hooligans",
    "http://www.gstatic.com/tv/thumb/dvdboxart/36479/p36479_d_v7_aa.jpg",  # noqa
    "http://www.youtube.com/watch?v=EAe-1Lv1KYU")

austinpowers1 = media.Movie(
    "Austin Powers: International Man of Mystery",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcRL9p4e-LSjwXBqgvJjNQsZmRLqRf1L7mYp4VpGasD7ZDgziA4p",  # noqa
    "http://www.youtube.com/watch?v=Oze1bn4_pbk")

austinpowers2 = media.Movie(
    "Austin Powers: The Spy Who Shagged Me",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcSGxRN5Uya0XnM2JThTEIrdLCaPLGsAJRcuMRIGJ7kXwh7WsJWp",  # noqa
    "http://www.youtube.com/watch?v=knNCtO7gf7g")

austinpowers3 = media.Movie(
    "Austin Powers: Goldmember",
    "http://www.gstatic.com/tv/thumb/movieposters/30078/p30078_p_v7_aa.jpg",  # noqa
    "http://www.youtube.com/watch?v=0F8CQp9pP7o")

aclockworkorange = media.Movie(
    "A Clockwork Orange",
    "http://www.gstatic.com/tv/thumb/movieposters/1587/p1587_p_v7_aa.jpg",  # noqa
    "http://www.youtube.com/watch?v=gmm5jeeH8mY")

_300spartans = media.Movie(
    "300",
    "http://www.gstatic.com/tv/thumb/movieposters/163191/p163191_p_v7_aa.jpg",  # noqa
    "http://www.youtube.com/watch?v=wDiUG52ZyHQ")

# List of movies to display
favouriteMovies = {greenStreetHooligans, austinpowers1, austinpowers2,
                   austinpowers3, aclockworkorange, _300spartans}


# Call to render webpage
fresh_tomatoes.open_movies_page(favouriteMovies)
