
sisters=("asi","tutu","mita")
brothers=("dera","lul")
sibiling=sisters + brothers
print(sibiling)
print(len(sibiling))
parent=("aba","eme")
family_member=sibiling+parent
print(family_member)
sibilings=family_member[0:5]
parents=family_member[5:8]
fruits=("banana","orange")
vegetables=("tomato","onion")
animal=("dog","cat")
food_stuff_tp=fruits+vegetables+animal
food_stuff_ls=list(food_stuff_tp)
print(food_stuff_ls)
middle_item=food_stuff_ls[2:4]
print(middle_item)
first_three_item=food_stuff_tp[0:3]
last_three_item=food_stuff_tp[3:7]
print(first_three_item)
print(last_three_item)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)



