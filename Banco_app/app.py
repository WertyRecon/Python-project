import sys
sys.path.append('../post_clases_python')
import tkinter as tk
from tkinter import messagebox, simpledialog

from ort_banco2 import PRESTAMO_1, PRESTAMO_2, PRESTAMO_3, SALDO_MINIMO_TRANSFERENCIA, Banco

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