it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

length_it_companies = len(it_companies)
print("Length of it_companies:", length_it_companies)

it_companies.add('Twitter')
print("it_companies after adding 'Twitter':", it_companies)

it_companies.update(['Snapchat', 'LinkedIn', 'Netflix'])
print("it_companies after adding multiple companies:", it_companies)

it_companies.remove('IBM')
print("it_companies after removing 'IBM':", it_companies)

it_companies.discard('NonExistentCompany')
