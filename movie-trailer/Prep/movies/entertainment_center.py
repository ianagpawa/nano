import fresh_tomatoes

import media


fear = media.Movie("Fear and Loathing in Las Vegas",
                    "A journalist and his lawyer embark on an existentialist journey in the desert City of Las Vegas and wreak havoc.",
                    "https://upload.wikimedia.org/wikipedia/en/6/6f/FandlinLV.jpg",
                    "https://www.youtube.com/watch?v=vvrkNjaZX0A")

wonder = media.Movie("Wonderboys",
                    "An author has a mid-life crisis.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/6/68/OriginalWBposter.jpg/220px-OriginalWBposter.jpg",
                    "https://www.youtube.com/watch?v=sveK_fhIqhs")

professional = media.Movie("The Professional",
                            "A hitman begins a friendship with an innocent girl.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/0/03/Leon-poster.jpg/220px-Leon-poster.jpg",
                            "https://www.youtube.com/watch?v=aNQqoExfQsg")

godfather = media.Movie("The Godfather",
                        "A master piece of cinema",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                        "https://www.youtube.com/watch?v=fB_8VCwXydM")


goodfellas = media.Movie("Goodfellas",
                        "Mafioso carve their own version of the American Dream.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/7/7b/Goodfellas.jpg/220px-Goodfellas.jpg",
                        "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

aliens = media.Movie("Aliens",
                    "Space marines battle aliens.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/Aliens_poster.jpg/220px-Aliens_poster.jpg",
                    "https://www.youtube.com/watch?v=zNE0dlHcmgA")


predator = media.Movie("Predator",
                        "An alien hunter stalks a military unit in the jungle",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/9/95/Predator_Movie.jpg/220px-Predator_Movie.jpg",
                        "https://www.youtube.com/watch?v=K9AT3tQGbIk")

terminator = media.Movie("Terminator 2: Judgement Day",
                        "An android from the future protects the savior of the human race.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/85/Terminator2poster.jpg/220px-Terminator2poster.jpg",
                        "https://www.youtube.com/watch?v=7QXDPzx71jQ")

stargate = media.Movie("Stargate",
                        "A team travels to an alien planet.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Stargateposter.jpg/220px-Stargateposter.jpg",
                        "https://www.youtube.com/watch?v=_mucMCddPy0")

loop = media.Movie("In The Loop",
                    "A revealing look inside the world of global politics and war.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/0/01/In_the_Loop_poster.jpg/220px-In_the_Loop_poster.jpg",
                    "https://www.youtube.com/watch?v=_VDc7-YH1LA")







#fear.show_trailer()
movies = [goodfellas, aliens, predator, terminator, stargate, loop]
#fresh_tomatoes.open_movies_page(movies)


#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
