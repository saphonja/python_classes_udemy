import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
"A story of a boy and his toys that come to life", 
"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", 
"https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
"A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.", 
"http://image.prntscr.com/image/df136c95d7c049c9a4e8d861457cd158.png",
"http://www.imdb.com/videoplayer/vi2804482585?ref_=tt_pv_vi_aiv_1")

american_beauty = media.Movie("American_Beauty",
"A sexually frustrated suburban father has a mid-life crisis after becoming infatuated with his daughter's best friend.", 
"http://image.prntscr.com/image/bcf29630b127403eac1890fdab90aae4.png", 
"http://www.imdb.com/title/tt0169547/videoplayer/vi788506137")

school_of_rock = media.Movie("School of Rock",
"After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school.", 
"https://cainpriest.files.wordpress.com/2013/11/the-school-of-rock1.jpg", 
"https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille ",
"A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.", 
"http://www.aflamfree.com/wp-content/uploads/2015/11/Ratatouille-2007-Arabic.jpg", 
"https://www.youtube.com/watch?v=uVeNEbh3A4U")

finding_nemo = media.Movie("Finding Nemo",
"After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.", 
"http://i.imgur.com/y0UN5jl.jpg", 
"http://www.imdb.com/title/tt0266543/videoplayer/vi2687214105?ref_=tt_ov_vi")

movies = [toy_story, avatar, american_beauty, school_of_rock, ratatouille, finding_nemo]
fresh_tomatoes.open_movies_page(movies)