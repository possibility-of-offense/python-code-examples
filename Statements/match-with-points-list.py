points = [[1, 2], [1, 3], [1, 10], [3, 12], [5, 32]]
# points = [[1, 5]]

match points :
    case [] :
        print('No points')
    case [[1, y]] :
        print(f'Only one point with {y} coordinate on the y axis')
    case [[1, y1], [1, y2]] :
        print(f'Two points with coordinates of {y1} and {y2} on y axis')
    case [[1, y1], [1, y2], [1, y3]] :
        print(f'Three points with coordinates of {y1}, {y2} and {y3} on y axis')
    case [[1, y1], [1, y2], [1, y3], *rest] :
        out = 'The leftover point is with coordinate of '
        for p in range(len(rest)) :
            comma = ', ' if p < len(rest) -1 else ''
            out += str(rest[p][0]) + ' ' + str(rest[p][1]) + comma

            if(p == len(rest) - 1) :
                out += '!'
    # this case is important if you don't have the rest parameter in the previous case
    # case _ :
    #     points_on_y = []

    #     for point in range(len(points)) :
    #         if points[point][0] != 1 :
    #             continue
    #         points_on_y.append({'index': point + 1, 'point': points[point]})

    #     for point in points_on_y : 
    #         print('The point {ind} is on the y axis with coordinate of {point}'.format(ind = point['index'], point = point['point'][1]))

    case _ :
        print('Something else')

print(out)