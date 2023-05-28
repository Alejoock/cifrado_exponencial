from keycode import KeyCode
from encryption import Encryption



enc = Encryption()

kc = KeyCode()
kc()
enc.key_code = kc
print(kc)
enc.message = "Texto de prueba"

enc.encrypt_message()
enc.decipher_message()











def main():
    pass


if __name__ == '__main__':
    try:
        print('\n\tGreetings! ')
        main()
        
    except KeyboardInterrupt:
        os.system('clear')
        input('\n\n\t\tWhat happened!?')
        os.system('clear')
        quit()
        