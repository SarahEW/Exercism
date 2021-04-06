days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

gifts = ['a Partridge in a Pear Tree', 'two Turtle Doves', 'three French Hens', 'four Calling Birds',\
         'five Gold Rings', 'six Geese-a-Laying', 'seven Swans-a-Swimming', 'eight Maids-a-Milking',\
         'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping', 'twelve Drummers Drumming']

def recite(start_verse, end_verse):
    gifts_given = []
    song = []
    for i in range(start_verse, end_verse+1):
        if i == 1: # first verse does not need an and.
            song = ['On the {} day of Christmas my true love gave to me: {}.'.format(days[0], gifts[0])]
        else:
            day = days[i-1]
            gifts_given = gifts[1:i]
            gifts_given_string = ', '.join(reversed(gifts_given)) + ', and ' + gifts[0]
            verse = 'On the {} day of Christmas my true love gave to me: {}.'.format(day, gifts_given_string)
            song.append(verse)
    return song

print(recite(1,12))