# example.p
def connect_to_db():
    # Password hardcoded (bad practice)
    password = "supersegreta123"
    print("Connettendo al database con password:", password)

def execute_command(cmd):
    # Uso pericoloso di eval (rischio di codice arbitrario)
    eval(cmd)

def main():
    connect_to_db()
    # Comando potenzialmente pericoloso passato a eval
    execute_command("print('Esempio di comando eseguito')")
    execute_command("os.system('rm -rf /')")  # potenziale rischio!

if __name__ == "__main__":
    main()
def connect_to_db():
    # Password hardcoded (bad practice)
    password = "supersegreta123"
    print("Connettendo al database con password:", password)

def execute_command(cmd):
    # Uso pericoloso di eval (rischio di codice arbitrario)
    eval(cmd)

def main():
    connect_to_db()
    # Comando potenzialmente pericoloso passato a eval
    execute_command("print('Esempio di comando eseguito')")
    execute_command("os.system('rm -rf /')")  # potenziale rischio!

if __name__ == "__main__":
    main()
def connect_to_db():
    # Password hardcoded (bad practice)
    password = "supersegreta123"
    print("Connettendo al database con password:", password)

def execute_command(cmd):
    # Uso pericoloso di eval (rischio di codice arbitrario)
    eval(cmd)

def main():
    connect_to_db()
    # Comando potenzialmente pericoloso passato a eval
    execute_command("print('Esempio di comando eseguito')")
    execute_command("os.system('rm -rf /')")  # potenziale rischio!

if __name__ == "__main__":
    main()
def connect_to_db():
    # Password hardcoded (bad practice)
    password = "supersegreta123"
    print("Connettendo al database con password:", password)

def execute_command(cmd):
    # Uso pericoloso di eval (rischio di codice arbitrario)
    eval(cmd)

def main():
    connect_to_db()
    # Comando potenzialmente pericoloso passato a eval
    execute_command("print('Esempio di comando eseguito')")
    execute_command("os.system('rm -rf /')")  # potenziale rischio!

if __name__ == "__main__":
    main()
def connect_to_db():
    # Password hardcoded (bad practice)
    password = "supersegreta123"
    print("Connettendo al database con password:", password)

def execute_command(cmd):
    # Uso pericoloso di eval (rischio di codice arbitrario)
    eval(cmd)

def main():
    connect_to_db()
    # Comando potenzialmente pericoloso passato a eval
    execute_command("print('Esempio di comando eseguito')")
    execute_command("os.system('rm -rf /')")  # potenziale rischio!

if __name__ == "__main__":
    main()
def connect_to_db():
    # Password hardcoded (bad practice)
    password = "supersegreta123"
    print("Connettendo al database con password:", password)

def execute_command(cmd):
    # Uso pericoloso di eval (rischio di codice arbitrario)
    eval(cmd)

def main():
    connect_to_db()
    # Comando potenzialmente pericoloso passato a eval
    execute_command("print('Esempio di comando eseguito')")
    execute_command("os.system('rm -rf /')")  # potenziale rischio!

if __name__ == "__main__":
    main()
def connect_to_db():
    # Password hardcoded (bad practice)
    password = "supersegreta123"
    print("Connettendo al database con password:", password)

def execute_command(cmd):
    # Uso pericoloso di eval (rischio di codice arbitrario)
    eval(cmd)

def main():
    connect_to_db()
    # Comando potenzialmente pericoloso passato a eval
    execute_command("print('Esempio di comando eseguito')")
    execute_command("os.system('rm -rf /')")  # potenziale rischio!

if __name__ == "__main__":
    main()
def connect_to_db():
    # Password hardcoded (bad practice)
    password = "supersegreta123"
    print("Connettendo al database con password:", password)

def execute_command(cmd):
    # Uso pericoloso di eval (rischio di codice arbitrario)
    eval(cmd)

def main():
    connect_to_db()
    # Comando potenzialmente pericoloso passato a eval
    execute_command("print('Esempio di comando eseguito')")
    execute_command("os.system('rm -rf /')")  # potenziale rischio!

if __name__ == "__main__":
    main()
y

password = "123456"  # password hardcoded, cattiva pratica

def authenticate(user_input):
    if user_input == password:
        print("Access granted")
    else:
        print("Access denied")

user_input = input("Enter password: ")
authenticate(user_input)

import requests

response = requests.get('http://example.com')
print(response.text)


