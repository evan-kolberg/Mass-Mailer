import yagmail, csv
with open('csv.csv') as file:
	reader = csv.reader(file); next(reader); user = 'massmailer69@gmail.com'; yag = yagmail.SMTP(user=user, password=input(f'Enter a password for {user} and press enter '))
	for (name, email, message) in reader: yag.send(to=email, subject=f'Hey {name}', contents=message); print('Email sent successfully')