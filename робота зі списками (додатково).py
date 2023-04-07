# задачі по роботам зі списками (додаткове завдання)

#№1
languages = [ 'Ukrainian', 'French', 'Bulgarian', 'Latvian']


print(languages)

print(sorted(languages))

languages.sort()
print(languages)

languages.reverse()
print(languages)

#№2
list = [1, 2, 3, 4, 5, 6, 7]

print(sum(list))


#№3
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
cities.insert(5, 'and')

print(cities)


cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
message = ', '.join(cities[:-1]) + ' and ' + cities[-1]

print(message)


#№4
numbers_string = input('5, 15, 25, 35, 45')
numbers = list(map(int, numbers_string.split()))
reverse_sorted_numbers = sorted(numbers, reverse=True)
reverse_sorted_number_string = ''.join(map(str, reverse_sorted_numbers))
reverse_sorted_number = int(reverse_sorted_number_string)


print(reverse_sorted_number)


#№5
professions = ['dancer', 'teacher', 'IT specialist', 'project manager', 'chef']

professions.reverse()
print(professions)

professions_sorted = sorted(professions)
print(professions_sorted)

professions.append('architector')
print(professions)

professions.remove('chef')
print(professions)


