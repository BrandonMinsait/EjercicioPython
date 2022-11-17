from datetime import datetime

class Nip:
    _nip = 0

    def __init__(self):
        self._nip = 1234

    def verificarNIP(self, passw):
        if str(passw) == str(self._nip):
            return True
        else:
            return False

class Consulta:
    _saldo = 1000

    def consultaSaldo(self):
        return self._saldo

class Movimientos:
    _movimientos = [[]]

    def imprimirMovimientos(self):
        print("\t\t\t***********************************")
        print("\t\t\t*            *          *         *")
        print("\t\t\t*    Fecha   *   Hora   *  Monto  *")
        print("\t\t\t*            *          *         *")
        print("\t\t\t***********************************")
        print("\t\t\t*            *          *         *")
        for mov in self._movimientos:
            movimiento = ""
            for datos in mov:
                movimiento = movimiento + "* " + datos + " "
            if str(len(movimiento)) != "0":
                movimiento = movimiento + "*"
                print("\t\t\t" + movimiento)
        print("\t\t\t*            *          *         *")
        print("\t\t\t***********************************")

    def agregar(self, lista):
        self._movimientos.append(lista)

class Retiro:
    movimientos = Movimientos()
    date = datetime.now()

    def retirarDinero(self, retiro=[]):
        saldoFin = Consulta._saldo - int(retiro)
        if saldoFin<0:
            print("\n\tSaldo insuficiente para realizar la operacion (Saldo actual: $" + str(Consulta._saldo) + ").")
        else:
            self.date = datetime.now()
            Consulta._saldo = saldoFin
            fecha = str(self.date.day) + "/" + str(self.date.month) + "/" + str(self.date.year)
            hora = str(self.date.hour) + ":" + str(self.date.minute) + ":" + str(self.date.second)
            lista = []
            lista.append(fecha)
            lista.append(hora)
            print(str(retiro))
            print(len(str(retiro)))
            if str(len(str(retiro)))=="1":
                lista.append("$     "+retiro)
            elif str(len(str(retiro)))=="2":
                lista.append("$    " + retiro)
            elif str(len(str(retiro)))=="3":
                lista.append("$   " + retiro)
            elif str(len(str(retiro)))=="4":
                lista.append("$  " + retiro)
            self.movimientos.agregar(lista)
            print("\n\tSaldo actual: $" + str(Consulta._saldo) + ".")

class Mensajes:
    banco = []
    menu = []

    def __init__(self):
        if len(self.banco)==0:
            self.banco.append("xxxxxxxxxxxxxxxxxxxxxxxxx")
            self.banco.append("x                       x")
            self.banco.append("x                   x   x")
            self.banco.append("x xxx  xxx  x   x   x   x")
            self.banco.append("x x  x x  x x   x   x   x")
            self.banco.append("x x  x x  x x   x  x x  x")
            self.banco.append("x x  x x  x  x x   x x  x")
            self.banco.append("x xxx  xxx   x x   x x  x")
            self.banco.append("x x  x x  x  x x  x   x x")
            self.banco.append("x x  x x  x   x   x   x x")
            self.banco.append("x x  x x  x   x   x   x x")
            self.banco.append("x xxx  xxx    x         x")
            self.banco.append("x                       x")
            self.banco.append("xxxxxxxxxxxxxxxxxxxxxxxxx")

            self.menu.append("xxxxxxxxxxxxxxxxxxxxxxxxx")
            self.menu.append("x                       x")
            self.menu.append("x       Bienvenido      x")
            self.menu.append("x                       x")
            self.menu.append("x  1.- Consultar saldo  x")
            self.menu.append("x  2.- Restirar dinero  x")
            self.menu.append("x 3.- Cons. movimientos x")
            self.menu.append("x                       x")
            self.menu.append("x       4.- Salir       x")
            self.menu.append("x                       x")
            self.menu.append("xxxxxxxxxxxxxxxxxxxxxxxxx")

class Menu:
    mensajes = Mensajes()
    consulta = Consulta()
    retiro = Retiro()
    movimientos = Movimientos()

    def menuPrincipal(self):
        opc = 0
        opc2 = True
        while str(opc)!="4" and opc2:
            for menuImp in self.mensajes.menu:
                print("\t\t\t\t" + menuImp)
            opc = input("\n\t\t\t\tEscoge una opcion para continuar: \n")
            if opc.isnumeric():
                if str(opc)=="1":
                    print("\n\t\t\t\tSu saldo actual es de: $" + str(self.consulta.consultaSaldo()))
                elif str(opc)=="2":
                    retirar = input("\n\t\t\t\t¿Cuanto dinero quieres retirar?\n")
                    self.retiro.retirarDinero(retirar)
                elif str(opc)=="3":
                    self.movimientos.imprimirMovimientos()
                opc2 = input("\n\n\t\t\t¿Desea volver al menu principal [1.- Si / 2.- No]\n")
                if opc2.isnumeric():
                    if str(opc2) == "1":
                        opc2 = True
                    elif str(opc2) == "2":
                        opc2 = False
                    else:
                        print("\n\t\t\t\tNo se ha escogido una opcion valida.")
                        opc2 = False
                else:
                    opc=4
            else:
                print("\n\t\t\tNo se ha escogido una opcion valida. Volviendo al menu...")
        print("\n\n\t\t\t\tHasta pronto.\n")

mensajes = Mensajes()
passw = Nip()
menu = Menu()
intentos = 1
flag = 0
for bancoImp in mensajes.banco:
    print("\t\t\t\t" + bancoImp)
print("\n\t\t\t\t\tBienvenido")
while intentos<4:
    nip = input("\n\t\t\t\tIntroduce tu NIP para continuar: ")
    if nip.isnumeric():
        if passw.verificarNIP(nip):
            menu.menuPrincipal()
            intentos = 4
            flag = 1
        else:
            print("\n\t\t\t\tNIP incorrecto")
            turno = 3 - intentos
            print("\n\t\t\t\tIntentos restantes: " + str(turno))
            intentos = intentos + 1
    else:
        print("\n\t\t\t\tNo se ha introducido un numero")
        turno = 3 - intentos
        print("\n\t\t\t\tIntentos restantes: " + str(turno))
        intentos = intentos + 1
if str(intentos)=="4":
    if str(flag)=="0":
        print("\n\t\t\t\tNumero de intentos excedido")