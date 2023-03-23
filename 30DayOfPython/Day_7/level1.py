# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


print(len(it_companies))
it_companies_ls=list(it_companies)
it_companies_ls[0]="Twitter"
it_companies_st=set(it_companies_ls)
print(it_companies_st)
it_companies_st.update(["company1","company2","company3"])
print(it_companies_st)
it_companies_st.remove("company1")
print(it_companies_st)






