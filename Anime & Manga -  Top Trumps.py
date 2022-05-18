import requests
import random
from jikanpy import Jikan
jikan = Jikan()

compare_anime= input("Would you like to compare random Animes? (Yes/No) ")
if compare_anime == ('No'):
   compare_manga = input("Would you like to compare random Mangas instead? (Yes/No)  ")
   if compare_manga == ('No'):
       print('GO AWAY!')
       exit()

   if compare_manga == ('Yes'):
        def random_manga():
           url = 'https://api.jikan.moe/v4/random/manga'
           response = requests.get(url)
           manga = response.json()
           return {
               'Title': manga['data']['title'],
               'Rank': manga['data']['rank'],
               'Popularity': manga['data']['popularity'],
               'Score': manga['data']['score']
           }

        def run():
            my_manga = random_manga()

            print('You were given: {}.'.format(my_manga['Title']),
            'This Manga has a rank of {},'.format(my_manga['Rank']),
            'a popularity of {}'.format(my_manga['Popularity']),
            'and a score of {}'.format(my_manga['Score']))

            stat_choice = input('Which stat do you want to use? (Rank, Popularity, Score) ')

            opponent_manga = random_manga()

            print('The opponent chose: {}.'.format(opponent_manga['Title']),
            'This Manga has a rank of {},'.format(opponent_manga['Rank']),
            'a popularity of {}'.format(opponent_manga['Popularity']),
            'and a score of {}'.format(opponent_manga['Score']))

            my_stat = my_manga[stat_choice]
            opponent_stat = opponent_manga[stat_choice]

            if my_stat == None:
                my_stat = 0
                print(my_stat)
            else:
                print(my_stat)

            if opponent_stat == None:
                opponent_stat = 0
                print(opponent_stat)
            else:
                print(opponent_stat)

            if stat_choice == 'Rank':
                if my_stat < opponent_stat:
                    print('You Win!')
                elif my_stat > opponent_stat:
                    print('You Lose!')
                else:
                    print('Draw!')

            if stat_choice == 'Popularity':
                if my_stat > opponent_stat:
                    print('You Win!')
                elif my_stat < opponent_stat:
                    print('You Lose!')
                else:
                    print('Draw!')

            if stat_choice == 'Score':
                if my_stat > opponent_stat:
                    print('You Win!')
                elif my_stat < opponent_stat:
                    print('You Lose!')
                else:
                    print('Draw!')
        run()
   exit()

if compare_anime == ('Yes'):

    def random_anime():
        url='https://api.jikan.moe/v4/random/anime'
        response = requests.get(url)
        anime = response.json()
        return {
        'Title':anime['data']['title'],
        'Rank':anime['data']['rank'],
        'Popularity':anime['data']['popularity'],
        'Score':anime['data']['score']
        }

    def run():

        my_anime = random_anime()

        print ('You were given: {}.'.format(my_anime['Title']),
        'This Anime has a rank of {}'.format(my_anime['Rank']),
        'a popularity of {}'.format(my_anime['Popularity']),
        'and a score of {}'.format(my_anime['Score']))


        stat_choice = input('Which stat do you want to use? (Rank, Popularity, Score) ')

        opponent_anime = random_anime()
        print ('The opponent chose: {}.'.format(opponent_anime['Title']),
        'This Anime has a rank of {}'.format(opponent_anime['Rank']),
        'a popularity of {}'.format(opponent_anime['Popularity']),
        'and a score of {}'.format(opponent_anime['Score']))

        my_stat = my_anime[stat_choice]
        opponent_stat = opponent_anime[stat_choice]

        if my_stat == None:
            my_stat = 0
            print(my_stat)
        else:
            print(my_stat)

        if opponent_stat == None:
            opponent_stat = 0
            print(opponent_stat)
        else:
            print(opponent_stat)

        if stat_choice == 'Rank':
            if my_stat < opponent_stat:
                print('You Win!')
            elif my_stat > opponent_stat:
                print('You Lose!')
            else:
                print('Draw!')

        if stat_choice == 'Popularity':
            if my_stat > opponent_stat:
                print('You Win!')
            elif my_stat < opponent_stat:
                print('You Lose!')
            else:
                print('Draw!')

        if stat_choice == 'Score':
            if my_stat > opponent_stat:
                print('You Win!')
            elif my_stat < opponent_stat:
                print('You Lose!')
            else:
                print('Draw!')


    run()
    exit()