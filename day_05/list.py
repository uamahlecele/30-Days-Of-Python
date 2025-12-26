# #Day 5 of 30 Days Python

# #Exercises: Day 5

# #1.

# empty_list = []

# #2.

# list_five = ["Amahlemandosi", "Cele", "Creative Director", 24, "Single"]

# #3.
# print(list_five)
# print(len(list_five))

# #4.

# # *rest unpacks whatever might be outstanding in a list

# print(list_five[0],list_five[2], list_five[-1])

# #5.

# mixed_data_types = ["Amahlemandosi Thabo",24,"1.76 Meters", "Single", "236 Mfeme Road"]

# #6.
# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# #7.

# print(f"IT Companies:",it_companies)

# #8.

# print("No. of companies:", len(it_companies))

# #9.

# print("First, Middle, Last:", it_companies[0],it_companies[4],it_companies[-1])

# #10.

# it_companies[0] = "Khumbuza"
# print(it_companies)

# #11.

# it_companies.append("Velaphi")
# print(it_companies)

# #12.

# it_companies.insert(4,"A24")
# print(it_companies)

# #13.

# print(it_companies[-1].upper())

# #14.

# print("#".join(it_companies))

# #15.


# for i in it_companies:
#     company = "Velaphi"
#     if i == company:
#         print("Exists")
#         break
#     else:
#         continue

# #16.

# print(sorted(it_companies))

# #17.

# print(*reversed(it_companies))

# #18.

# print(it_companies[0:3])

# #19.

# print(it_companies[-4:-1])

# #20.

# print(it_companies[4:7])

# #21.
# it_companies.pop(0)
# print(it_companies)

# #22.

# it_companies.pop(5)
# print(it_companies)

# #23.

# it_companies.pop(-1)
# print(it_companies)

# #24.
# it_companies.clear()
# print(it_companies)

# #25.
# del it_companies

# #26.

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# joined_list= front_end+back_end
# print(joined_list)

# #27.

# full_stack = joined_list.copy()
# full_stack.insert(5,"Python")
# full_stack.insert(6,"SQL")

# print("Fullstack:",full_stack)

#Exercises: Level 2.
 
#1.

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#sorting the list
ages.sort()
print(ages)
print("Max:",ages[-1],"\nMin:",ages[0])
ages.append(19)
ages.append(26)
ages.sort()
print(ages)

print(f"Median: {(ages[4]+ages[5])//2}")

print(f"Average Age: {sum(ages)//len(ages)}")

print(f"Range: {max(ages)-min(ages)}")

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

#Middle country
print(f"Middle country: {countries[len(countries)//2]}")

print(len(countries))

print(f"First Half:\n{countries[:len(countries)//2]}")

print(f"Second Half:\n{countries[len(countries)//2:-1]}")

countries_2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

print("First Three:\n",*countries_2[0:3])
print(f"Scandanavian:\n{countries_2[3:7]}")