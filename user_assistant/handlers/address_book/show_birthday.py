def show_birthday(book):
    while True:
        try:
            days = int(input(f'Enter volume days :'))
            if days in range(1,365):
                break
            else:
                print('Days may be in interval 1-365')
                continue
        except:
           print(ValueError('Days may be integer volume'))

    print(book.show_birthday(days))