import csv
import random
players = 2
list=[]
index=[]
def gimme_car():
    carclasses=['E','D','C','B','A','S','R','P','X']
    carclass = random.choice(carclasses)
    print(f'Car Class: {carclass}')
    with open(f'FM6 list CSV{carclass}.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                list.append(row)
                line_count += 1
        n=1
        for _ in range (players):
            car = random.choice(list)
            print(f'\nPlayer {n}: {str(car[1])} {str(car[0])}\n')
            n+=1
gimme_car()