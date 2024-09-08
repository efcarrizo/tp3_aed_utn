import os.path
from support import *

def main():
    v = []
    vec = []
    opc = -1
    while opc !=0:
        opc = menu()
        if opc == 1:
            if len(v) != 0:
                opc = int(input("Advertencia el arreglo anterior se eliminara. Si desea continaur coloque 1, sino el numero 2: "))

                if opc == 1:
                    v = []
                    vec = []
                    # nombre del archivo de texto de entrada...
                    # ... se asume que está en la misma carpeta del proyecto...
                    fd = 'envios-tp3.txt'

                    # control de existencia...
                    if not os.path.exists(fd):
                        print('El archivo', fd, 'no existe...')
                        print('Revise, y reinicie el programa...')
                        exit(1)

                    # procesamiento del archivo de entrada...
                    # apertura del archivo...
                    m = open(fd, 'rt')

                    # procesamento de la línea de timestamp...
                    # Resultado 1...
                    line = m.readline()
                    control = 'Soft Control'
                    if 'HC' in line:
                        control = 'Hard Control'
                    while True:
                        # ...intentar leer la linea que sigue...
                        line = m.readline()

                        # ...si se obtuvo una cadena vacia, cortar el ciclo y terminar...
                        if line == '':
                            break

                        if line[-1] == "\n":
                            line = line[0:-1]

                        # ...procesar la línea leída si el ciclo no cortó...
                        # ... obtener cada dato por separado, y en el tipo correcto...
                        # ... no es necesario en este caso eliminar el "\n" del final,
                        # porque la linea no se va a mostrar en pantalla, y porque las
                        # instrucciones que siguen toman cada dato en forma directa,
                        # prescindiendo del "\n"...
                        cp = line[0:9].strip().upper()
                        direccion = line[9:29].strip()
                        tipo = int(line[29])
                        pago = int(line[30])
                        pais = country(cp)
                        if control == "Hard Control":
                            if check_dir(direccion):
                                cargar_registros(v,cp,direccion, tipo, pago)
                        else:
                            cargar_registros(v, cp, direccion, tipo, pago)
            else:
                # nombre del archivo de texto de entrada...
                # ... se asume que está en la misma carpeta del proyecto...
                fd = 'envios-tp3.txt'

                # control de existencia...
                if not os.path.exists(fd):
                    print('El archivo', fd, 'no existe...')
                    print('Revise, y reinicie el programa...')
                    exit(1)

                # procesamiento del archivo de entrada...
                # apertura del archivo...
                m = open(fd, 'rt')

                # procesamento de la línea de timestamp...
                # Resultado 1...
                line = m.readline()
                control = 'Soft Control'
                if 'HC' in line:
                    control = 'Hard Control'
                while True:
                    # ...intentar leer la linea que sigue...
                    line = m.readline()

                    # ...si se obtuvo una cadena vacia, cortar el ciclo y terminar...
                    if line == '':
                        break

                    if line[-1] == "\n":
                        line = line[0:-1]

                    # ...procesar la línea leída si el ciclo no cortó...
                    # ... obtener cada dato por separado, y en el tipo correcto...
                    # ... no es necesario en este caso eliminar el "\n" del final,
                    # porque la linea no se va a mostrar en pantalla, y porque las
                    # instrucciones que siguen toman cada dato en forma directa,
                    # prescindiendo del "\n"...
                    cp = line[0:9].strip().upper()
                    direccion = line[9:29].strip()
                    tipo = int(line[29])
                    pago = int(line[30])
                    pais = country(cp)
                    if control == "Hard Control":
                        if check_dir(direccion):
                            cargar_registros(v, cp, direccion, tipo, pago)

                    else:
                        cargar_registros(v, cp, direccion, tipo, pago)

        elif opc == 2:
            print("Usted eligio la opcion de cargar envio manual: ")
            salir = 1
            while salir == 1:
                cp = input("Ingrese el cp: ")
                direccion = input("Ingrese la direccion (Deje espacio para los numero y termine con ´.´): ")
                tipo = int(input("Ingrese el tipo de envio: "))
                while (tipo <0 or tipo > 6):
                    print("Ingreso un tipo de envio incorrecto. Vuelva a intentarlo")
                    tipo = int(input("Ingrese el tipo de envio: "))
                pago = int(input("Ingrese el tipo de pago: "))
                while (pago != 1 and pago != 2):
                    print("Ingreso un tipo de pago incorrecto. Vuelva a intentarlo")
                    pago = int(input("Ingrese el tipo de pago: "))




                pais = country(cp)
                cargar_registros(v, cp, direccion, tipo, pago)

                salir = int(input("Si desea cargar otro envio coloque 1, Si desea continuar 2: "))

        elif opc == 3:
            if len(v) == 0:
                print("No cargo ningun envio, primero deber cargar al menos 1 envio")

            else:
                opc3 =int(input("Si desea mostrar todo los registros coloque 1, Si desea mostrar un cantidad detrminada de los primeros 2: "))
                ordenamiento(v)
                if opc3 == 1:
                    mostrar_registros(v)
                else:
                    m = int(input("Ingrese la cantidad a mostrar: "))
                    mostrar_primeros(v, m)

        elif opc == 4:
            #Busqueda de envio
            if len(v) == 0:
                print("No hay ningun envio")
            else:
                d = input("Ingrese la direccion a buscar (Dejar espacio para los numero y debe terminar con ´.´): ")
                e = input("Ingrese el tipo de envio a buscar: ")
                if e in "0123456789":
                    e = int(e)
                    busqueda_4(v,d,e)
                else:
                    print("Debe ingresar un tipo de envio valido")
                
                

        elif opc == 5:
            if len(v) == 0:
                print("No hay ningun envio")
            else:
                cp1 = input("Ingrese el cp a buscar: ")
                busqueda_5(v,cp1)

        elif opc == 6:
            if len(v) == 0:
                print("No hay ningun envio")
            else:
                vector_contador_tipo(v)

        elif opc == 7:
            if len(v) == 0:
                print("No hay ningun envio")
            else:
                tipos_de_envios = vector_contador_importe_x_tipo(v)
                print("Listado de la cantidad de tipos de envio")
                for i in range(len(tipos_de_envios)):
                    print(f"Tipo de envio: {i} --- Precios total:   {tipos_de_envios[i]}")

        elif opc == 8:
            if len(tipos_de_envios) == 0:
                print('Primero debe usar la opcion 7')
            else:
                mayor = None
                indice = 0
                acumulador = 0
                for i in tipos_de_envios:
                    indice += 1
                    acumulador += i
                    if (mayor == None) or (mayor < i):
                        mayor = i
                        indice_mayor = indice



                porcetaje = round((mayor * 100) / acumulador, 2)
                print('El tipo de envio', indice_mayor,'tiene el monto mayor y es: $',mayor)
                print('El porcentaje del mayor sobre el total es de: %', porcetaje)

        elif opc == 9:
            if len(v) == 0:
                print("No hay ningun envio")

            else:
                importe_9 = 0
                cantidad_envios_9 = 0
                importe_final_9 = 0
                cont_9 = 0
                for envios in v:
                    importe_final_9 += final_amount(envios.cp, country(envios.cp), envios.tipo, envios.pago)
                    cantidad_envios_9 += 1

                promedio_9 = round(importe_final_9 / cantidad_envios_9,2)

                for envios in v:
                    importe_9 = final_amount(envios.cp, country(envios.cp), envios.tipo, envios.pago)
                    if importe_9 < promedio_9:
                        cont_9 += 1

                print(f"Importe total : {importe_final_9}, cantidad de envios: {cantidad_envios_9} final promedio: {promedio_9}")
                print(f"La cantidad de envios que tuvieron un importe menor al promedio: {cont_9}")


if __name__ == '__main__':
    main()