import json

def signUp():
    mail = input("Ingrese su email: ")
    if userCheck(mail):
        print("Usuario ya registrado, intente con un mail diferente")
        return
    contraseña = input("Ingrese su contraseña: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    dataUsuarios = {
        "mail": mail,
        "contraseña": contraseña,
        "nombre": nombre,
        "apellido": apellido
    }

    with open("usuariosPE.json", "a") as file:
        json.dump(dataUsuarios, file)
        file.write('\n')
        file.close()
    
    print("Usuario registrado con exito")

def userCheck(mail):
    with open("usuariosPE.json", "r") as file:
        for line in file:
            dataUsuarios = json.loads(line)
            if dataUsuarios["mail"] == mail:
                return True
            file.close()
    return False

def login():
    mail = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")
    
    with open("usuariosPE.json", "r") as file:
        for line in file:
            dataUsuarios = json.loads(line)
            if dataUsuarios["mail"] == mail and dataUsuarios["contraseña"] == contraseña:
                name = dataUsuarios["nombre"]
                print(f"Bienvenido {name}!!")
                file.close()
                return
            
    print("Usuario o contraseña invalido, intente nuevamente")

def dataCheck():
    with open("usuariosPE.json", "r") as file:
        for line in file:
            dataUsuarios = json.loads(line)
            print(" ")
            print("Email:", dataUsuarios["mail"])
            print("Nombre:", dataUsuarios["nombre"])
            print("Apellido:", dataUsuarios["apellido"])
            print(" ")


def main():
    print("1. Registrate")
    print("2. Iniciar sesion")
    print("3. Ver datos")
    eleccion = input("Seleccione una opcion: ")
    
    if eleccion == "1":
        signUp()
    elif eleccion == "2":
        login()
    elif eleccion == "3":
        dataCheck()
    else:
        print("Opcion incorrecta")

main()