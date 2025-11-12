
USUARIO = "12345678"
PASSWORD = "password"
SALDO_INICIAL = 5000.0
PRESTAMO_1 = 100000
PRESTAMO_2 = 500000
PRESTAMO_3 = 1000000
SALDO_MINIMO_TRANSFERENCIA = 10000.0

class Banco:
    def __init__(self):
        self.saldo = SALDO_INICIAL
        self.intentos = 0
        self.bloqueado = False

    def validar_usuario(self, usuario, password):
        if usuario == USUARIO and password == PASSWORD:
            self.intentos = 0
            return True
        else:
            self.intentos += 1
            if self.intentos >= 5:
                self.bloqueado = True
            return False

    def retirar(self, monto):
        if monto <= 0:
            return "Ingrese un monto positivo"
        if self.saldo >= monto:
            self.saldo -= monto
            return f"Retiro exitoso. Saldo restante: ${self.saldo:.2f}"
        else:
            return "No posee saldo suficiente para retirar dicho monto"

    def depositar(self, monto):
        if monto <= 0:
            return "Ingrese un monto positivo"
        self.saldo += monto
        return f"Depósito exitoso. Saldo actual: ${self.saldo:.2f}"

    def consultar_saldo(self):
        return f"Su saldo actual es: ${self.saldo:.2f}"

    def pedir_prestamo(self, opcion):
        if self.saldo > 0:
            if opcion == 'A':
                return f"Préstamo aprobado: ${PRESTAMO_1}"
            elif opcion == 'B':
                return f"Préstamo aprobado: ${PRESTAMO_2}"
            elif opcion == 'C':
                return f"Préstamo aprobado: ${PRESTAMO_3}"
        return "No está habilitado a solicitar un préstamo"

    def transferir(self, alias, monto):
        if self.saldo < SALDO_MINIMO_TRANSFERENCIA:
            return "No dispone del saldo mínimo para transferir"
        if not alias:
            return "Alias no puede estar vacío"
        if monto <= 0:
            return "Ingrese un monto positivo"
        if self.saldo >= monto:
            self.saldo -= monto
            return f"Transferencia exitosa a {alias} por ${monto:.2f}"
        else:
            return "Usted no dispone de este monto para realizar la transferencia"