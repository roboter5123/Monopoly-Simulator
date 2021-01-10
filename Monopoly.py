from sys import argv
import random
import datetime

try:

    scipt, max_rounds = argv

except ValueError:

    print("Enter an integer as a commandline argument")
    exit(1)

try:
    max_rounds = int(max_rounds)

except ValueError:
    print("Enter an integer as a commandline argument")
    exit(1)

###################################################################


def overflow(max, position, roll):

    if position + roll > max:
        position = -1 + roll - (max - position)
        return position

    else:
        return position + roll

#############################

def felder():

    positions = []

    for i in range(0, 40):
        positions.append(0)

    return positions

#############################

def jail(position, positions, log):

    if position == 30:

        positions[position] += 1
        log.write(f"Go to Jail ")
        position = 10
        positions[position] += 1
        return position, positions

    else:
        positions[position] += 1
        return position, positions

#############################

def community_chest(position, positions, log):

    draw = random.randint(1, 16)

    if draw == 1:

        positions[position] +=1
        log.write(f"Community card. Go to Jail ")
        position = 10
        return position, positions

    elif draw == 2:

        positions[position] +=1
        log.write(f"Community card. Go to Go ")
        position = 0
        return position, positions

    else:
        positions[position] += 1
        return position, positions

#############################

def chance(position, positions, log):

    draw = random.randint(1, 16)
    positions[position] +=1

    if draw == 1:

        log.write(f"Chance card. Go to Jail ")
        position = 10


    elif draw == 2:

        log.write(f"Chance card. Go to Go ")
        position = 0

    elif draw == 3:

        log.write(f"Chance card. Go to 24 ")
        position = 24

    elif draw == 4:

        log.write(f"Chance card. Go to 11 ")
        position = 11

    elif draw == 5:

        log.write(f"Chance card. Go to 5 ")
        position = 5

    elif draw == 6:

        log.write(f"Chance card. Go to 39 ")
        position = 39

    elif draw == 7:

        if position < 12 or position >= 28:

            log.write(f"Chance card. Go to 12 ")
            position = 12

        else:

            log.write(f"Chance card. Go to 28 ")
            position = 28

    elif draw == 8:

        if position >= 35 or position < 5:

            log.write(f"Chance card. Go to 5 ")
            position = 5

        elif position >=5 and position <15:

            log.write(f"Chance card. Go to 15 ")
            position = 15

        elif position >= 15 and position < 25:

            log.write(f"Chance card. Go to 25 ")
            position = 25

        elif position >= 25 and position < 35:

            log.write(f"Chance card. Go to 25 ")
            position = 35

    elif draw == 9:

        if position != 36:

            position -=3
            log.write(f"Chance card. Go to {position - 3} ")

        else:

            log.write(f"Chance card. Go to {position - 3} ")
            position -= 3
            positions[position] +=1
            position, positions = community_chest(position, positions, log)



#Continue here!!!! go back 3 spaces!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    else:

        log.write(f"Chance card.No Movement ")

    positions[position] +=1
    return position, positions
#####################################################################


rounds = 0
position = 0
max_position = 39
dice = 0
datum = datetime.datetime.now()
logname = f"log_{datum.strftime('%H-%M-%S')}.txt"
log = open(logname, "x")

positions = felder()


#######################################################################



for rounds in range(0, max_rounds):

    log.write(f"position vor wurf: {position} ")
    dice = random.randint(2, 12)
    log.write(f"Wurf: {dice} ")
    position = overflow(max_position, position, dice)
    log.write(f"Position nach wurf ohne Jail: {position} ")

    if position == 2 or position == 17 or position == 3:
        position, positions = community_chest(position, positions, log)

    elif position == 7 or position == 22 or position == 36:

        position, positions = chance(position, positions, log)

    else:
        position, positions = jail(position, positions, log)

    log.write(f"Position: {position}\n")

log.write(f"\n\n")

for i in positions:

    log.write(f"{i}\n")

log.write(f"\n\n Welches Feld wie oft: {positions}\n")
log.close()
