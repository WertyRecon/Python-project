import tkinter as tk
from tkinter import messagebox, simpledialog

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

class App:
    def __init__(self, root):
        self.root = root
        self.banco = Banco()
        self.root.title("ORT Banking")
        self.login_window()

    def login_window(self):
        self.clear()
        tk.Label(self.root, text="Usuario (DNI):").pack()
        self.usuario_entry = tk.Entry(self.root)
        self.usuario_entry.pack()
        tk.Label(self.root, text="Contraseña:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        tk.Button(self.root, text="Ingresar", command=self.check_login).pack()

    def check_login(self):
        usuario = self.usuario_entry.get()
        password = self.password_entry.get()
        if self.banco.bloqueado:
            messagebox.showerror("Bloqueado", "Se le ha bloqueado el ingreso al cajero. Contacte a un asesor en línea")
            self.root.quit()
        elif self.banco.validar_usuario(usuario, password):
            self.menu_window()
        else:
            if self.banco.intentos >= 5:
                messagebox.showerror("Bloqueado", "Se le ha bloqueado el ingreso al cajero. Contacte a un asesor en línea")
                self.root.quit()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def menu_window(self):
        self.clear()
        tk.Label(self.root, text="Seleccione una opción:").pack()
        tk.Button(self.root, text="Retirar dinero", command=self.retirar_window).pack(fill='x')
        tk.Button(self.root, text="Depositar dinero", command=self.depositar_window).pack(fill='x')
        tk.Button(self.root, text="Consultar saldo", command=self.consultar_saldo).pack(fill='x')
        tk.Button(self.root, text="Pedir préstamo", command=self.prestamo_window).pack(fill='x')
        tk.Button(self.root, text="Transferencia de dinero", command=self.transferir_window).pack(fill='x')
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(fill='x')

    def retirar_window(self):
        monto = simpledialog.askfloat("Retirar dinero", "Ingrese el monto a retirar:")
        if monto is not None:
            resultado = self.banco.retirar(monto)
            messagebox.showinfo("Resultado", resultado)

    def depositar_window(self):
        monto = simpledialog.askfloat("Depositar dinero", "Ingrese el monto a depositar:")
        if monto is not None:
            resultado = self.banco.depositar(monto)
            messagebox.showinfo("Resultado", resultado)

    def consultar_saldo(self):
        resultado = self.banco.consultar_saldo()
        messagebox.showinfo("Saldo", resultado)

    def prestamo_window(self):
        opciones = {"A": PRESTAMO_1, "B": PRESTAMO_2, "C": PRESTAMO_3}
        opcion = simpledialog.askstring("Préstamo", "Seleccione opción:\nA) $100.000\nB) $500.000\nC) $1.000.000")
        if opcion:
            resultado = self.banco.pedir_prestamo(opcion.upper())
            messagebox.showinfo("Préstamo", resultado)

    def transferir_window(self):
        if self.banco.saldo < SALDO_MINIMO_TRANSFERENCIA:
            messagebox.showerror("Error", "No dispone del saldo mínimo para transferir")
            return
        alias = simpledialog.askstring("Transferencia", "Ingrese el alias de la cuenta:")
        monto = simpledialog.askfloat("Transferencia", "Ingrese el monto a transferir:")
        if alias and monto is not None:
            resultado = self.banco.transferir(alias, monto)
            messagebox.showinfo("Transferencia", resultado)

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    app = App(root)
    root.mainloop()