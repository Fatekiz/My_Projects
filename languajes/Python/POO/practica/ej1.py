# Crea un sistema mediante clases para el funcionamiento de tarjetas, desde la creacion de la tarjeta y sus funciones:
# Mostrar datos, depositar, transferir, girar etc.
# Just enjoy it, good luck...

class Usuario():
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        
class Tarjeta():
    def __init__(self, banco, tipo, n_tarjeta, c_seguridad, dinero, nombres, fecha_nacimiento, usuario, contraseña):
        self.banco = banco
        self.tipo = tipo
        self.n_tarjeta = n_tarjeta
        self.c_seguridad = c_seguridad
        self.nombres = nombres
        self.fecha_nacimiento = fecha_nacimiento
        self.usuario = usuario
        self.contraseña = contraseña
        self.dinero = dinero
        assert dinero >= 0, "Error: no puede iniciar su cuenta con dinero en 'negativo'." # Aqui estoy condicionando con un assert el atributo 'dinero'

    def __str__ (self):
        return f"\n Nombres: {self.nombres} | Fecha de nacimiento: {self.fecha_nacimiento} \n Nombre del banco: {self.banco} | N° de Cuenta: {self.n_tarjeta} \n Codigo de seguridad: {self.c_seguridad} \n --------------------------------------------------------"

    def interactuar(self):
        # Bienvenida y verificación de usuario
        usuario = input(f"\n Bienvenido a {self.banco}, introduzca su usuario: ")
        while usuario != self.usuario:
            usuario = input(f"\n ERROR!: USUARIO INCORRECTO, introduzca nuevamente su usuario: ")
        # Contrasña
        if usuario == self.usuario:
            contraseña = input(f"\n Introduce tu contraseña para acceder a tu cuenta: ")
            while contraseña != self.contraseña:
                contraseña = input(f"\n ERROR!: Contraseña incorrecta, introduzca nuevamente su contraseña: ")
            if contraseña == self.contraseña:

                # interaccion principal de banco.
                opcion1 = input(f"\n Bienvenid@ {self.usuario}! ¿Que deseas hacer? \n \n Opciones: \n 1: Depositarse \n 2: Girar \n 3: Transferir \n \n Ingresa la opción correspondiente: ")

                # Menú e interacción para depositar.
                if opcion1 == "1":
                    print(f"\n ---- Menu de Depositos ----")
                    dinero = int(input(f" \n Ingrese la cantidad que desea depositar a su cuenta (CLP) (posteriormente ingreselo por la 'entrada de billetes'): $ "))
                    self.dinero += dinero
                    opcion2 = input("\n Deposito realizado. ¿Desea generar su comprobante? (De esta manera usted podrá ver el estado de su cuenta.) \n 1) Si. Generar comprobante\n 2) No. \n \n ")
                    if opcion2 == "1":
                        print(f"\n ---- COMPROBANTE DE AUTO-DEPOSITO ---- \n \n En este momento usted se ha depositado: -- ${dinero} CLP -- a su cuenta: '{self.tipo}' de numero: {self.n_tarjeta}. \n Estado actual de la cuenta: \n \n Monto: ${self.dinero} CLP \n")
                
                #
                elif opcion1 == 2:
                    pass

                elif opcion1 == 3:
                    pass

                else:
                    print(f"\n ERROR:  Opción ingresada inválida, Las opciones válidas son:  '1' , '2' y '3'. Ingrese nuevamente su opción: ")

        


    
    





#Creacion de tarjetas

Tarjeta1 = Tarjeta("Banco Estado", "De Crédito", 123456789, 737, 1000000, "Rocio Cárdenas Nancuante Belén", "12/11/1997", "Rocy_Wildcat97", "Rocy1997")

Tarjeta2 = Tarjeta("Banco Falabella", "Vista", 123456789, 737, 0, "Benjamin Concha Monsalves Orlando", "03/10/2005", "Fatekiz", "Fatekiz1203.,")
#mostrando datos con método magico
print(Tarjeta1)

# interacción con el banco
Tarjeta1.interactuar()

# --------------------------------- TERMINO DEL CÓDIGO -------------------------------------------------------- 

"""
Area de trabajo para hacer anotaciones:

-Usuarios con contraseña (all in 'default'). <-- todavia no se como implementarlo de manera que sea como un cajero publico y no una app privada.

-tener un banco. <-- LISTO

-funciones de cada tarjeta: tranferir, girar, depositar, mostrar datos. 
validaciones: debe tener validaciones como las de sus numeros al momento de la inscripción etc...     <--- EN PROCESO 23-02-2025

- 23-02-2025 : Quiero agregar una libreria que me permita imprimir el 'tiempo real del momento' , esto para los comprobantes.    <--- Aún no iniciado.

"""