# FIRST DEFINITION
# def get_mode(l) :
#     sort_list = sorted(l)

#     color = ''
#     num_times = 1

#     temp_color = sort_list[0]
#     temp_num_times = 1
#     l = len(sort_list)

#     for ind, val in enumerate(sort_list) :
        
#         if ind == 0 :
#             continue
#         else :
#             if val == temp_color :
#                 temp_num_times = temp_num_times + 1

#                 if ind == l - 1:
#                     num_times = temp_num_times
#                     color = temp_color

#             else :            
#                 if temp_num_times > num_times :
#                     num_times = temp_num_times
#                     color = temp_color

#                 temp_color = val
#                 temp_num_times = 1

    
#     print(color, num_times)

# SECOND DEFINITION

# def get_mode(l) :
#     obj = {}

#     for val in l :
#         if val in obj :
#             obj[val] = obj[val] + 1
#         else :
#             obj[val] = 1

#     max_count = 0
#     color = ''

#     for val, count in obj.items() :
#         if count > max_count :
#             max_count = count
#             color = val

#     print('The color {color} is being repeated {n} times!'.format(color = color.upper(), n = max_count))

get_mode(["green",
"green",
"green",
"yellow",
"green",
"yellow",
"yellow",
"yellow",
"yellow",
"yellow",
"yellow",
"red",
"green",
"red", 
"green", 
"yellow"])