import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Control de Notas")
    
        self.alumnos = []
        self.crear_pestaña_alta()
        self.crear_pestaña_consultas()
        self.crear_menu()

        self.ventana1.mainloop()

    def crear_pestaña_alta(self):
        pestaña_alta = ttk.Frame(self.ventana1)
        pestaña_alta.pack(fill="both", expand=1)

        ttk.Label(pestaña_alta, text="Código:").grid(row=0, column=0, padx=5, pady=5)
        self.codigo_var = tk.StringVar()
        ttk.Entry(pestaña_alta, textvariable=self.codigo_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(pestaña_alta, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
        self.nombre_var = tk.StringVar()
        ttk.Entry(pestaña_alta, textvariable=self.nombre_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(pestaña_alta, text="Apellidos:").grid(row=2, column=0, padx=5, pady=5)
        self.apellidos_var = tk.StringVar()
        ttk.Entry(pestaña_alta, textvariable=self.apellidos_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(pestaña_alta, text="Nota:").grid(row=3, column=0, padx=5, pady=5)
        self.nota_var = tk.StringVar()
        ttk.Entry(pestaña_alta, textvariable=self.nota_var).grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(pestaña_alta, text="Guardar", command=self.guardar_alumno).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def crear_pestaña_consultas(self):
        pestaña_consultas = ttk.Frame(self.ventana1)
        pestaña_consultas.pack(fill="both", expand=1)

        ttk.Button(pestaña_consultas, text="Consultar Aprobados", command=self.consultar_aprobados).pack(pady=5)
        ttk.Button(pestaña_consultas, text="Consultar Suspensos", command=self.consultar_suspendidos).pack(pady=5)

    def crear_menu(self):
        menubar = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar)

        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Guardar Informe de Aprobados", command=self.guardar_aprobados)
        archivo_menu.add_command(label="Guardar Informe de Suspensos", command=self.guardar_suspendidos)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.salir)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

    def guardar_alumno(self):
        codigo = self.codigo_var.get()
        nombre = self.nombre_var.get()
        apellidos = self.apellidos_var.get()
        nota = self.nota_var.get()

        if codigo and nombre and apellidos and nota:
            try:
                nota = float(nota)
                self.alumnos.append((codigo, nombre, apellidos, nota))
                mb.showinfo("Éxito", "Alumno registrado correctamente.")
                self.codigo_var.set("")
                self.nombre_var.set("")
                self.apellidos_var.set("")
                self.nota_var.set("")
            except ValueError:
                mb.showerror("Error", "La nota debe ser un número.")
        else:
            mb.showerror("Error", "Por favor, complete todos los campos.")

    def consultar_aprobados(self):
        aprobados = [alumno for alumno in self.alumnos if float(alumno[3]) >= 5.0]
        self.mostrar_resultados(aprobados, "Alumnos Aprobados")

    def consultar_suspendidos(self):
        suspendidos = [alumno for alumno in self.alumnos if float(alumno[3]) < 5.0]
        self.mostrar_resultados(suspendidos, "Alumnos Suspensos")

    def mostrar_resultados(self, alumnos, titulo):
        resultados_ventana = tk.Toplevel()
        resultados_ventana.title(titulo)

        if not alumnos:
            ttk.Label(resultados_ventana, text="No hay resultados.").pack()
        else:
            for alumno in alumnos:
                ttk.Label(resultados_ventana, text=f"Código: {alumno[0]}, Nombre: {alumno[1]}, Apellidos: {alumno[2]}, Nota: {alumno[3]}").pack()

    def guardar_aprobados(self):
        self.guardar_informe("aprobados.txt", [alumno for alumno in self.alumnos if float(alumno[3]) >= 5.0])

    def guardar_suspendidos(self):
        self.guardar_informe("suspendidos.txt", [alumno for alumno in self.alumnos if float(alumno[3]) < 5.0])

    def guardar_informe(self, archivo, alumnos):
        try:
            with open(archivo, "w") as f:
                for alumno in alumnos:
                    f.write(f"Código: {alumno[0]}, Nombre: {alumno[1]}, Apellidos: {alumno[2]}, Nota: {alumno[3]}\n")
            mb.showinfo("Éxito", f"Informe guardado como {archivo}")
        except Exception as e:
            mb.showerror("Error", f"No se pudo guardar el informe: {e}")

    def salir(self):
        self.ventana1.destroy()

aplicacion = Aplicacion()
