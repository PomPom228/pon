import random

class Student:
    def __init__(self, name):
        self.name=name
        self.gladness= 50
        self.progress= 0
        self.alive=True

    def to_feed(self):
        print("Feed me!")
        self.progress += 1
        self.gladness-= 3

    def to_play(self):
        print("Lets play!")
        print("Rest time!")
        self.gladness += 5
        self.progress -= 0.5

    def to_sleep(self):
        print("Rest time!")
        self.gladness += 3

    def is_alive(self):
        if self.progress < -0.5:
            print('Oh no! My cat lived me...')
            self.alive = False

        elif self.gladness <=0:
            print('Depression...')
            self.alive = False

        elif self.progress > 5:
            print('My cat so happy!!!')
            self.alive=False

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress)}')

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "live"
        print(f'{day:^50}')
        print('1 - to feed')
        print('2 - to play')
        print('3 - to sleep')
        live_cube = (input('Enter your choise'))
        if live_cube == '1':
            print('You entered 1 variant (feed)')
            self.to_feed()
        elif live_cube == '2':
            print('You entered 2 variant (play)')
            self.to_play()
        elif live_cube == '3':
            print('You entered 3 variant (sleep')
            self.to_sleep()
        else:
            print('Not correct choice!!')
        self.end_of_day()
        self.is_alive()

nick=Student(name='Nick')
for day in range(7):
    if nick.alive==False:
        print('Lose...')
        break
    nick.live(day)
