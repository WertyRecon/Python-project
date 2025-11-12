import tkinter as tk

alumnos = {}

def verificar(dato):
    if dato == "":
        dato == "error"
    return dato

def convertir(valor):
    if valor.isdecimal():
        valor = int(valor)
    else:
        valor = "error"
    return valor

def ver():
    datos = []

    for i in alumnos:
        curso = alumnos[i]
        datos.append(f"{i.capitalize()} - {curso} cursos")
    mensaje.config(text = "\n".join(datos))


def agregar():
    nombre = caja_nombre.get().strip().lower()
    cursos = caja_cursos.get().strip()
    
    nombre = verificar(nombre)
    cursos = convertir(cursos)

    if nombre == "error" or cursos == "error":
        mensaje.config(text="Error en los datos ingresados")
    else:
            alumnos[nombre] = cursos
            mensaje.config(text=f"Alumno {nombre} se agrego bien a la lista")

def ver_alumno():
    nombre = caja_nombre.get().strip().lower()
    nombre = verificar(nombre)
    
    if nombre in alumnos:
       mensaje.config(text=f"el alumno {nombre} tiene {alumnos[nombre]} cursos")
    else:
     mensaje.config(text=f"El alumno {nombre} no tiene  cursos")




ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title("registro de alumnos")

boton_lista = tk.Button(text="Ver lista de alumnos", command=ver)
boton_lista.place(x=10, y=10, width=120, height=30)   

etiqueta_nombre = tk.Label(ventana, text="Nombre del alumno:")
etiqueta_nombre.place(x=10, y=60)

caja_nombre = tk.Entry()
caja_nombre.place(x=150, y=60, width=200, height=20)

etiqueta_cursos = tk.Label(ventana, text="Cantidad de cursos:")
etiqueta_cursos.place(x=10, y=100)

caja_cursos = tk.Entry()
caja_cursos.place(x=150, y=100, width=100, height=20)

boton_agregar = tk.Button(text="Agregar a la lista", command=agregar)
boton_agregar.place(x=10, y=140, width=120, height=30)

boton_cursos = tk.Button(text="Ver cantidad de cursos : ", command=ver_alumno)
boton_cursos.place(x=150, y=140, width=180, height=30)

mensaje = tk.Label(text="")
mensaje.place(x=10, y=200)

ventana.mainloop()
