import tkinter as tk
from datetime import datetime

class InterfazUsuario(tk.Tk):
    def __init__(self):
        super().__init__()

        # Sección 1: Recuadro de datos de entrada de usuario
        self.frame_datos_usuario = tk.Frame(self)
        self.frame_datos_usuario.pack(padx=10, pady=10)

        tk.Label(self.frame_datos_usuario, text="Nombre:").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(self.frame_datos_usuario)
        self.entry_nombre.grid(row=0, column=1)

        # Repite el proceso para los demás campos (apellidos, fecha de nacimiento, etc.)

        self.frame_botones = tk.Frame(self)
        self.frame_botones.pack(pady=10)

        # Botones para editar, guardar y limpiar datos
        tk.Button(self.frame_botones, text="Editar", command=self.editar_datos).pack(side=tk.LEFT)
        tk.Button(self.frame_botones, text="Guardar", command=self.guardar_datos).pack(side=tk.LEFT)
        tk.Button(self.frame_botones, text="Limpiar", command=self.limpiar_datos).pack(side=tk.LEFT)

        # Sección 2: Recuadro de bloqueo
        self.frame_bloqueo = tk.Frame(self)
        self.frame_bloqueo.pack(padx=10, pady=10)

        tk.Button(self.frame_bloqueo, text="Bloquear", command=self.bloquear).pack()

    def editar_datos(self):
        # Lógica para editar datos
        pass

    def guardar_datos(self):
        # Lógica para guardar datos
        pass

    def limpiar_datos(self):
        # Lógica para limpiar datos
        pass

    def bloquear(self):
        # Lógica para bloquear
        # Aquí puedes automatizar la entrada de datos según tus necesidades
        numero_tarjeta = obtener_numero_tarjeta_desde_pagina_web()  # Debes implementar esta función
        motivo_bloqueo = "Perdida/Extravío o Robo"
        fecha_bloqueo = datetime.now().strftime("%Y-%m-%d")
        hora_bloqueo = obtener_hora_actual()  # Debes implementar esta función
        correo_electronico = self.entry_correo.get()

        # Puedes utilizar estos datos como desees (mostrarlos, enviarlos a una base de datos, etc.)
        print(f"Número de tarjeta: {numero_tarjeta}")
        print(f"Motivo de bloqueo: {motivo_bloqueo}")
        print(f"Fecha de bloqueo: {fecha_bloqueo}")
        print(f"Hora de bloqueo: {hora_bloqueo}")
        print(f"Correo electrónico: {correo_electronico}")

def obtener_numero_tarjeta_desde_pagina_web():
    # Simula obtener el número de tarjeta desde una página web
    return "1234-5678-9012-3456"

def obtener_hora_actual():
    # Simula obtener la hora actual
    return datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    app = InterfazUsuario()
    app.title("Menú de Interacción")
    app.geometry("400x300")
    app.mainloop()
