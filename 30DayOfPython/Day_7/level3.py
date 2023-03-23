age = [22, 19, 24, 25, 26, 24, 25, 24]
age_st=set(age)
print(age_st)
print(len(age) > len(age_st))
print("""string is combination of character , list is combination of ordered and mutable item
 tuple is a combination of ordered and immutable item  set is a combination unordered and mutable and unordered item 
 """)
sentence="I am a teacher and I love to inspire and teach people."
sentence_ls=sentence.split(" ")
sentence_st=set(sentence_ls)
print(sentence_st)
print(len(sentence_st))