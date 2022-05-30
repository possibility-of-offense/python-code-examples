def filter_through(friends) :
    friends_to_come = []

    for friend in range(len(friends)) :
        if(friends[friend] != 'Friend is coming') :
            continue

        if type(friends[friend + 1]) == int :
            friends_to_come.append(f'Friend is coming at {friends[friend + 1]}') 

    for h in friends_to_come :
        print(h)

friends = ['Friend is coming', 20, 'Friend is coming', 10, 'Friend is not coming', None, 'Friend is coming', '25d']
filter_through(friends)