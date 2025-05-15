from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Adds sample movies to the database'

    def handle(self, *args, **kwargs):
        movies = [
            {
                'title': 'Pulp Fiction',
                'description': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
                'image': 'https://image.tmdb.org/t/p/original/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg',
                'year': 1994,
                'director': 'Quentin Tarantino',
            },
            {
                'title': 'The Dark Knight',
                'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                'image': 'https://image.tmdb.org/t/p/original/qJ2tW6WMUDux911r6m7haRef0WH.jpg',
                'year': 2008,
                'director': 'Christopher Nolan',
            },
            {
                'title': 'Inception',
                'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
                'image': 'https://image.tmdb.org/t/p/original/8IB2e4r4oVhHnANbnm7O3Tj6tF8.jpg',
                'year': 2010,
                'director': 'Christopher Nolan',
            },
            {
                'title': 'Fight Club',
                'description': 'An insomniac office worker and a devil-may-care soap maker form an underground fight club.',
                'image': 'https://image.tmdb.org/t/p/original/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg',
                'year': 1999,
                'director': 'David Fincher',
            },
            {
                'title': 'Forrest Gump',
                'description': 'The presidencies of Kennedy and Johnson, the Vietnam War, and more through the eyes of an Alabama man.',
                'image': 'https://image.tmdb.org/t/p/original/saHP97rTPS5eLmrLQEcANmKrsFl.jpg',
                'year': 1994,
                'director': 'Robert Zemeckis',
            },
            {
                'title': 'The Matrix',
                'description': 'A computer hacker learns about the true nature of his reality and his role in the war against its controllers.',
                'image': 'https://image.tmdb.org/t/p/original/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg',
                'year': 1999,
                'director': 'Lana Wachowski, Lilly Wachowski',
            },
            {
                'title': 'Goodfellas',
                'description': 'The story of Henry Hill and his life in the mob.',
                'image': 'https://image.tmdb.org/t/p/original/aKuFiU82s5ISJpGZp7YkIr3kCUd.jpg',
                'year': 1990,
                'director': 'Martin Scorsese',
            },
            {
                'title': 'The Lord of the Rings: The Return of the King',
                'description': 'Gandalf and Aragorn lead the World of Men against Sauron.',
                'image': 'https://image.tmdb.org/t/p/original/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg',
                'year': 2003,
                'director': 'Peter Jackson',
            },
            {
                'title': 'The Lord of the Rings: The Fellowship of the Ring',
                'description': 'A meek Hobbit and eight companions set out on a journey to destroy the One Ring.',
                'image': 'https://image.tmdb.org/t/p/original/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg',
                'year': 2001,
                'director': 'Peter Jackson',
            },
            {
                'title': 'The Lord of the Rings: The Two Towers',
                'description': 'While Frodo and Sam edge closer to Mordor, the divided fellowship makes a stand against Sauron.',
                'image': 'https://image.tmdb.org/t/p/original/5VTN0pR8gcqV3EPUHHfMGnJYN9L.jpg',
                'year': 2002,
                'director': 'Peter Jackson'
            },
            {
                'title': 'Interstellar',
                'description': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
                'image': 'https://image.tmdb.org/t/p/original/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg',
                'year': 2014,
                'director': 'Christopher Nolan',
            },
            {
                'title': 'Se7en',
                'description': 'Two detectives hunt a serial killer who uses the seven deadly sins as his motives.',
                'image': 'https://image.tmdb.org/t/p/original/6yoghtyTpznpBik8EngEmJskVUO.jpg',
                'year': 1995,
                'director': 'David Fincher',
            },
            {
                'title': 'The Silence of the Lambs',
                'description': 'A young F.B.I. cadet must confide in an incarcerated and manipulative killer.',
                'image': 'https://image.tmdb.org/t/p/original/uS9m8OBk1A8eM9I042bx8XXpqAq.jpg',
                'year': 1991,
                'director': 'Jonathan Demme',
            },
            {
                'title': 'The Green Mile',
                'description': 'The lives of guards on Death Row are affected by one of their charges.',
                'image': 'https://image.tmdb.org/t/p/original/velWPhVMQeQKcxggNEU8YmIo52R.jpg',
                'year': 1999,
                'director': 'Frank Darabont',
            },
            {
                'title': 'Gladiator',
                'description': 'A former Roman General sets out to exact vengeance against the corrupt emperor.',
                'image': 'https://image.tmdb.org/t/p/original/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg',
                'year': 2000,
                'director': 'Ridley Scott',
            },
            {
                'title': 'The Prestige',
                'description': 'After a tragic accident, two stage magicians engage in a battle to create the ultimate illusion.',
                'image': 'https://image.tmdb.org/t/p/original/bdN3gXuIZYaJP7ftKK2sU0nPtEA.jpg',
                'year': 2006,
                'director': 'Christopher Nolan',
            },
            {
                'title': 'Whiplash',
                'description': 'A promising young drummer enrolls at a cut-throat music conservatory.',
                'image': 'https://image.tmdb.org/t/p/original/6uSPcdGNA2A6vJmCagXkvnutegs.jpg',
                'year': 2014,
                'director': 'Damien Chazelle',
            },
            {
                'title': 'The Intouchables',
                'description': 'After he becomes a quadriplegic from a paragliding accident, an aristocrat hires a young man from the projects to be his caregiver.',
                'image': 'https://image.tmdb.org/t/p/original/323BP0itpxTsO0skTwdnVmf7YC9.jpg',
                'year': 2011,
                'director': 'Olivier Nakache, Éric Toledano',
            },
            {
                'title': 'Parasite',
                'description': 'Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.',
                'image': 'https://image.tmdb.org/t/p/original/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg',
                'year': 2019,
                'director': 'Bong Joon Ho',
            },
            {
                'title': 'Joker',
                'description': 'In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society.',
                'image': 'https://image.tmdb.org/t/p/original/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg',
                'year': 2019,
                'director': 'Todd Phillips',
            },
            {
                'title': 'Avengers: Endgame',
                'description': 'After the devastating events of Avengers: Infinity War, the universe is in ruins.',
                'image': 'https://image.tmdb.org/t/p/original/or06FN3Dka5tukK1e9sl16pB3iy.jpg',
                'year': 2019,
                'director': 'Anthony Russo, Joe Russo',
            },
            {
                'title': 'Braveheart',
                'description': 'Scottish warrior William Wallace leads his countrymen in a rebellion to free his homeland from the tyranny of King Edward I of England.',
                'image': 'https://image.tmdb.org/t/p/original/or1gBugydmjToAEq7OZY0owwFk.jpg',
                'year': 1995,
                'director': 'Mel Gibson',
            },
            {
                'title': 'The Lion King',
                'description': 'Lion prince Simba and his father are targeted by his bitter uncle.',
                'image': 'https://image.tmdb.org/t/p/original/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg',
                'year': 1994,
                'director': 'Roger Allers, Rob Minkoff',
            },
            {
                'title': 'The Pianist',
                'description': 'A Polish Jewish musician struggles to survive the destruction of the Warsaw ghetto of World War II.',
                'image': 'https://image.tmdb.org/t/p/original/2hFvxCCWrTmCYwfy7yum0GKRi3Y.jpg',
                'year': 2002,
                'director': 'Roman Polanski',
            },
            {
                'title': 'Terminator 2: Judgment Day',
                'description': 'A cyborg, identical to the one who failed to kill Sarah Connor, must now protect her teenage son.',
                'image': 'https://image.tmdb.org/t/p/original/5M0j0B18abtBI5gi2RhfjjurTqb.jpg',
                'year': 1991,
                'director': 'James Cameron',
            },
            {
                'title': 'Back to the Future',
                'description': 'Marty McFly, a 17-year-old high school student, is accidentally sent 30 years into the past.',
                'image': 'https://image.tmdb.org/t/p/original/qvktm0BHcnmDpul4Hz01GIazWPr.jpg',
                'year': 1985,
                'director': 'Robert Zemeckis',
            },
            {
                'title': 'Alien',
                'description': 'After a space merchant vessel receives an unknown transmission as a distress call, one of the crew is attacked by a mysterious lifeform.',
                'image': 'https://image.tmdb.org/t/p/original/vfrQk5IPloGg1v9Rzbh2Eg3VGyM.jpg',
                'year': 1979,
                'director': 'Ridley Scott',
            },
            {
                'title': 'WALL·E',
                'description': 'In the distant future, a small waste-collecting robot inadvertently embarks on a space journey.',
                'image': 'https://image.tmdb.org/t/p/original/hbhFnRzzg6ZDmm8YAmxBnQpQIPh.jpg',
                'year': 2008,
                'director': 'Andrew Stanton',
            },
            {
                'title': 'Oldboy',
                'description': 'After being kidnapped and imprisoned for fifteen years, Oh Dae-Su is released, only to find that he must find his captor in five days.',
                'image': 'https://image.tmdb.org/t/p/original/pWDtjs568ZfOTMbURQBYuT4Qxka.jpg',
                'year': 2003,
                'director': 'Park Chan-wook',
            },
            {
                'title': 'The Shining',
                'description': 'A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence.',
                'image': 'https://image.tmdb.org/t/p/original/nRj5511mZdTl4saWEPoj9QroTIu.jpg',
                'year': 1980,
                'director': 'Stanley Kubrick',
            },
            {
                'title': 'The Usual Suspects',
                'description': 'A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat.',
                'image': 'https://image.tmdb.org/t/p/original/bUPmtQzrRhzqYySeiMpv7GurAfm.jpg',
                'year': 1995,
                'director': 'Bryan Singer',
            },
            {
                'title': 'Léon: The Professional',
                'description': 'Mathilda, a 12-year-old girl, is reluctantly taken in by Léon, a professional assassin.',
                'image': 'https://image.tmdb.org/t/p/original/yI6X2cCM5YPJtxMhUd3dPGqDAhw.jpg',
                'year': 1994,
                'director': 'Luc Besson',
            },
            {
                'title': 'Casablanca',
                'description': 'A cynical expatriate American cafe owner struggles to decide whether or not to help his former lover and her fugitive husband escape the Nazis in French Morocco.',
                'image': 'https://image.tmdb.org/t/p/original/5K7cOHoay2mZusSLezBOY0Qxh8a.jpg',
                'year': 1942,
                'director': 'Michael Curtiz',
            },
            {
                'title': 'Cinema Paradiso',
                'description': 'A filmmaker recalls his childhood when falling in love with the pictures at the cinema of his home village.',
                'image': 'https://image.tmdb.org/t/p/original/8SRUfRUi6x4O68n0VCbDNRa6iGL.jpg',
                'year': 1988,
                'director': 'Giuseppe Tornatore',
            },
            {
                'title': 'Life Is Beautiful',
                'description': 'When an open-minded Jewish librarian and his son become victims of the Holocaust, he uses a perfect mixture of will, humor, and imagination to protect his son.',
                'image': 'https://image.tmdb.org/t/p/original/74hLDKjD5aGYOotO6esUVaeISa2.jpg',
                'year': 1997,
                'director': 'Roberto Benigni',
            },
            {
                'title': 'Modern Times',
                'description': 'The Tramp struggles to live in modern industrial society with the help of a young homeless woman.',
                'image': 'https://image.tmdb.org/t/p/original/7uoiKOEjxBBW0AgDGQWrlfGQ90w.jpg',
                'year': 1936,
                'director': 'Charles Chaplin',
            },
            {
                'title': 'Rear Window',
                'description': 'A wheelchair-bound photographer spies on his neighbors from his apartment window and becomes convinced one of them has committed murder.',
                'image': 'https://image.tmdb.org/t/p/original/qitnZcLP7C9DLRuPpmvZ7GiEjJN.jpg',
                'year': 1954,
                'director': 'Alfred Hitchcock',
            },
            {
                'title': 'The Lives of Others',
                'description': 'In 1984 East Berlin, an agent of the secret police, conducting surveillance on a writer and his lover, finds himself becoming increasingly absorbed by their lives.',
                'image': 'https://image.tmdb.org/t/p/original/jQ2iUsXI2jmUcOFGjOaONCLwaVp.jpg',
                'year': 2006,
                'director': 'Florian Henckel von Donnersmarck',
            },
            {
                'title': 'Grave of the Fireflies',
                'description': 'A young boy and his little sister struggle to survive in Japan during World War II.',
                'image': 'https://image.tmdb.org/t/p/original/k9tv1rXZbOhH7eiCk378x61kNQ1.jpg',
                'year': 1988,
                'director': 'Isao Takahata',
            }
        ]
        
        for movie_data in movies:
            movie, created = Movie.objects.get_or_create(
                title=movie_data['title'],
                defaults={
                    'description': movie_data['description'],
                    'image': movie_data['image'],
                    'year': movie_data['year'],
                    'director': movie_data['director'],
                }
            )
            
            if not created:
                # Update the image URL even if the movie exists
                movie.image = movie_data['image']
                movie.save()
                self.stdout.write(self.style.WARNING(f'Updated image for movie "{movie.title}"'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully added movie "{movie.title}"'))

        self.stdout.write(self.style.SUCCESS('Successfully added sample movies')) 