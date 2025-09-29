import tkinter as tk
from tkinter import messagebox, simpledialog

# =========================
# Clase principal (Modelo)
# =========================
class Registro:
    def __init__(self, codigo, nombre, descripcion):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - {self.descripcion}"


# =========================
# Clase de la aplicación (Vista + Controlador)
# =========================
class GestorRegistros:
    def __init__(self, root):
        self.root = root
        self.root.title("📋 Gestor de Registros")
        self.root.geometry("500x400")
        self.root.config(bg="#2C3E50")  # fondo oscuro elegante

        self.registros = []  # Lista para almacenar las instancias

        # ====== Título ======
        titulo = tk.Label(
            root,
            text="Gestor de Registros",
            font=("Arial Black", 16),
            fg="white",
            bg="#2C3E50"
        )
        titulo.grid(row=0, column=0, columnspan=3, pady=15)

        # ====== Etiquetas y campos ======
        lbl_codigo = tk.Label(root, text="Código:", fg="white", bg="#2C3E50", font=("Arial", 11))
        lbl_codigo.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_codigo = tk.Entry(root, font=("Arial", 11), width=25, bg="#ECF0F1")
        self.entry_codigo.grid(row=1, column=1, padx=5, pady=5)

        lbl_nombre = tk.Label(root, text="Nombre:", fg="white", bg="#2C3E50", font=("Arial", 11))
        lbl_nombre.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(root, font=("Arial", 11), width=25, bg="#ECF0F1")
        self.entry_nombre.grid(row=2, column=1, padx=5, pady=5)

        lbl_desc = tk.Label(root, text="Descripción:", fg="white", bg="#2C3E50", font=("Arial", 11))
        lbl_desc.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_desc = tk.Entry(root, font=("Arial", 11), width=25, bg="#ECF0F1")
        self.entry_desc.grid(row=3, column=1, padx=5, pady=5)

        # ====== Botones ======
        btn_style = {"font": ("Arial", 10, "bold"), "width": 10, "pady": 5}

        tk.Button(root, text="Agregar", command=self.agregar, bg="#27AE60", fg="white", **btn_style).grid(row=4, column=0, padx=5, pady=10)
        tk.Button(root, text="Modificar", command=self.modificar, bg="#2980B9", fg="white", **btn_style).grid(row=4, column=1, padx=5, pady=10)
        tk.Button(root, text="Eliminar", command=self.eliminar, bg="#C0392B", fg="white", **btn_style).grid(row=4, column=2, padx=5, pady=10)

        # ====== Listbox ======
        self.lista = tk.Listbox(root, width=65, height=10, bg="#34495E", fg="white", font=("Consolas", 10))
        self.lista.grid(row=5, column=0, columnspan=3, padx=10, pady=15)

    # =========================
    # Métodos del CRUD
    # =========================
    def agregar(self):
        codigo = self.entry_codigo.get().strip()
        nombre = self.entry_nombre.get().strip()
        descripcion = self.entry_desc.get().strip()

        if not codigo or not nombre or not descripcion:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        nuevo = Registro(codigo, nombre, descripcion)
        self.registros.append(nuevo)
        self.actualizar_lista()
        self.limpiar_campos()

    def modificar(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un registro para modificar")
            return

        index = seleccion[0]
        registro = self.registros[index]

        nuevo_codigo = simpledialog.askstring("Modificar", "Nuevo código:", initialvalue=registro.codigo)
        nuevo_nombre = simpledialog.askstring("Modificar", "Nuevo nombre:", initialvalue=registro.nombre)
        nueva_desc = simpledialog.askstring("Modificar", "Nueva descripción:", initialvalue=registro.descripcion)

        if nuevo_codigo and nuevo_nombre and nueva_desc:
            registro.codigo = nuevo_codigo
            registro.nombre = nuevo_nombre
            registro.descripcion = nueva_desc
            self.actualizar_lista()
        else:
            messagebox.showerror("Error", "Datos inválidos")

    def eliminar(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un registro para eliminar")
            return

        index = seleccion[0]
        self.registros.pop(index)
        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for r in self.registros:
            self.lista.insert(tk.END, str(r))

    def limpiar_campos(self):
        self.entry_codigo.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)


# =========================
# Programa principal
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorRegistros(root)
    root.mainloop()