class Envio:
    #Definimos con su metodo constructor la clase envio y sus atributos
    def __init__(self, cp, direccion, tipo, pago):
        self.cp = cp
        self.direccion = direccion
        self.tipo = tipo
        self.pago = pago

    #Definimos str para retornar una cadena en el caso que se quiera ver el objeto generado
    def __str__(self):
        cad = " Codigo postal: " + str(self.cp)
        cad += " Direccion: " + str(self.direccion)
        cad += " Tipo de envio: " + str(self.tipo)
        cad += " Tipo de pago: " + str(self.pago)
        return cad

def menu():
    #Menu de opciones
    print("\nMenu de opciones")
    print("1_Crear el arreglo de registros/objetos de forma que contenga todos los datos de todos los envíos guardados en el archivo de texto")
    print("2_Cargar los datos del envio manualmente")
    print("3_Mostrar el arreglo de los envios")
    print("4_Busqueda por direccion y tipo de envio")
    print("5_Cambiar tipo de pago por busqueda de cp")
    print("6_Mostrar cantidad de tipos de envios")
    print("7_Mostrar importe total por tipo de envio")
    print("8_Tipo de envio con mayor importe final acumulado")
    print("9_Mostrar el importe final promedio entre todos los envíos del arreglo")
    print("0_Salir del programa")
    opc = int(input("Ingrese una opcion: "))
    return opc

def country(cp):
    n = len(cp)
    if n < 4 or n > 9:
        return 'Otro'

    # ¿es Argentina?
    if n == 8:
        if cp[0].isalpha() and cp[0] not in 'IO' and cp[1:5].isdigit() and cp[5:8].isalpha():
            return 'Argentina'
        else:
            return 'Otro'

    # ¿es Brasil?
    if n == 9:
        if cp[0:5].isdigit() and cp[5] == '-' and cp[6:9].isdigit():
            return 'Brasil'
        else:
            return 'Otro'

    if cp.isdigit():
        # ¿es Bolivia?
        if n == 4:
            return 'Bolivia'

        # ¿es Chile?
        if n == 7:
            return 'Chile'

        # ¿es Paraguay?
        if n == 6:
            return 'Paraguay'
        # ¿es Uruguay?
        if n == 5:
            return 'Uruguay'

    # ...si nada fue cierto, entonces sea lo que sea, es otro...
    return 'Otro'

def check_dir(direccion):
    cl = cd = 0
    td = False
    ant = " "
    for car in direccion:
        if car in " .":
            # fin de palabra...
            # un flag si la palabra tenia todos sus caracteres digitos...
            if cl == cd:
                td = True

            # resetear variables de uso parcial...
            cl = cd = 0
            ant = " "

        else:
            # en la panza de la palabra...
            # contar la cantidad de caracteres de la palabra actual...
            cl += 1

            # si el caracter no es digito ni letra, la direccion no es valida... salir con False...
            if not car.isdigit() and not car.isalpha():
                return False

            # si hay dos mayusculas seguidas, la direccion no es valida... salir con False...
            if ant.isupper() and car.isupper():
                return False

            # contar digitos para saber si hay alguna palabra compuesta solo por digitos...
            if car.isdigit():
                cd += 1

            ant = car

    # si llegamos acá, es porque no había dos mayusculas seguidas y no habia caracteres raros...
    # ... por lo tanto, habria que salir con True a menos que no hubiese una palabra con todos digitos...
    return td

def cargar_registros(v,cp,direccion,tipo,pago):
    for i in range(1):
        envio = Envio(cp,direccion,tipo,pago)
        v.append(envio)

def ordenamiento(v):
    #Ordenamiento secuencial, va intercambiando el anterior con el siguiente si son 
    m = len(v)

    for i in range(m-1):
        for j in range(i+1,m):
            cp1 = v[j].cp
            cp = v[i].cp
            if cp > cp1:
                v[i], v[j] = v[j], v[i]
    return v

def mostrar_registros(v):

    for envio in v:
        pais = country(envio.cp)
        print(f"{envio} pais {pais}")

def mostrar_primeros(v,m):
    c = 0
    for envio in v:
        pais = country(envio.cp)
        print(f"{envio} pais {pais}")
        c += 1
        if c == m:
            break

def busqueda_4(v,d,e):
    flag = False
    for envio in v:
        if envio.direccion == d and envio.tipo == e:
            print("Se encontro su busqueda\nEste es el envio: ",envio)
            flag = True
            break
    if not flag:
        print("No existe un envio con dichos datos")

def busqueda_5(v,cp1):
    flag = False
    for envio in v:
        if envio.cp == cp1:
            if envio.pago == 1:
                envio.pago = 2
                print("Se encontro un envio con el mismos cp\nEnvio modificado :",envio)
                flag = True
                break
            else:
                envio.pago = 1
                print("Se encontro un envio con el mismos cp\nEnvio modificado :",envio)
                flag = True
                break
    if not flag:
        print("No existe un envio con ese codigo postal")

def vector_contador_tipo(v):
    tipos_de_envios= [0] * 7
    for envios in v:
        tipo = envios.tipo
        tipos_de_envios[tipo] += 1
    print("Listado de la cantidad de tipos de envio")
    for i in range(len(tipos_de_envios)):
        print(f"El tipo de envio {i} tiene {tipos_de_envios[i]}")

def vector_contador_importe_x_tipo(v):
    #Vector
    tipos_de_envios = [0] * 7
    for envios in v:
        tipo = envios.tipo
        tipos_de_envios[tipo] += final_amount(envios.cp, country(envios.cp), envios.tipo, envios.pago)

    return tipos_de_envios

def final_amount(cp, destino, tipo, pago):
    # determinación del importe inicial a pagar.
    importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    monto = importes[tipo]

    if destino == 'Argentina':
        inicial = monto
    else:
        if destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1'):
            inicial = int(monto * 1.20)
        elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1'):
            inicial = int(monto * 1.25)
        elif destino == 'Brasil':
            if cp[0] == '8' or cp[0] == '9':
                inicial = int(monto * 1.20)
            else:
                if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                    inicial = int(monto * 1.25)
                else:
                    inicial = int(monto * 1.30)
        else:
            inicial = int(monto * 1.50)

    # determinación del valor final del ticket a pagar.
    # asumimos que es pago en tarjeta...
    final = inicial

    # ... y si no lo fuese, la siguiente será cierta y cambiará el valor...
    if pago == 1:
        final = int(0.9 * inicial)

    return final