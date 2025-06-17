commend = ''
current_status = ''
while True:
    command = input('> ').lower()
    if command == 'start':
        if current_status == 'start':
            print("Car is already started")
        else:
            current_status = 'start'
            print('Car started...')
    elif command == 'stop':
        if current_status == 'stop':
            print("Car is already stopped")
        else:
            current_status = 'stop'
            print('Car stopped.')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command == 'quit':
        break
    else:
        print("sorry, I don't understand that!")

