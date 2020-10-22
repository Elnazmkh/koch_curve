
def Restaurant_Ranking(list1, list2):


    max_rank = len(list1 ) +len(list2)
    selected_restaurant = "None"

    for i ,item in enumerate(list1):
        for j ,jtem in enumerate(list2):
            if item == jtem and i+ j < max_rank:
                selected_restaurant = item
                max_rank = i + j

    print(max_rank)
    return selected_restaurant


# ----------------------------------

# Creating my favorite list

my_list = []
print("Please enter your favorite restaurants (Press 0 when finished) : ")
a = input()
while (a != "0"):
    a.lower()
    my_list.append(a)
    a = input()

# Creating my friend's favorite list

my_friends_list = []
print("Please enter your friend's favorite restaurants (Press 0 when finished) : ")
a = input()
while (a != "0"):
    a.lower()
    my_friends_list.append(a)
    a = input()

# printing out both lists
print(my_list, my_friends_list)

# choosing the least combined item
print("The least combined rank restaurant is : " + Restaurant_Ranking(my_list, my_friends_list))