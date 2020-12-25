def info(first_name, last_name, year_of_birth, city, mail, phone):
    print(
        f'first name - {first_name}, last name - {last_name}, year of birth - {year_of_birth}, city - {city}, mail - {mail}, phone - {phone}')


info(first_name=input('enter first name '), last_name=input('enter last name '),
     year_of_birth=int(input('enter year of birth ')), city=input('enter your city '), mail=input('enter your mail '),
     phone=int(input('enter your phone number ')))
