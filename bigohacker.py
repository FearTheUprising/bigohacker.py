import time
import random
def location_finder():
    print("""
Please tell me what operation you would like to perform.\n
1. IP finder
2. Beans adder
3. Brute-Forcing
""")
    
    choice = int(input("Please enter a number (1 - 3): "))

    if choice == 1:
        ip_s = [
        '192.168.1.45',
        '10.0.0.105',
        '172.16.254.3',
        '203.0.113.9'
        ]

        account_name = input("Please the name of the account you would like to find the IP of: ")
        user_input = input("Would you like to do anything further: ")
        if user_input == 'Y':
            print("Please tell me what you would like to to do.")
        elif user_input == 'N':
            pass
        print(f'Thanks, you have entered {account_name}')
        gen_ip = random.randint(0, len(ip_s) - 1)
        ip_selection = ip_s[gen_ip]
        time.sleep(2)
        for i in range(3):
            print("Searching", end='', flush=True)
            print(".", end='', flush=True)
            time.sleep(2)
        print("\n")
        print(f'For the name of {account_name}, the IP is {ip_selection}.')
    elif choice == 2:
        print("What is the name of the account: ")
        account = input("")
        print(f'You have entered {account}.')
        print("How many means would you like added to this account: ")
        beans = int(input("Input a number (1 - 1000): "))
        if beans >= 1000:
            print("Please enter a smaller number. This could result in account being banned.")
            print("Please enter an amount smaller than or equal to 1000")
            beans = int(input("Enter a number: "))

        print(f'You have entered {beans} beans.')
        time.sleep(1)
        print("Bypassing app restrictions...")
        time.sleep(4)
        print("Injecting scripts...")
        time.sleep(3)
        print("Injecting BEANS.PAYLOADER")
        time.sleep(4)
        print("User should expect to receive their beans in 24 hours.")
    elif choice == 3:
        print("This will Brute-Force an account using leaked passwords.")
        time.sleep(3)
        print("Conneting to app...")
        for i in range(6):
            print(".", end='', flush=True)
        print("\n")
        time.sleep(3)
        print("Connected to: https://www.bigo.tv/")
        print("""
How would you like to hack this account: 
              
1. ID
2. Account name\n
        
Choose your method
        """)

        passwords = [
            'summer2021',
            'password123',
            'qwertyuiop',
            'iloveyou123',
            'admin@123',
            'letmein456',
            'welcome!123',
            'monkey1234',
            'football22',
            'abc12345',
            'dragonfly77',
            'sunshine123',
            'trustno1!',
            'baseball2020',
            'superman99',
            'starwars2022',
            'hello2021!',
            'masterkey123',
            'ninja555',
            'princess!23',
            'ilovejava22',
            '!password!',
            'batmanForever',
            'qazwsxedc123',
            'hunter2021',
            'michael123',
            'football2022',
            'abc123!',
            'letmein!',
            'secretpass!',
            'love123456',
            'pass@1234',
            '123qweasd',
            'freedom2021',
            'soccerfan22',
            'baseball@home',
            'forever2021',
            'sunshine2022!',
            'welcome!1234',
            'newyork2022',
            'dragon12345',
            'chocolate99',
            'sparrow2020',
            'linkedin123!',
            'qwerty@123',
            'monkey2020!',
            'jordan!23',
            'guitar!567',
            'windows@2021',
            'password!',
            'masterkey2020',
            'loveyoumore2022',
            'happytime2022',
            'letmein@123',
            'asdfghjkl123',
            'puppylover!',
            'trustme2021',
            'starwarsfan2020',
            'sunshine22!',
            'computer!123',
            'catlover2021',
            'footballfan22',
            'just4fun123',
            'basketball99',
            'iloveyou@2021',
            'kitty123456',
            'welcomeagain1',
            'redbluegreen123',
            'masterpass@2021',
            'letmein99!',
            'freedom!123',
            'gameon2022',
            'abcdefg123!',
            'qwerty2021!',
            'kingkong123',
            'soccer2020!',
            'no1canstopme',
            'hotdog99!',
            'flower2021!',
            'newbeginning2022',
            'bigboss123!',
            'elephant777',
            'icantremember123',
            'mickeymouse99',
            'n0tsecure!',
            'lovemusic123',
            'ilovefood@2022',
            'brightsun99',
            'butterfly1234',
            'admin@1234',
            'nooneknows123',
            'tiger!555',
            'helloworld99',
            'ilovecats!22',
            'gaminglife2021',
            'freedom22!',
            'yayfootball123',
            'footballfan@2022',
            'chocolate!99',
            'sunset@2021'
        ]

        counter = 1
        try:
            choice = int(input("Please choose a number (1 - 2): "))
        except ValueError:
            print("Invalid input! Please input a number: ")
            choice = None


        if choice == 1:
            time.sleep(3)
            id = input("What is their ID: ")
            print(f'You have entered {id}!')
            for passwords in passwords:
                print(f'Trying password: "{passwords}" for account: {id}. Attempt {counter}!')
                counter+= 1
                time.sleep(5)
                print("Brute-Force attempt failed, trying the next password...")
            time.sleep(5)
        elif choice == 2:
            time.sleep(3)
            time.sleep(3)
            name = input("What is their account name: ")
            print(f'You have enterd {name}!')
            time.sleep(3)
            for passwords in passwords:
                print(f'Trying password: "{passwords}" for account: {name}. Attempt {counter}!')
                counter+= 1
                time.sleep(5)
                print("Brute-Force attempt failed, trying the next password...")
        else:
            print("Invalid choice! Please choose option 1 or 2.")


location_finder()

