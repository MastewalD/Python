# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(len(it_companies))
it_companies_ls=list(it_companies)
it_companies_ls[0]="Twitter"
it_companies_st=set(it_companies_ls)
print(it_companies_st)
it_companies_st.update(["company1","company2","company3"])
print(it_companies_st)
it_companies_st.remove("company1")
print(it_companies_st)
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B),B.union(A))
print(A.symmetric_difference(B))
del A
del B






