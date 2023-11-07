import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
import mysql.connector
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os
from tkinter.simpledialog import askstring
import webbrowser

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="base_de_prueba"
    )



except Exception as e:
    messagebox.showerror("Error", f"Ocurrió un error al conectarse a la base de datos.")


def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")


def ventanaAcceso():
    def acceso():
        usuario = entry_user.get()
        contraseña = entry_pass.get()

        if usuario == "" or contraseña == "":
            messagebox.showerror("Error de acceso", "Uno o mas campos se encuentran vacios.")

        else:

            cursor = conexion.cursor()

            consulta = "SELECT nom_usuario, contraseña FROM usuarios WHERE nom_usuario = %s"
            
            cursor.execute(consulta, (usuario,))

            resultado = cursor.fetchone()

            cursor.nextset()
            cursor.close()

            if resultado is not None:

                usuario_db, contrasena_db = resultado

                if usuario_db == usuario and contrasena_db == contraseña:

                    messagebox.showinfo("Exito", "Inicio de sesión exitoso.")
                    root.withdraw()
                    ventanaInicio()

                else:
                    messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

            else:
                messagebox.showerror("Error", "Usuario no encontrado.")

    root = tk.Tk()
    root.title("Clinet")
    root.geometry("300x400")
    root.iconbitmap("resources/imagenn.ico")
    root.configure(bg="#bc6c25")
    root.resizable(False, False)

    centrar_ventana(root)

    image = os.path.abspath("resources/imagen1.png")

    clinetLogo = Image.open(image)

    nuevo_tamano = (120, 120)
    imagen_redimensionada = clinetLogo.resize(nuevo_tamano)

    imagen_gif = ImageTk.PhotoImage(imagen_redimensionada) 

    roboto = ("Roboto", 12, "bold")

    accessFrame = tk.Frame(root, background="#bc6c25")
    accessFrame.pack(pady=30)

    def saltoEntry(event, sigEntry):
        sigEntry.focus_set()
    
    def buscarr(event, funcion):
        funcion()


    userLabel = tk.Label(accessFrame, text="Usuario", font=roboto, background="#bc6c25", foreground="white")
    userLabel.pack(pady=10)
    entry_user = tk.Entry(accessFrame, width=30, font=roboto, bg="#fefefe")
    entry_user.pack()

    entry_user.focus_set()

    passLabel = tk.Label(accessFrame, text="Contraseña", font=roboto, background="#bc6c25", foreground="white")
    passLabel.pack(pady=10)
    entry_pass = tk.Entry(accessFrame, width=30, font=roboto, show="●", bg="#fefefe")
    entry_pass.pack()

    entry_user.bind('<Return>', lambda event, entry=entry_pass: saltoEntry(event, entry))
    entry_pass.bind('<Return>', lambda event, entry=acceso: buscarr(event, entry))


    formSub = tk.Button(accessFrame, text="Ingresar", width=27, height=1, command=acceso, background="#6c757d", foreground="#fefefe", font=roboto)
    formSub.pack(pady=20)

    imageLabel = tk.Label(accessFrame, image=imagen_gif, borderwidth=0)
    imageLabel.pack(pady=10)

    root.mainloop()


def ventanaInicio():
    global imagen_gif
    root = tk.Toplevel()
    root.title("Inicio")
    root.geometry("1108x500")
    root.iconbitmap("resources/imagenn.ico")
    root.configure(bg="#bc6c25")
    root.resizable(False, False)

    centrar_ventana(root)

    def abrirInicio():
        root.withdraw()
        ventanaInicio()

    def abrirPacientes():
        root.withdraw()
        ventanaPacientes()

    def abrirMedicos():
        root.withdraw()
        ventanaMedicos()

    def abrirHistoriasClinicas():
        root.withdraw()
        ventanaHistoriasClinicas()

    def abrirTurnos():
        root.withdraw()
        ventanaTurnos()

    def abrirAsignarT():
        root.withdraw()
        ventanaAsignarT()

    def abrirInternaciones():
        root.withdraw()
        ventanaInternaciones()

    def abrirAsignarI():
        root.withdraw()
        ventanaAsignarI()

    def abrirEspecialidades():
        root.withdraw()
        ventanaEspecialidades()

    def abrirPatologias():
        root.withdraw()
        ventanaPatologias()

    def abrirUsuarios():
        root.withdraw()
        ventanaUsuarios()

    navFrame = tk.Frame(root)
    navFrame.pack()

    variables = ["btnInicio", "btnPacientes", "btnMedicos", "btnHistoriasClinicas", "Asignar Turnos", "btnTurnos", "btnInternaciones", "Asignar Internacion", "btnEspecialidades", "btnPatologias", "btnUsuarios"]

    textos = ["Inicio", "Pacientes", "Medicos", "Historias Clinicas", "Turnos", "Asignar \n Turnos", "Internaciones", "Asignar \n Internacion", "Especialidades", "Patologias", "Usuarios"]

    comandos = [abrirInicio, abrirPacientes, abrirMedicos, abrirHistoriasClinicas, abrirTurnos, abrirAsignarT, abrirInternaciones, abrirAsignarI, abrirEspecialidades, abrirPatologias, abrirUsuarios]
    
    roboto = ("Roboto", 8, "bold")
    
    for i in range(len(variables)):
        button = variables[i]
        button = tk.Button(navFrame, text=f"{textos[i]}", width=13, height=2, command=comandos[i], background="#6c757d", foreground="#fefefe", font=roboto)
        button.pack(side="left")

    def abrirPdf():
        # URL del archivo PDF que deseas abrir en el navegador
        url_pdf = os.path.abspath("resources/manual.pdf")

        # Abrir la URL en el navegador predeterminado
        webbrowser.open_new(url_pdf)

    frameImage = tk.Frame(root, background="#bc6c25")
    frameImage.pack(pady=20)

    image_path = os.path.abspath("resources/imagen1.png")

    clinet = Image.open(image_path)

    imagen_gif = ImageTk.PhotoImage(clinet)

    imagen = tk.Label(frameImage, image=imagen_gif, borderwidth=0)
    imagen.pack()

    botonManual = tk.Button(frameImage, text="Abrir Manual", width=20, height=2, command=abrirPdf, background="#6c757d", foreground="#fefefe", font=roboto)
    botonManual.pack()

    root.mainloop()

def ventanaPacientes():

    root = tk.Tk()
    root.title("Pacientes")
    root.geometry("1108x500")
    root.iconbitmap("resources/imagenn.ico")
    root.configure(bg="#bc6c25")
    root.resizable(False, False)

    centrar_ventana(root)

    def abrirInicio():
        root.withdraw()
        ventanaInicio()

    def abrirPacientes():
        root.withdraw()
        ventanaPacientes()

    def abrirMedicos():
        root.withdraw()
        ventanaMedicos()

    def abrirHistoriasClinicas():
        root.withdraw()
        ventanaHistoriasClinicas()

    def abrirTurnos():
        root.withdraw()
        ventanaTurnos()

    def abrirAsignarT():
        root.withdraw()
        ventanaAsignarT()

    def abrirInternaciones():
        root.withdraw()
        ventanaInternaciones()

    def abrirAsignarI():
        root.withdraw()
        ventanaAsignarI()

    def abrirEspecialidades():
        root.withdraw()
        ventanaEspecialidades()

    def abrirPatologias():
        root.withdraw()
        ventanaPatologias()

    def abrirUsuarios():
        root.withdraw()
        ventanaUsuarios()

    navFrame = tk.Frame(root)
    navFrame.pack()

    variables = ["btnInicio", "btnPacientes", "btnMedicos", "btnHistoriasClinicas", "Asignar Turnos", "btnTurnos", "btnInternaciones", "Asignar Internacion", "btnEspecialidades", "btnPatologias", "btnUsuarios"]

    textos = ["Inicio", "Pacientes", "Medicos", "Historias Clinicas", "Turnos", "Asignar \n Turnos", "Internaciones", "Asignar \n Internacion", "Especialidades", "Patologias", "Usuarios"]

    comandos = [abrirInicio, abrirPacientes, abrirMedicos, abrirHistoriasClinicas, abrirTurnos, abrirAsignarT, abrirInternaciones, abrirAsignarI, abrirEspecialidades, abrirPatologias, abrirUsuarios]
    
    roboto = ("Roboto", 8, "bold")

    for i in range(len(variables)):
        button = variables[i]
        button = tk.Button(navFrame, text=f"{textos[i]}", width=13, height=2, command=comandos[i], background="#6c757d", foreground="#fefefe", font=roboto)
        button.pack(side="left")

    def actualizar_treeview():

        cursor = conexion.cursor()

        if tree.get_children():
            tree.delete(*tree.get_children())
        select_query = "SELECT * FROM pacientes" 
        cursor.execute(select_query)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)

        cursor.close()


    def modificarRegistro():
        codValue = codVar.get()
        nombreValue = nombreVar.get()
        papellidoValue = apellidoVar.get()
        fechaDeNacValue = fechaVar.get()
        dniValue = dniVar.get()
        direcValue = direcVar.get()
        telefonoValue = telefonoVar.get()       

        update_query = "UPDATE pacientes SET Nombre = %s, Papellido = %s, fecha_de_nac = %s, dni = %s, direc = %s, telefono = %s WHERE cod_paciente = %s "
        valores = (nombreValue, papellidoValue, fechaDeNacValue, dniValue, direcValue, telefonoValue, codValue)

        if codValue == "" or nombreValue == "" or papellidoValue == "" or fechaDeNacValue == "" or dniValue == "" or direcValue == "" or telefonoValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            cursor = conexion.cursor()
            valor = (codValue,)
            consulta2 = "SELECT * FROM pacientes WHERE cod_paciente = %s"
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchall()
            cursor.close()
            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea modificar el registro?")
                if confirmacion:
                    cursor = conexion.cursor()
                    cursor.execute(update_query, valores)
                    conexion.commit()
                    cursor.close()
                    messagebox.showinfo("Exito", "El registro ha sido modificado exitosamente.")
                    actualizar_treeview()

                    textos = [codVar, nombreVar, apellidoVar, fechaVar, dniVar, direcVar, telefonoVar]

                    for i in range(len(textos)):
                        nuevo_valor = "" 
                        textos[i].delete(0, tk.END)
                        textos[i].insert(0, nuevo_valor)
                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera modificado.")
            else:
                messagebox.showerror("Error", "El codigo de paciente ingresado no existe.")


    def cargarRegistro():
        nombreValue = str(nombreVar.get()).strip()
        papellidoValue = str(apellidoVar.get()).strip()
        fechaDeNacValue = str(fechaVar.get()).strip()
        dniValue = str(dniVar.get()).strip()
        direcValue = str(direcVar.get()).strip()
        telefonoValue = str(telefonoVar.get()).strip()
        
        valores = (nombreValue, papellidoValue, fechaDeNacValue, dniValue, direcValue, telefonoValue)

        insert_query = "INSERT INTO pacientes (Nombre, Papellido, fecha_de_nac, dni, direc, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
        
        if nombreValue == "" or papellidoValue == "" or fechaDeNacValue == "" or dniValue == "" or direcValue == "" or telefonoValue == "" :
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            cursor = conexion.cursor()
            cursor.execute(insert_query, valores)
            messagebox.showinfo("Éxito", "El registro ha sido cargado exitosamente.")
            conexion.commit()
            cursor.close()
            actualizar_treeview()

            textos = [codVar, nombreVar, apellidoVar, fechaVar, dniVar, direcVar, telefonoVar]

            for i in range(len(textos)):
                nuevo_valor = "" 
                textos[i].delete(0, tk.END)
                textos[i].insert(0, nuevo_valor)

    def eliminarRegistro():
        id_to_delete = codVar.get()

        if id_to_delete == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else: 
            cursor = conexion.cursor()
            valor = (id_to_delete,)
            consulta2 = "SELECT * FROM pacientes WHERE cod_paciente = %s"
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchall()
            cursor.close()
            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar el registro?")
                if confirmacion:
                        cursor = conexion.cursor()
                        valores = (id_to_delete,)
                        delete_query = "DELETE FROM pacientes WHERE cod_paciente = %s"
                        cursor.execute(delete_query, valores)
                        conexion.commit()
                        messagebox.showinfo("Exito", "El registro ha sido eliminado exitosamente.")
                        actualizar_treeview()
                        cursor.close()
                        textos = [codVar, nombreVar, apellidoVar, fechaVar, dniVar, direcVar, telefonoVar]

                        for i in range(len(textos)):
                            nuevo_valor = "" 
                            textos[i].delete(0, tk.END)
                            textos[i].insert(0, nuevo_valor)
                    
                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera eliminado.")
            else:
                messagebox.showerror("Error", "El codigo de paciente ingresado no existe.")


    def volcarTodo():
        cursor = conexion.cursor()
        consulta = "SELECT * FROM pacientes"
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()

        for a in tree.get_children():
            tree.delete(a)
            

        for registro in registros:
            tree.insert("", "end", values=registro)

    def on_tree_double_click(event):
        item = tree.selection()[0]
        values = tree.item(item, "values")

        textboxx = [codVar, nombreVar, apellidoVar, fechaVar, dniVar, direcVar, telefonoVar]

        for index, value in enumerate(values):
            textboxx[index].delete(0, tk.END)
            textboxx[index].insert(0, value)


    def columnSearch(event):
        comboValue = comboSearch.get()
        searchValue = search.get()

        consulta = None

        if comboValue == "":
            messagebox.showinfo("Campo Vacio", "El selector se encuentra vacio.")
        elif comboValue == "Nombre":
            consulta = "SELECT * FROM pacientes WHERE Nombre LIKE %s"
        elif comboValue == "Apellido":
            consulta = "SELECT * FROM pacientes WHERE Papellido LIKE %s"
        elif comboValue == "Fecha de Nacimiento":
            consulta = "SELECT * FROM pacientes WHERE fecha_de_nac LIKE %s"
        elif comboValue == "Dni":
            consulta = "SELECT * FROM pacientes WHERE dni LIKE %s"
        elif comboValue == "Direccion":
            consulta = "SELECT * FROM pacientes WHERE direc LIKE %s"
        elif comboValue == "Telefono":
            consulta = "SELECT * FROM pacientes WHERE telefono LIKE %s"
        elif comboValue != "Codigo de Paciente" or comboValue != "Nombre" or comboValue != "Apellido" or comboValue != "Fecha de Nacimiento" or comboValue != "Dni" or comboValue != "Direccion" or comboValue != "Telefono":
            messagebox.showinfo("Columna no válida", "La columna seleccionada no es válida.")
        cursor = conexion.cursor()
        cursor.execute(consulta, ("%" + searchValue + "%",))
        registros = cursor.fetchall()
        cursor.close()
        for a in tree.get_children():
            tree.delete(a)

        if searchValue == "":
            for a in tree.get_children():
                tree.delete(a)
        else:
            for registro in registros:
                tree.insert("", "end", values=registro)

    searchFrame = tk.Frame(root, background="#bc6c25")
    searchFrame.pack(pady=10)

    comboSearch = ttk.Combobox(searchFrame, values=["Nombre", "Apellido", "Fecha de Nacimiento", "Dni", "Direccion", "Telefono"], width=44)
    comboSearch.pack(side="left", padx=10)

    search = tk.Entry(searchFrame, width=44, font=roboto)
    search.pack(side="left", padx=10)

    search.bind("<KeyRelease>", columnSearch)

    tree_frame = tk.Frame(root, background="#bc6c25")
    tree_frame.pack(pady=10)

    tree = ttk.Treeview(tree_frame, columns=("Cod Paciente", "Nombre", "Apellido", "Fecha de N", "Dni", "Direccion", "Telefono"))

    for c in range(1,7):
        tree.column(f"#{c}", width=127, anchor="center")
        tree.column("#0", width=0, anchor="center")
        tree.column("#7", width=127, anchor="center")

    headings = ["Cod Paciente", "Nombre", "Apellido", "Fecha de N", "Dni", "Direccion", "Telefono"]

    for e in range(7):
        headNum = [1,2,3,4,5,6,7]
        tree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    tree.bind("<Double-1>", on_tree_double_click)


    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)


    tree.grid(row=0, column=0, sticky="nsew")


    scrollbar.grid(row=0, column=1, sticky="ns")


    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

    textbox_frame = tk.Frame(root, background="#bc6c25")
    textbox_frame.pack(pady=10)

    labels = ["Código de Paciente", "Nombre", "Apellido", "Fecha de Nacimiento", "DNI", "Dirección", "Teléfono"]

    for i in range(7):
        label = tk.Label(textbox_frame, text=f"{labels[i]}", background="#bc6c25", foreground="#fefefe", font=roboto)
        label.grid(row=1, column=i, padx=5, pady=5)


    def saltoEntry(event, sigEntry):
        sigEntry.focus_set()

    codVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    codVar.grid(row=2, column=0, padx=2, pady=5)


    nombreVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    nombreVar.grid(row=2, column=1, padx=2, pady=5)


    apellidoVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    apellidoVar.grid(row=2, column=2, padx=2, pady=5)


    fechaVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    fechaVar.grid(row=2, column=3, padx=2, pady=5)


    dniVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    dniVar.grid(row=2, column=4, padx=2, pady=5)


    direcVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    direcVar.grid(row=2, column=5, padx=2, pady=5)


    telefonoVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    telefonoVar.grid(row=2, column=6, padx=2, pady=5)

    codVar.bind('<Return>', lambda event, entry=nombreVar: saltoEntry(event, entry))
    nombreVar.bind('<Return>', lambda event, entry=apellidoVar: saltoEntry(event, entry))
    apellidoVar.bind('<Return>', lambda event, entry=fechaVar: saltoEntry(event, entry))
    fechaVar.bind('<Return>', lambda event, entry=dniVar: saltoEntry(event, entry))
    dniVar.bind('<Return>', lambda event, entry=direcVar: saltoEntry(event, entry))
    direcVar.bind('<Return>', lambda event, entry=telefonoVar: saltoEntry(event, entry))
    
    btn_frame = tk.Frame(root, background="#bc6c25")
    btn_frame.pack(pady=10, padx=30)

    btn_cargar_registro = tk.Button(btn_frame, text="Cargar Registro", command=cargarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_modificar = tk.Button(btn_frame, text="Modificar Registro", command=modificarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_eliminar = tk.Button(btn_frame, text="Eliminar Registro", command=eliminarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_volcar = tk.Button(btn_frame, text="Buscar sin Filtros", command=volcarTodo, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)

    btn_cargar_registro.pack(side="left", padx=10, pady=10)
    btn_modificar.pack(side="left", padx=10, pady=10)
    btn_eliminar.pack(side="left", padx=10, pady=10)
    btn_volcar.pack(side="left", padx=10, pady=10)

    root.mainloop()


def ventanaMedicos():

    root = tk.Tk()
    root.title("Medicos")
    root.geometry("1108x500")
    root.iconbitmap("resources/imagenn.ico")
    root.configure(bg="#bc6c25")
    root.resizable(False, False)

    centrar_ventana(root)

    def abrirInicio():
        root.withdraw()
        ventanaInicio()

    def abrirPacientes():
        root.withdraw()
        ventanaPacientes()

    def abrirMedicos():
        root.withdraw()
        ventanaMedicos()

    def abrirHistoriasClinicas():
        root.withdraw()
        ventanaHistoriasClinicas()

    def abrirTurnos():
        root.withdraw()
        ventanaTurnos()

    def abrirAsignarT():
        root.withdraw()
        ventanaAsignarT()

    def abrirInternaciones():
        root.withdraw()
        ventanaInternaciones()

    def abrirAsignarI():
        root.withdraw()
        ventanaAsignarI()

    def abrirEspecialidades():
        root.withdraw()
        ventanaEspecialidades()

    def abrirPatologias():
        root.withdraw()
        ventanaPatologias()

    def abrirUsuarios():
        root.withdraw()
        ventanaUsuarios()

    navFrame = tk.Frame(root)
    navFrame.pack()

    variables = ["btnInicio", "btnPacientes", "btnMedicos", "btnHistoriasClinicas", "Asignar Turnos", "btnTurnos", "btnInternaciones", "Asignar Internacion", "btnEspecialidades", "btnPatologias", "btnUsuarios"]

    textos = ["Inicio", "Pacientes", "Medicos", "Historias Clinicas", "Turnos", "Asignar \n Turnos", "Internaciones", "Asignar \n Internacion", "Especialidades", "Patologias", "Usuarios"]

    comandos = [abrirInicio, abrirPacientes, abrirMedicos, abrirHistoriasClinicas, abrirTurnos, abrirAsignarT, abrirInternaciones, abrirAsignarI, abrirEspecialidades, abrirPatologias, abrirUsuarios]
    
    roboto = ("Roboto", 8, "bold")

    for i in range(len(variables)):
        button = variables[i]
        button = tk.Button(navFrame, text=f"{textos[i]}", width=13, height=2, command=comandos[i], background="#6c757d", foreground="#fefefe", font=roboto)
        button.pack(side="left")

    def actualizar_treeview():
        cursor = conexion.cursor()
        if tree.get_children():
            tree.delete(*tree.get_children())
        select_query = "SELECT * FROM medicos" 
        cursor.execute(select_query)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        cursor.close()


    def modificarRegistro():
        codValue = codVar.get()
        nombreValue = nombreVar.get()
        papellidoValue = apellidoVar.get()
        fechaDeNacValue = fechaVar.get()
        dniValue = dniVar.get()
        direcValue = direcVar.get()
        telefonoValue = telefonoVar.get()  
        especialidadValue = especialidadVar.get()     

        
        if codValue == "" or nombreValue == "" or papellidoValue == "" or fechaDeNacValue == "" or dniValue == "" or direcValue == "" or telefonoValue == "" or especialidadValue == "" :
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            cursor = conexion.cursor()
            valor = (codValue,)
            consulta2 = "SELECT * FROM medicos WHERE cod_medico = %s"
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchone()
            cursor.close()
            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea modificar el registro?")
                if confirmacion:
                    cursor = conexion.cursor()
                    valor = (especialidadValue,)
                    consulta1 = "SELECT cod_especialidad FROM especialidades WHERE Especialidad = %s"
                    cursor.execute(consulta1, valor)
                    resultado1 = cursor.fetchone()
                    cursor.close()
                    cursor = conexion.cursor()
                    consulta2 = "SELECT * FROM especialidades WHERE cod_especialidad = %s"
                    cursor.execute(consulta2, valor)
                    resultado2 = cursor.fetchone()
                    cursor.close()
                    if resultado1 or resultado2: 
                        if resultado1:
                            resultado = resultado1
                        elif resultado2:
                            resultado = resultado2

                        update_query = "UPDATE medicos SET Nombre = %s, Mapellido = %s, fecha_de_nac = %s, dni = %s, direc = %s, telefono = %s, especialidad = %s WHERE cod_medico = %s "
                        valores = (nombreValue, papellidoValue, fechaDeNacValue, dniValue, direcValue, telefonoValue, resultado[0], codValue,)
                        cursor = conexion.cursor()
                        cursor.execute(update_query, valores)
                        conexion.commit()
                        cursor.close()
                        messagebox.showinfo("Exito", "El registro ha sido modificado exitosamente.")

                        actualizar_treeview()

                        textos = [codVar, nombreVar, apellidoVar, fechaVar, dniVar, direcVar, telefonoVar, especialidadVar]

                        for i in range(len(textos)):
                                nuevo_valor = "" 
                                textos[i].delete(0, tk.END)
                                textos[i].insert(0, nuevo_valor)
                    
                    else:
                        messagebox.showerror("Error", "La especialidad ingresada no existe.")
                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera modificado.")
            else:
                messagebox.showerror("Error", "El codigo de medico ingresado no existe.")





    def cargarRegistro():
        nombreValue = str(nombreVar.get()).strip()
        mapellidoValue = str(apellidoVar.get()).strip()
        fechaDeNacValue = str(fechaVar.get()).strip()
        dniValue = str(dniVar.get()).strip()
        direcValue = str(direcVar.get()).strip()
        telefonoValue = str(telefonoVar.get()).strip()
        especialidadValue = str(especialidadVar.get()).strip()

        if nombreValue == "" or mapellidoValue == "" or fechaDeNacValue == "" or dniValue == "" or direcValue == "" or telefonoValue == "" or especialidadValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            cursor = conexion.cursor()
            valor = (especialidadValue,)
            consulta2 = "SELECT cod_especialidad FROM especialidades WHERE Especialidad = %s"
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchone()
            cursor.nextset()
            cursor.close()
            if resultado:
                insert_query = "INSERT INTO medicos (Nombre, Mapellido, fecha_de_nac, dni, direc, telefono, especialidad) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                valores = (nombreValue, mapellidoValue, fechaDeNacValue, dniValue, direcValue, telefonoValue, resultado[0])
                cursor = conexion.cursor()
                cursor.execute(insert_query, valores)
                conexion.commit()
                messagebox.showinfo("Éxito", "El registro ha sido cargado exitosamente.")
                actualizar_treeview()
                cursor.close()
                textos = [codVar, nombreVar, apellidoVar, fechaVar, dniVar, direcVar, telefonoVar, especialidadVar]

                for i in range(len(textos)):
                    nuevo_valor = ""
                    textos[i].delete(0, tk.END)
                    textos[i].insert(0, nuevo_valor)
            else:
                messagebox.showerror("Error", "La especialidad ingresada no existe.")


    def eliminarRegistro():
        id_to_delete = codVar.get()

        if id_to_delete == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else: 
            cursor = conexion.cursor()
            valor = (id_to_delete,)
            consulta2 = "SELECT * FROM medicos WHERE cod_medico = %s"
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchall()
            cursor.close()
            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar el registro?")
                if confirmacion:
                    valores = (id_to_delete,)
                    delete_query = "DELETE FROM medicos WHERE cod_medico = %s"
                    cursor = conexion.cursor()
                    cursor.execute(delete_query, valores)
                    conexion.commit()
                    cursor.close()
                    messagebox.showinfo("Exito", "El registro ha sido eliminado exitosamente.")
                    actualizar_treeview()

                    textos = [codVar, nombreVar, apellidoVar, fechaVar, dniVar, direcVar, telefonoVar, especialidadVar]

                    for i in range(len(textos)):
                        nuevo_valor = "" 
                        textos[i].delete(0, tk.END)
                        textos[i].insert(0, nuevo_valor)

                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera eliminado.")
            else:
                messagebox.showerror("Error", "El codigo de medico ingresado no existe.")


    def volcarTodo():
        consulta = "SELECT * FROM medicos"

        cursor = conexion.cursor()
        cursor.execute(consulta)
        registros = cursor.fetchall()

        cursor.close()

        for a in tree.get_children():
            tree.delete(a)
            

        for registro in registros:
            tree.insert("", "end", values=registro)

    def on_tree_double_click(event):
        item = tree.selection()[0]
        values = tree.item(item, "values")

        textboxx = [codVar, nombreVar, apellidoVar, fechaVar, dniVar, direcVar, telefonoVar, especialidadVar]

        for index, value in enumerate(values):
            textboxx[index].delete(0, tk.END)
            textboxx[index].insert(0, value)


    def columnSearch(event):
        comboValue = comboSearch.get()
        searchValue = search.get()

        consulta = None

        if comboValue == "":
            messagebox.showinfo("Campo Vacio", "El selector se encuentra vacio.")
        elif comboValue == "Nombre":
            consulta = "SELECT * FROM medicos WHERE Nombre LIKE %s"
        elif comboValue == "Apellido":
            consulta = "SELECT * FROM medicos WHERE Mapellido LIKE %s"
        elif comboValue == "Fecha de Nacimiento":
            consulta = "SELECT * FROM medicos WHERE fecha_de_nac LIKE %s"
        elif comboValue == "Dni":
            consulta = "SELECT * FROM medicos WHERE dni LIKE %s"
        elif comboValue == "Direccion":
            consulta = "SELECT * FROM medicos WHERE direc LIKE %s"
        elif comboValue == "Telefono":
            consulta = "SELECT * FROM medicos WHERE telefono LIKE %s"
        elif comboValue == "Especialidad":
            consulta = "SELECT cod_especialidad FROM especialidades WHERE Especialidad LIKE %s"
        
        if comboValue == "Nombre" or comboValue == "Apellido" or comboValue == "Fecha de Nacimiento" or comboValue == "Dni" or comboValue == "Direccion" or comboValue == "Telefono":
            cursor = conexion.cursor()
            cursor.execute(consulta, ("%" + searchValue + "%",))
            registros = cursor.fetchall()
            cursor.close()
        elif comboValue == "Especialidad":
            cursor = conexion.cursor()
            cursor.execute(consulta, ("%" + searchValue + "%",))
            registros = cursor.fetchall()
            cursor.nextset()
            cursor.close()
            if len(registros) > 0:
                cursor = conexion.cursor()
                valor = (registros[0])
                consulta1 = "SELECT * FROM medicos WHERE especialidad LIKE %s"
                cursor.execute(consulta1, valor)
                registros = cursor.fetchall()
                cursor.nextset()
                cursor.close()
            else:
                messagebox.showinfo("Sin registros", "No se han encontrado turnos asociados a ese paciente.")

        elif comboValue != "Nombre" or comboValue != "Apellido" or comboValue != "Fecha de Nacimiento" or comboValue != "Dni" or comboValue != "Direccion" or comboValue != "Telefono" or comboValue != "Especialidad":
            messagebox.showinfo("Columna no válida", "La columna seleccionada no es válida.")

        for a in tree.get_children():
            tree.delete(a)

        if searchValue == "":
            for a in tree.get_children():
                tree.delete(a)
        else:
            for registro in registros:
                tree.insert("", "end", values=registro)


    searchFrame = tk.Frame(root, background="#bc6c25")
    searchFrame.pack(pady=10)

    comboSearch = ttk.Combobox(searchFrame, values=["Nombre", "Apellido", "Fecha de Nacimiento", "Dni", "Direccion", "Telefono", "Especialidad"], width=44)
    comboSearch.pack(side="left", padx=10)

    search = tk.Entry(searchFrame, width=44, font=roboto)
    search.pack(side="left", padx=10)

    search.bind("<KeyRelease>", columnSearch)

    tree_frame = tk.Frame(root, background="#bc6c25")
    tree_frame.pack(pady=10)

    tree = ttk.Treeview(tree_frame, columns=("Cod Medico", "Nombre", "Apellido", "Fecha de N", "Dni", "Direccion", "Telefono", "Especialidad"))

    for c in range(1,8):
        tree.column(f"#{c}", width=127, anchor="center")
        tree.column("#0", width=0, anchor="center")
        tree.column("#8", width=127, anchor="center")

    headings = ["Cod Medico", "Nombre", "Apellido", "Fecha de N", "Dni", "Direccion", "Telefono", "Especialidad"]

    for e in range(8):
        headNum = [1,2,3,4,5,6,7,8]
        tree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    tree.bind("<Double-1>", on_tree_double_click)


    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)


    tree.grid(row=0, column=0, sticky="nsew")


    scrollbar.grid(row=0, column=1, sticky="ns")


    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

    textbox_frame = tk.Frame(root, background="#bc6c25")
    textbox_frame.pack(pady=10)

    labels = ["Código de Medico", "Nombre", "Apellido", "Fecha de Nacimiento", "DNI", "Dirección", "Teléfono", "Especialidad"]

    for i in range(len(labels)):
        label = tk.Label(textbox_frame, text=f"{labels[i]}", background="#bc6c25", foreground="#fefefe", font=roboto)
        label.grid(row=1, column=i, padx=5, pady=5)


    def saltoEntry(event, sigEntry):
        sigEntry.focus_set()

    codVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    codVar.grid(row=2, column=0, padx=2, pady=5)

    nombreVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    nombreVar.grid(row=2, column=1, padx=2, pady=5)

    apellidoVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    apellidoVar.grid(row=2, column=2, padx=2, pady=5)

    fechaVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    fechaVar.grid(row=2, column=3, padx=2, pady=5)

    dniVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    dniVar.grid(row=2, column=4, padx=2, pady=5)

    direcVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    direcVar.grid(row=2, column=5, padx=2, pady=5)

    telefonoVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    telefonoVar.grid(row=2, column=6, padx=2, pady=5)

    especialidadVar = ttk.Combobox(textbox_frame, width=20, font=roboto)
    especialidadVar.grid(row=2, column=7, padx=2, pady=5)
    
    cursor = conexion.cursor()
    sqlEsp = "SELECT Especialidad FROM especialidades"
    cursor.execute(sqlEsp)
    resultados = cursor.fetchall()
    cursor.close()

    for i in resultados:
        especialidadVar["values"] = (*especialidadVar["values"], i)

    codVar.bind('<Return>', lambda event, entry=nombreVar: saltoEntry(event, entry))
    nombreVar.bind('<Return>', lambda event, entry=apellidoVar: saltoEntry(event, entry))
    apellidoVar.bind('<Return>', lambda event, entry=fechaVar: saltoEntry(event, entry))
    fechaVar.bind('<Return>', lambda event, entry=dniVar: saltoEntry(event, entry))
    dniVar.bind('<Return>', lambda event, entry=direcVar: saltoEntry(event, entry))
    direcVar.bind('<Return>', lambda event, entry=telefonoVar: saltoEntry(event, entry))
    telefonoVar.bind('<Return>', lambda event, entry=especialidadVar: saltoEntry(event, entry))


    btn_frame = tk.Frame(root, background="#bc6c25")
    btn_frame.pack(pady=10, padx=30)

    btn_cargar_registro = tk.Button(btn_frame, text="Cargar Registro", command=cargarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_modificar = tk.Button(btn_frame, text="Modificar Registro", command=modificarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_eliminar = tk.Button(btn_frame, text="Eliminar Registro", command=eliminarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_volcar = tk.Button(btn_frame, text="Buscar sin Filtros", command=volcarTodo, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)

    btn_cargar_registro.pack(side="left", padx=10, pady=10)
    btn_modificar.pack(side="left", padx=10, pady=10)
    btn_eliminar.pack(side="left", padx=10, pady=10)
    btn_volcar.pack(side="left", padx=10, pady=10)


    root.mainloop()


def ventanaHistoriasClinicas():

    root = tk.Tk()
    root.title("Historias Clinicas")
    root.geometry("1108x620")
    root.iconbitmap("resources/imagenn.ico")
    root.configure(bg="#bc6c25")
    root.resizable(False, False)

    centrar_ventana(root)

    def abrirInicio():
        root.withdraw()
        ventanaInicio()

    def abrirPacientes():
        root.withdraw()
        ventanaPacientes()

    def abrirMedicos():
        root.withdraw()
        ventanaMedicos()

    def abrirHistoriasClinicas():
        root.withdraw()
        ventanaHistoriasClinicas()

    def abrirTurnos():
        root.withdraw()
        ventanaTurnos()

    def abrirAsignarT():
        root.withdraw()
        ventanaAsignarT()

    def abrirInternaciones():
        root.withdraw()
        ventanaInternaciones()

    def abrirAsignarI():
        root.withdraw()
        ventanaAsignarI()

    def abrirEspecialidades():
        root.withdraw()
        ventanaEspecialidades()

    def abrirPatologias():
        root.withdraw()
        ventanaPatologias()

    def abrirUsuarios():
        root.withdraw()
        ventanaUsuarios()

    navFrame = tk.Frame(root)
    navFrame.pack()

    variables = ["btnInicio", "btnPacientes", "btnMedicos", "btnHistoriasClinicas", "Asignar Turnos", "btnTurnos", "btnInternaciones", "Asignar Internacion", "btnEspecialidades", "btnPatologias", "btnUsuarios"]

    textos = ["Inicio", "Pacientes", "Medicos", "Historias Clinicas", "Turnos", "Asignar \n Turnos", "Internaciones", "Asignar \n Internacion", "Especialidades", "Patologias", "Usuarios"]

    comandos = [abrirInicio, abrirPacientes, abrirMedicos, abrirHistoriasClinicas, abrirTurnos, abrirAsignarT, abrirInternaciones, abrirAsignarI, abrirEspecialidades, abrirPatologias, abrirUsuarios]

    roboto = ("Roboto", 8, "bold")

    for i in range(len(variables)):
        button = variables[i]
        button = tk.Button(navFrame, text=f"{textos[i]}", width=13, height=2, command=comandos[i], background="#6c757d", foreground="#fefefe", font=roboto)
        button.pack(side="left")

    def actualizar_treeview():
        cursor = conexion.cursor()
        if tree.get_children():
            tree.delete(*tree.get_children())  # Eliminar todas las filas excepto la raíz
        select_query = "SELECT * FROM historia_clinica" 
        cursor.execute(select_query)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        cursor.close()

    def modificarRegistro():
        codValue = cod_hist_var.get()
        pacienteValue = paciente_var.get()
        fechaValue = fecha_var.get()
        histValue = hist_var.get("1.0", "end-1c")
        
        if codValue == "" or pacienteValue == "" or fechaValue == "" or histValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            cursor = conexion.cursor()
            valor = (codValue,)
            consulta2 = "SELECT * FROM historia_clinica WHERE cod_historia = %s"
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchone()
            cursor.close()

            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea modificar el registro?")
                if confirmacion:

                    cursor = conexion.cursor()
                    valor = (pacienteValue,)
                    consulta1 = "SELECT cod_paciente FROM pacientes WHERE dni = %s"
                    cursor.execute(consulta1, valor)
                    resultado1 = cursor.fetchone()
                    cursor.close()

                    cursor = conexion.cursor()
                    consulta2 = "SELECT * FROM pacientes WHERE cod_paciente = %s"
                    cursor.execute(consulta2, valor)
                    resultado2 = cursor.fetchone()
                    cursor.close()

                    if resultado1 or resultado2: 
                        if resultado1:
                            resultado = resultado1
                        elif resultado2:
                            resultado = resultado2

                        update_query = "UPDATE historia_clinica SET descripcion = %s, paciente = %s, fecha = %s WHERE cod_historia = %s"
                        valores = (histValue, resultado[0], fechaValue, codValue,)
                        cursor = conexion.cursor()
                        cursor.execute(update_query, valores)
                        conexion.commit()
                        cursor.close()
                        messagebox.showinfo("Exito", "El registro ha sido modificado exitosamente.")
                        actualizar_treeview()

                        textCamp = [cod_hist_var, paciente_var, fecha_var]

                        for i in range(len(textCamp)):
                            nuevo_valor = ""  # Reemplaza esto con el valor que deseas cargar
                            textCamp[i].delete(0, tk.END)  # Borra cualquier texto existente
                            textCamp[i].insert(0, nuevo_valor)
                            hist_var.delete('1.0', 'end')
                            hist_var.insert('1.0', nuevo_valor)

                    else:
                        messagebox.showerror("Error", "El paciente ingresado no existe.")
                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera modificado.")
            else:
                messagebox.showerror("Error", "El codigo de historia clinica ingresado no existe.")



    def cargarRegistro():
        pacienteValue = paciente_var.get()
        fechaValue = fecha_var.get()
        histValue = hist_var.get("1.0", "end-1c")

        
        if histValue == "" or pacienteValue == "" or fechaValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            cursor = conexion.cursor()
            valor = (pacienteValue,)
            consulta2 = "SELECT cod_paciente FROM pacientes WHERE dni = %s"
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchone()
            cursor.close()

            if resultado:
                insert_query = "INSERT INTO historia_clinica (descripcion, paciente, fecha) VALUES (%s, %s, %s)"
                valores = (histValue, resultado[0], fechaValue,)
                cursor = conexion.cursor()
                cursor.execute(insert_query, valores)
                messagebox.showinfo("Éxito", "El registro ha sido cargado exitosamente.")
                conexion.commit()
                cursor.close()
                actualizar_treeview()

                textCamp = [cod_hist_var, paciente_var, fecha_var]

                for i in range(len(textCamp)):
                    nuevo_valor = ""  # Reemplaza esto con el valor que deseas cargar
                    textCamp[i].delete(0, tk.END)  # Borra cualquier texto existente
                    textCamp[i].insert(0, nuevo_valor)
                    hist_var.delete('1.0', 'end')
                    hist_var.insert('1.0', nuevo_valor)
            
            else:
                messagebox.showerror("Error", "El paciente ingresado no existe.")



    # Función para eliminar un registro de la base de datos
    def eliminarRegistro():
        id_to_delete = cod_hist_var.get()

        if id_to_delete == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else: 
            cursor = conexion.cursor()
            valor = (id_to_delete,)
            consulta2 = "SELECT * FROM historia_clinica WHERE cod_historia = %s"
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchall()
            cursor.close()

            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar el registro?")
                if confirmacion:
                    valores = (id_to_delete,)
                    delete_query = "DELETE FROM historia_clinica WHERE cod_historia = %s"
                    cursor = conexion.cursor()
                    cursor.execute(delete_query, valores)
                    conexion.commit()
                    cursor.close()
                    messagebox.showinfo("Exito", "El registro ha sido eliminado exitosamente.")
                    actualizar_treeview()

                    textCamp = [cod_hist_var, paciente_var, fecha_var]

                    for i in range(len(textCamp)):
                        nuevo_valor = ""  # Reemplaza esto con el valor que deseas cargar
                        textCamp[i].delete(0, tk.END)  # Borra cualquier texto existente
                        textCamp[i].insert(0, nuevo_valor)
                        hist_var.delete('1.0', 'end')
                        hist_var.insert('1.0', nuevo_valor)
                        
                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera eliminado.")
            else:
                messagebox.showerror("Error", "El codigo de historia clinica ingresado no existe.")

    # Función para volcar datos desde la base de datos al Treeview
    def volcarTodo():
        consulta = "SELECT * FROM historia_clinica"

        cursor = conexion.cursor()
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()

        for a in tree.get_children():
            tree.delete(a)
            
            # Llenar el Treeview con los datos
        for registro in registros:
            tree.insert("", "end", values=registro)



    def on_tree_double_click(event):        
        # Obtén el registro seleccionado en el Treeview
        seleccion = tree.selection()
        if seleccion:
            item = seleccion[0]
            valores = tree.item(item, 'values')
            
            # Actualiza los Entry widgets con los primeros tres valores
            cod_hist_var.delete(0, 'end')
            paciente_var.delete(0, 'end')
            fecha_var.delete(0, 'end')
            cod_hist_var.insert(0, valores[0])
            paciente_var.insert(0, valores[2])
            fecha_var.insert(0, valores[3])
            
            # Actualiza el Text widget con el cuarto valor
            hist_var.delete('1.0', 'end')
            hist_var.insert('1.0', valores[1])



    def columnSearch(event):
        comboValue = comboSearch.get()
        searchValue = search.get()

        consulta = None

        if comboValue == "":
            messagebox.showinfo("Campo Vacio", "El selector se encuentra vacio.")
        elif comboValue == "Paciente (Dni)":
            consulta = "SELECT cod_paciente FROM pacientes WHERE dni LIKE %s"
        elif comboValue == "Fecha":
            consulta = "SELECT * FROM historia_clinica WHERE fecha LIKE %s"
        
        if comboValue == "Fecha":
            cursor = conexion.cursor()
            cursor.execute(consulta, ("%" + searchValue + "%",))
            registros = cursor.fetchall()
            cursor.close()
        elif comboValue == "Paciente (Dni)":
            cursor = conexion.cursor()
            cursor.execute(consulta, ("%" + searchValue + "%",))
            registros = cursor.fetchall()
            cursor.nextset()
            cursor.close()
            if len(registros) > 0:
                cursor = conexion.cursor()
                valor = (registros[0])
                consulta1 = "SELECT * FROM historia_clinica WHERE paciente LIKE %s"
                cursor.execute(consulta1, valor)
                registros = cursor.fetchall()
                cursor.nextset()
                cursor.close()
            else:
                messagebox.showinfo("Sin registros", "No se ha encontrado ninguna historia clinica asociada a ese paciente.")
        elif comboValue != "Paciente (Dni)" or comboValue != "Fecha":
            messagebox.showinfo("Columna no válida", "La columna seleccionada no es válida.")


        for a in tree.get_children():
            tree.delete(a)

        if searchValue == "":    
            for a in tree.get_children():
                tree.delete(a)
        else:
            for registro in registros:
                tree.insert("", "end", values=registro)


    searchFrame = tk.Frame(root, background="#bc6c25")
    searchFrame.pack(pady=10)

    comboSearch = ttk.Combobox(searchFrame, values=["Paciente (Dni)", "Fecha"], width=45)
    comboSearch.pack(side="left", padx=10)

    # TextBox para mostrar los resultados
    search = tk.Entry(searchFrame, width=45, font=roboto)
    search.pack(side="left", padx=10)

    search.bind("<KeyRelease>", columnSearch)

    # Treeview
    tree_frame = tk.Frame(root, background="#bc6c25")
    tree_frame.pack(pady=10)

    tree = ttk.Treeview(tree_frame, columns=("Cod Historia", "Descripcion", "Paciente", "Fecha"))

    for c in range(1,5):
        tree.column(f"#{c}", width=250, anchor="center")
        tree.column("#0", width=0, anchor="center")

    headings = ["Cod Historia", "Descripcion", "Paciente", "Fecha"]

    for e in range(min(len(headings), 4)):
        headNum = [1, 2, 3, 4]
        tree.heading(f"#{headNum[e]}", text=f"{headings[e]}")

    tree.bind("<Double-1>", on_tree_double_click)

    # Barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    # Colocar el Treeview usando grid
    tree.grid(row=0, column=0, sticky="nsew")

    # Colocar el scrollbar junto al Treeview usando grid
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configurar el peso de las filas y columnas para que el Treeview se expanda correctamente
    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)


    generalFrame = tk.Frame(root, background="#bc6c25")
    generalFrame.pack()

    # Etiquetas y TextBox
    textbox_frame = tk.Frame(generalFrame, background="#bc6c25")
    textbox_frame.pack(side="left", pady=10)

    labels = ["Codigo de Historia", "Paciente", "Fecha"]

    for i in range(len(labels)):
        ubication = [1, 3, 5]
        label = tk.Label(textbox_frame, text=labels[i], background="#bc6c25", foreground="#fefefe", font=roboto)
        label.grid(row=ubication[i], column=0, padx=10, pady=5)
        labels.append(label)


    def saltoEntry(event, sigEntry):
        sigEntry.focus_set()

    cod_hist_var = tk.Entry(textbox_frame, width=20, font=roboto)
    cod_hist_var.grid(row=2, column=0, padx=5, pady=5)

    paciente_var = ttk.Combobox(textbox_frame, width=20, font=roboto)
    paciente_var.grid(row=4, column=0, padx=5, pady=5)

    sqlPac = "SELECT dni FROM pacientes"
    cursor = conexion.cursor()
    cursor.execute(sqlPac)
    resultados = cursor.fetchall()
    cursor.close()

    for i in resultados:
        paciente_var["values"] = (*paciente_var["values"], i)

    fecha_var = tk.Entry(textbox_frame, width=20, font=roboto)
    fecha_var.grid(row=6, column=0, padx=5, pady=5)

    hist_frame = tk.Frame(generalFrame, background="#bc6c25")
    hist_frame.pack(side="left", pady=10, padx=10)

    histLabel = tk.Label(hist_frame, text="Descripcion", width=10, background="#bc6c25", foreground="#fefefe", font=roboto)
    histLabel.grid(row=0, column=0, pady=5)

    hist_var = tk.Text(hist_frame, width=50, height=8.5, font=roboto)
    hist_var.grid(row=1, column=0, pady=5)

    cod_hist_var.bind('<Return>', lambda event, entry=paciente_var: saltoEntry(event, entry))
    paciente_var.bind('<Return>', lambda event, entry=fecha_var: saltoEntry(event, entry))
    fecha_var.bind('<Return>', lambda event, entry=hist_var: saltoEntry(event, entry))


    # Crear una barra de desplazamiento vertical
    scrollbarHistoria = tk.Scrollbar(hist_frame, command=hist_var.yview)
    scrollbarHistoria.grid(row=1, column=1, sticky="ns")

    # Configurar la barra de desplazamiento para el widget Text
    hist_var.config(yscrollcommand=scrollbarHistoria.set)




    btn_frame = tk.Frame(root, background="#bc6c25")
    btn_frame.pack(pady=10, padx=30)

    btn_cargar_registro = tk.Button(btn_frame, text="Cargar Registro", command=cargarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_modificar = tk.Button(btn_frame, text="Modificar Registro", command=modificarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_eliminar = tk.Button(btn_frame, text="Eliminar Registro", command=eliminarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_volcar = tk.Button(btn_frame, text="Buscar sin Filtros", command=volcarTodo, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)

    btn_cargar_registro.pack(side="left", padx=10, pady=10)
    btn_modificar.pack(side="left", padx=10, pady=10)
    btn_eliminar.pack(side="left", padx=10, pady=10)
    btn_volcar.pack(side="left", padx=10, pady=10)


    root.mainloop()


def ventanaTurnos():

    root = tk.Tk()
    root.title("Turnos")
    root.geometry("1108x500")
    root.iconbitmap("resources/imagenn.ico")
    root.configure(bg="#bc6c25")
    root.resizable(False, False)

    centrar_ventana(root)

    def abrirInicio():
        root.withdraw()
        ventanaInicio()

    def abrirPacientes():
        root.withdraw()
        ventanaPacientes()

    def abrirMedicos():
        root.withdraw()
        ventanaMedicos()

    def abrirHistoriasClinicas():
        root.withdraw()
        ventanaHistoriasClinicas()

    def abrirTurnos():
        root.withdraw()
        ventanaTurnos()

    def abrirAsignarT():
        root.withdraw()
        ventanaAsignarT()

    def abrirInternaciones():
        root.withdraw()
        ventanaInternaciones()

    def abrirAsignarI():
        root.withdraw()
        ventanaAsignarI()

    def abrirEspecialidades():
        root.withdraw()
        ventanaEspecialidades()

    def abrirPatologias():
        root.withdraw()
        ventanaPatologias()

    def abrirUsuarios():
        root.withdraw()
        ventanaUsuarios()

    navFrame = tk.Frame(root)
    navFrame.pack()

    variables = ["btnInicio", "btnPacientes", "btnMedicos", "btnHistoriasClinicas", "Asignar Turnos", "btnTurnos", "btnInternaciones", "Asignar Internacion", "btnEspecialidades", "btnPatologias", "btnUsuarios"]

    textos = ["Inicio", "Pacientes", "Medicos", "Historias Clinicas", "Turnos", "Asignar \n Turnos", "Internaciones", "Asignar \n Internacion", "Especialidades", "Patologias", "Usuarios"]

    comandos = [abrirInicio, abrirPacientes, abrirMedicos, abrirHistoriasClinicas, abrirTurnos, abrirAsignarT, abrirInternaciones, abrirAsignarI, abrirEspecialidades, abrirPatologias, abrirUsuarios]

    roboto = ("Roboto", 8, "bold")

    for i in range(len(variables)):
        button = variables[i]
        button = tk.Button(navFrame, text=f"{textos[i]}", width=13, height=2, command=comandos[i], background="#6c757d", foreground="#fefefe", font=roboto)
        button.pack(side="left")

    def actualizar_treeview():

        cursor = conexion.cursor()
        if tree.get_children():
            tree.delete(*tree.get_children())
        select_query = "SELECT * FROM turnos" 
        cursor.execute(select_query)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        cursor.close()

    def modificarRegistro():
        codValue = codVar.get()
        fechaValue = fechaVar.get()
        horaValue = horaVar.get()
        pacienteValue = pacienteVar.get()
        medicoValue = medicoVar.get()
       
        if codValue == "" or fechaValue == "" or horaValue == "" or pacienteValue == "" or medicoValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            valor = (codValue,)
            consulta2 = "SELECT * FROM turnos WHERE cod_turno = %s"
            cursor = conexion.cursor()
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchone()
            cursor.close()
            
            if resultado:
                    valor1 = (pacienteValue,)
                    consulta1 = "SELECT cod_paciente FROM pacientes WHERE dni = %s"
                    cursor = conexion.cursor()
                    cursor.execute(consulta1, valor1)
                    resultado1 = cursor.fetchone()
                    cursor.close()

                    consulta5 = "SELECT * FROM pacientes WHERE cod_paciente = %s"
                    cursor = conexion.cursor()
                    cursor.execute(consulta5, valor1)
                    resultado2 = cursor.fetchone()
                    cursor.close()

                    valor2 = (medicoValue,)
                    consulta3 = "SELECT cod_medico FROM medicos WHERE dni = %s"
                    cursor = conexion.cursor()
                    cursor.execute(consulta3, valor2)
                    resultado3 = cursor.fetchone()
                    cursor.close()

                    consulta4 = "SELECT * FROM medicos WHERE cod_medico = %s"
                    cursor = conexion.cursor()
                    cursor.execute(consulta4, valor2)
                    resultado4 = cursor.fetchone()
                    cursor.close()

                    paciente = None
                    medico = None

                    if resultado1 or resultado2: 
                        if resultado1:
                            paciente = resultado1
                        elif resultado2:
                            paciente = resultado2

                    if resultado3 or resultado4: 
                        if resultado3:
                            medico = resultado3
                        elif resultado4:
                            medico = resultado4

                    if paciente and medico:
                            confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea modificar el registro?")
                            if confirmacion:
                                update_query = "UPDATE turnos SET fecha = %s, hora = %s, paciente = %s, medico = %s WHERE cod_turno = %s "
                                valores = (fechaValue, horaValue, paciente[0], medico[0], codValue)

                                cursor = conexion.cursor()
                                cursor.execute(update_query, valores)
                                conexion.commit()
                                cursor.close()

                                messagebox.showinfo("Exito", "El registro ha sido modificado exitosamente.")
                                actualizar_treeview()

                                textos = [codVar, fechaVar, horaVar, pacienteVar, medicoVar]

                                for i in range(len(textos)):
                                    nuevo_valor = "" 
                                    textos[i].delete(0, tk.END)
                                    textos[i].insert(0, nuevo_valor)
                            else:
                                messagebox.showinfo("Cancelacion", "El registro no sera modificado.")
                    else:
                        messagebox.showerror("Error", "El codigo de paciente o medico ingresado no existe.")
            else:
                messagebox.showerror("Error", "El codigo de turno ingresado no existe.")

    def eliminarRegistro():
        id_to_delete = codVar.get()

        if id_to_delete == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else: 
            valor = (id_to_delete,)
            sql = "SELECT * FROM turnos WHERE cod_turno = %s"

            cursor = conexion.cursor()
            cursor.execute(sql, valor)
            result = cursor.fetchall()
            cursor.close()

            if result:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar el registro?")
                if confirmacion:
                    valores = (id_to_delete,)
                    delete_query = "DELETE FROM turnos WHERE cod_turno = %s"
                    cursor = conexion.cursor()
                    cursor.execute(delete_query, valores)
                    conexion.commit()
                    cursor.close()
                    messagebox.showinfo("Exito", "El registro ha sido eliminado exitosamente.")
                    actualizar_treeview()

                    textos = [codVar, fechaVar, horaVar, pacienteVar, medicoVar]

                    for i in range(len(textos)):
                        nuevo_valor = "" 
                        textos[i].delete(0, tk.END)
                        textos[i].insert(0, nuevo_valor)
                        

                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera eliminado.")
            else:
                messagebox.showerror("Error", "El codigo de turno ingresado no existe.")


    def volcarTodo():
        consulta = "SELECT * FROM turnos"

        cursor = conexion.cursor()
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()

        for a in tree.get_children():
            tree.delete(a)

        for registro in registros:
            tree.insert("", "end", values=registro)

    def on_tree_double_click(event):
        item = tree.selection()[0]
        values = tree.item(item, "values")

        textboxx = [codVar, fechaVar, horaVar, pacienteVar, medicoVar]

        for index, value in enumerate(values):
            textboxx[index].delete(0, tk.END)
            textboxx[index].insert(0, value)


    def columnSearch(event):
        comboValue = comboSearch.get()
        searchValue = search.get()

        consulta = None
        valor = None

        if comboValue == "":
            messagebox.showinfo("Campo Vacio", "El selector se encuentra vacio.")
        elif comboValue == "Fecha":
            consulta = "SELECT * FROM turnos WHERE fecha LIKE %s"
        elif comboValue == "Hora":
            consulta = "SELECT * FROM turnos WHERE hora LIKE %s"
        elif comboValue == "Paciente (Dni)":
            consulta = "SELECT cod_paciente FROM pacientes WHERE dni LIKE %s"
        elif comboValue == "Medico (Dni)":
            consulta = "SELECT cod_medico FROM medicos WHERE dni LIKE %s"


        if comboValue == "Fecha" or comboValue == "Hora":
            cursor = conexion.cursor()
            cursor.execute(consulta, ("%" + searchValue + "%",))
            registros = cursor.fetchall()
            cursor.close()
        elif comboValue == "Paciente (Dni)":
            cursor = conexion.cursor()
            cursor.execute(consulta, ("%" + searchValue + "%",))
            registros = cursor.fetchall()
            cursor.nextset()
            cursor.close()
            if len(registros) > 0:
                cursor = conexion.cursor()
                valor = registros[0]
                consulta1 = "SELECT * FROM turnos WHERE paciente LIKE %s"
                cursor.execute(consulta1, valor)
                registros = cursor.fetchall()
                cursor.nextset()
                cursor.close()
            else:
                messagebox.showinfo("Sin registros", "No se han encontrado turnos asociados a ese paciente.")
        elif comboValue == "Medico (Dni)":
            cursor = conexion.cursor()
            cursor.execute(consulta, ("%" + searchValue + "%",))
            registros = cursor.fetchall()
            cursor.nextset()
            cursor.close()
            if len(registros) > 0:
                cursor = conexion.cursor()
                valor = registros[0]
                consulta1 = "SELECT * FROM turnos WHERE medico LIKE %s"
                cursor.execute(consulta1, valor)
                registros = cursor.fetchall()
                cursor.nextset()
                cursor.close()
            else:
                messagebox.showinfo("Sin registros", "No se han encontrado turnos asociados a ese medico.")

        elif comboValue != "Fecha" or comboValue != "Hora" or comboValue != "Paciente (Dni)" or comboValue != "Medico (Dni)":
            messagebox.showinfo("Columna no válida", "La columna seleccionada no es válida.")


        for a in tree.get_children():
            tree.delete(a)

        if searchValue == "":   
            for a in tree.get_children():
                tree.delete(a)
        else:
            for registro in registros:
                tree.insert("", "end", values=registro)

    searchFrame = tk.Frame(root, background="#bc6c25")
    searchFrame.pack(pady=10)

    comboSearch = ttk.Combobox(searchFrame, values=["Fecha", "Hora", "Paciente (Dni)", "Medico (Dni)"], width=30)
    comboSearch.pack(side="left", padx=10)

    search = tk.Entry(searchFrame, width=30, font=roboto)
    search.pack(side="left", padx=10)

    search.bind("<KeyRelease>", columnSearch)

    tree_frame = tk.Frame(root, background="#bc6c25")
    tree_frame.pack(pady=10)

    tree = ttk.Treeview(tree_frame, columns=("Cod Turno", "Fecha", "Hora", "Paciente", "Medico"))

    for c in range(1,5):
        tree.column(f"#{c}", width=127, anchor="center")
        tree.column("#0", width=0, anchor="center")
        tree.column("#5", width=127, anchor="center")

    headings = ["Cod Turno", "Fecha", "Hora", "Paciente", "Medico"]

    for e in range(len(headings)):
        headNum = [1,2,3,4,5]
        tree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    tree.bind("<Double-1>", on_tree_double_click)


    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)


    tree.grid(row=0, column=0, sticky="nsew")


    scrollbar.grid(row=0, column=1, sticky="ns")


    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

    textbox_frame = tk.Frame(root, background="#bc6c25")
    textbox_frame.pack(pady=10)

    labels = ["Código de Turno", "Fecha", "Hora", "Paciente", "Medico"]

    for i in range(len(labels)):
        label = tk.Label(textbox_frame, text=f"{labels[i]}", background="#bc6c25", foreground="#fefefe", font=roboto)
        label.grid(row=1, column=i, padx=5, pady=5)

    def saltoEntry(event, sigEntry):
        sigEntry.focus_set()

    codVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    codVar.grid(row=2, column=0, padx=2, pady=5)

    fechaVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    fechaVar.grid(row=2, column=1, padx=2, pady=5)

    horaVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    horaVar.grid(row=2, column=2, padx=2, pady=5)

    pacienteVar = ttk.Combobox(textbox_frame, width=20, font=roboto)
    pacienteVar.grid(row=2, column=3, padx=2, pady=5)

    sqlPac = "SELECT dni FROM pacientes"

    cursor = conexion.cursor()
    cursor.execute(sqlPac)
    resultados = cursor.fetchall()
    cursor.close()

    for i in resultados:
        pacienteVar["values"] = (*pacienteVar["values"], i)


    medicoVar = ttk.Combobox(textbox_frame, width=20, font=roboto)
    medicoVar.grid(row=2, column=4, padx=2, pady=5)

    sqlMed = "SELECT dni FROM medicos"

    cursor = conexion.cursor()
    cursor.execute(sqlMed)
    resultados = cursor.fetchall()
    cursor.close()
    
    for i in resultados:
        medicoVar["values"] = (*medicoVar["values"], i)

    codVar.bind('<Return>', lambda event, entry=fechaVar: saltoEntry(event, entry))
    fechaVar.bind('<Return>', lambda event, entry=horaVar: saltoEntry(event, entry))
    horaVar.bind('<Return>', lambda event, entry=pacienteVar: saltoEntry(event, entry))
    pacienteVar.bind('<Return>', lambda event, entry=medicoVar: saltoEntry(event, entry))


    btn_frame = tk.Frame(root, background="#bc6c25")
    btn_frame.pack(pady=10, padx=30)

    btn_modificar = tk.Button(btn_frame, text="Modificar Registro", command=modificarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_eliminar = tk.Button(btn_frame, text="Eliminar Registro", command=eliminarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_volcar = tk.Button(btn_frame, text="Buscar sin Filtros", command=volcarTodo, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)

    btn_modificar.pack(side="left", padx=10, pady=10)
    btn_eliminar.pack(side="left", padx=10, pady=10)
    btn_volcar.pack(side="left", padx=10, pady=10)

    root.mainloop()

def ventanaAsignarT():

    root = tk.Tk()
    root.title("Asignar Turno")
    root.geometry("1108x640")
    root.iconbitmap("resources/imagenn.ico")
    root.configure(bg="#bc6c25")
    root.resizable(False, False)

    centrar_ventana(root)

    def abrirInicio():
        root.withdraw()
        ventanaInicio()

    def abrirPacientes():
        root.withdraw()
        ventanaPacientes()

    def abrirMedicos():
        root.withdraw()
        ventanaMedicos()

    def abrirHistoriasClinicas():
        root.withdraw()
        ventanaHistoriasClinicas()

    def abrirTurnos():
        root.withdraw()
        ventanaTurnos()

    def abrirAsignarT():
        root.withdraw()
        ventanaAsignarT()

    def abrirInternaciones():
        root.withdraw()
        ventanaInternaciones()

    def abrirAsignarI():
        root.withdraw()
        ventanaAsignarI()

    def abrirEspecialidades():
        root.withdraw()
        ventanaEspecialidades()

    def abrirPatologias():
        root.withdraw()
        ventanaPatologias()

    def abrirUsuarios():
        root.withdraw()
        ventanaUsuarios()

    navFrame = tk.Frame(root)
    navFrame.pack()

    variables = ["btnInicio", "btnPacientes", "btnMedicos", "btnHistoriasClinicas", "Asignar Turnos", "btnTurnos", "btnInternaciones", "Asignar Internacion", "btnEspecialidades", "btnPatologias", "btnUsuarios"]

    textos = ["Inicio", "Pacientes", "Medicos", "Historias Clinicas", "Turnos", "Asignar \n Turnos", "Internaciones", "Asignar \n Internacion", "Especialidades", "Patologias", "Usuarios"]

    comandos = [abrirInicio, abrirPacientes, abrirMedicos, abrirHistoriasClinicas, abrirTurnos, abrirAsignarT, abrirInternaciones, abrirAsignarI, abrirEspecialidades, abrirPatologias, abrirUsuarios]

    roboto = ("Roboto", 8, "bold")

    for i in range(len(variables)):
        button = variables[i]
        button = tk.Button(navFrame, text=f"{textos[i]}", width=13, height=2, command=comandos[i], background="#6c757d", foreground="#fefefe", font=roboto)
        button.pack(side="left")

    frameGeneral3 = tk.Frame(root, background="#bc6c25")
    frameGeneral3.pack(pady=10, padx=10)
    frameGeneral1 = tk.Frame(root, background="#bc6c25")
    frameGeneral1.pack(padx=10)
    frameGeneral2 = tk.Frame(root, background="#bc6c25")
    frameGeneral2.pack(pady=10, padx=10)

    #--------------------------------------TREEVIEW DE LABELS#--------------------------------------
    
    def patientSearch():
        pacienteValue = askstring("Ingresar Datos", "Por favor, ingrese un numero de dni sin puntos ni espacios.",parent=root)
        valores = (pacienteValue,)
        consulta = "SELECT cod_paciente, Nombre, Papellido, dni FROM pacientes WHERE dni = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, valores)
        registros = cursor.fetchall()
        cursor.close()

        pacienteLabel.config(text = "")
        medicoLabel.config(text = "")
        fechaLabel.config(text = "")
        horaLabel.config(text = "")
        for item in pacienteTree.get_children():
            pacienteTree.delete(item)
        for item in medicoTree.get_children():
            medicoTree.delete(item)
        for item in especialidadTree.get_children():
            especialidadTree.delete(item)
        for item in añoTree.get_children():
            añoTree.delete(item)
        for item in mesTree.get_children():
            mesTree.delete(item)
        for item in diaTree.get_children():
            diaTree.delete(item)
        for item in horaTree.get_children():
            horaTree.delete(item)

        for registro in registros:
            pacienteTree.insert("", "end", values=registro)

    pacienteSearchButton = tk.Button(frameGeneral3, width=20, height=1, command=patientSearch, text="Buscar Paciente", background="#6c757d", foreground="#fefefe", font=roboto)
    pacienteSearchButton.grid(row=0, column=0, rowspan=2, columnspan=2, padx=5, pady=5)

    label1 = tk.Label(frameGeneral3, text="Paciente", background="#bc6c25", foreground="#fefefe", font=roboto)
    label1.grid(row=0, column=3, padx=30, pady=2)
    pacienteLabel = tk.Label(frameGeneral3, height=1, background="#bc6c25", foreground="#fefefe", font=roboto)
    pacienteLabel.grid(row=1, column=3, padx=30, pady=2)

    label2 = tk.Label(frameGeneral3, text="Medico", background="#bc6c25", foreground="#fefefe", font=roboto)
    label2.grid(row=0, column=4, padx=30, pady=2)
    medicoLabel = tk.Label(frameGeneral3, height=1, background="#bc6c25", foreground="#fefefe", font=roboto)
    medicoLabel.grid(row=1, column=4, padx=30, pady=2)

    label3 = tk.Label(frameGeneral3, text="Fecha", background="#bc6c25", foreground="#fefefe", font=roboto)
    label3.grid(row=0, column=5, padx=30, pady=2)
    fechaLabel = tk.Label(frameGeneral3, height=1, background="#bc6c25", foreground="#fefefe", font=roboto)
    fechaLabel.grid(row=1, column=5, padx=5, pady=2)

    label4 = tk.Label(frameGeneral3, text="Hora", background="#bc6c25", foreground="#fefefe", font=roboto)
    label4.grid(row=0, column=6, padx=30, pady=2)
    horaLabel = tk.Label(frameGeneral3, height=1, background="#bc6c25", foreground="#fefefe", font=roboto)
    horaLabel.grid(row=1, column=6, padx=30, pady=2)
    

    #--------------------------------------TREEVIEW DE PACIENTE#--------------------------------------
    
    def on_tree_double_click_paciente(event):
        item_seleccionado = pacienteTree.focus()

        if item_seleccionado:
            # Obtiene los valores de las dos primeras columnas del registro
            valores = pacienteTree.item(item_seleccionado, "values")
            
            if valores:
                # Muestra los valores en el Label
                pacienteLabel.config(text=valores[0])  # Actualiza el contenido de pacienteLabel
            
        for a in pacienteTree.get_children():
            pacienteTree.delete(a)

        consulta = "SELECT * FROM especialidades"
        cursor = conexion.cursor()
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()

        for a in especialidadTree.get_children():
            especialidadTree.delete(a)

        for registro in registros:
            especialidadTree.insert("", "end", values=registro)



    framePaciente = tk.Frame(frameGeneral1, background="#bc6c25")
    framePaciente.pack(side="left", pady=10, padx=10)

    pacienteTree = ttk.Treeview(framePaciente, columns=("Cod Paciente", "Nombre", "Apellido"))
    pacienteTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,4):
        pacienteTree.column(f"#{c}", width=100, anchor="center")
        pacienteTree.column("#0", width=0, anchor="center")

    headings = ["Cod Paciente", "Nombre", "Apellido"]

    for e in range(len(headings)):
        headNum = [1,2,3]
        pacienteTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")

    pacienteTree.bind("<Double-1>", lambda event: on_tree_double_click_paciente(event))

    scrollbar = ttk.Scrollbar(framePaciente, orient="vertical", command=pacienteTree.yview)
    scrollbar.grid(row=1, column=2, sticky="ns")

    pacienteTree.configure(yscroll=scrollbar.set)

    framePaciente.grid_rowconfigure(0, weight=1)
    framePaciente.grid_columnconfigure(0, weight=1)

    #--------------------------------------TREEVIEW DE ESPECIALIDAD#--------------------------------------


    def on_tree_double_click_especialidad(event):
        item_seleccionado = especialidadTree.focus()

        if item_seleccionado:
            # Obtiene los valores de las dos primeras columnas del registro
            valores = especialidadTree.item(item_seleccionado, "values")
            
            if valores:
                especialidad = valores[0]
            
        for a in especialidadTree.get_children():
            especialidadTree.delete(a)

        valores = (especialidad,) 
        consulta = "SELECT cod_medico, Nombre, Mapellido FROM medicos WHERE especialidad = %s"
        cursor = conexion.cursor()
        cursor.execute(consulta, valores)
        registros = cursor.fetchall()
        cursor.close()
        for a in medicoTree.get_children():
            medicoTree.delete(a)

        for registro in registros:
            medicoTree.insert("", "end", values=registro)

    frameEspecialidad = tk.Frame(frameGeneral1, background="#bc6c25")
    frameEspecialidad.pack(side="left", pady=10, padx=10)

    especialidadTree = ttk.Treeview(frameEspecialidad, columns=("Cod Especialidad", "Especialidad"))
    especialidadTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,3):
        especialidadTree.column(f"#{c}", width=165, anchor="center")
        especialidadTree.column("#0", width=0, anchor="center")

    headings = ["Cod Especialidad", "Especialidad"]

    for e in range(len(headings)):
        headNum = [1,2]
        especialidadTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    especialidadTree.bind("<Double-1>", lambda event: on_tree_double_click_especialidad(event))

    scrollbar = ttk.Scrollbar(frameEspecialidad, orient="vertical", command=especialidadTree.yview)
    scrollbar.grid(row=1, column=2, sticky="ns")
    
    especialidadTree.configure(yscroll=scrollbar.set)

    frameEspecialidad.grid_rowconfigure(0, weight=1)
    frameEspecialidad.grid_columnconfigure(0, weight=1)

    #--------------------------------------TREEVIEW DE MEDICO#--------------------------------------

    def on_tree_double_click_medico(event):
        item_seleccionado = medicoTree.focus()

        if item_seleccionado:
            valores = medicoTree.item(item_seleccionado, "values")
            
            if valores:
                medicoLabel.config(text=valores[0])  # Actualiza el contenido de pacienteLabel
            
        for a in medicoTree.get_children():
            medicoTree.delete(a)

        for a in añoTree.get_children():
            añoTree.delete(a)

        for i in range(2023, 2051):
            añoTree.insert("", "end", values=(i,))


    frameMedico = tk.Frame(frameGeneral1, background="#bc6c25")
    frameMedico.pack(side="left", pady=10, padx=10)

    medicoTree = ttk.Treeview(frameMedico, columns=("Cod Medico", "Nombre", "Apellido"))
    medicoTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,4):
        medicoTree.column(f"#{c}", width=100, anchor="center")
        medicoTree.column("#0", width=0, anchor="center")

    headings = ["Cod Medico", "Nombre", "Apellido"]

    for e in range(len(headings)):
        headNum = [1,2,3]
        medicoTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    medicoTree.bind("<Double-1>", lambda event: on_tree_double_click_medico(event))

    scrollbar = ttk.Scrollbar(frameMedico, orient="vertical", command=medicoTree.yview)
    scrollbar.grid(row=1, column=2, sticky="ns")
    
    medicoTree.configure(yscroll=scrollbar.set)

    frameMedico.grid_rowconfigure(0, weight=1)
    frameMedico.grid_columnconfigure(0, weight=1)

    #--------------------------------------TREEVIEW DE FECHA#--------------------------------------

    #--------------------------------------TREEVIEW DE AÑO#--------------------------------------

    año = tk.StringVar()
    mes = tk.StringVar()
    dia = tk.StringVar()
    hora = tk.StringVar()

    def on_tree_double_click_año(event):
        global año
        item_seleccionado = añoTree.focus()

        if item_seleccionado:
            valores = añoTree.item(item_seleccionado, "values")
            
            if valores:
                año = valores[0]
                fechaLabel.config(text=f"00/00/{año}")
            
        for a in añoTree.get_children():
            añoTree.delete(a)

        for item in mesTree.get_children():
            mesTree.delete(item)

        for item in diaTree.get_children():
            diaTree.delete(item)

        for item in horaTree.get_children():
            horaTree.delete(item)

        horaLabel.config(text = "")

        for i in range(2023, 2051):
            añoTree.insert("", "end", values=(i,))

        for a in mesTree.get_children():
            mesTree.delete(a)

        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

        for i in range(len(months)):
            mesTree.insert("", "end", values=months[i])



    frameAño = tk.Frame(frameGeneral2, background="#bc6c25")
    frameAño.pack(side="left", pady=10, padx=10)

    añoTree = ttk.Treeview(frameAño, columns=("Año"))
    añoTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,2):
        añoTree.column(f"#{c}", width=120, anchor="center")
        añoTree.column("#0", width=0, anchor="center")

    headings = ["Año"]  

    for e in range(len(headings)):
        headNum = [1]
        añoTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    añoTree.bind("<Double-1>", lambda event: on_tree_double_click_año(event))

    scrollbarAño = ttk.Scrollbar(frameAño, orient="vertical", command=añoTree.yview)
    scrollbarAño.grid(row=1, column=2, sticky="ns")
    
    añoTree.configure(yscroll=scrollbarAño.set)

    frameAño.grid_rowconfigure(0, weight=1)
    frameAño.grid_columnconfigure(0, weight=1)

    #--------------------------------------TREEVIEW DE MES#--------------------------------------

    def on_tree_double_click_mes(event):
        global año
        global mes
        item_seleccionado = mesTree.focus()

        for item in diaTree.get_children():
            diaTree.delete(item)
            
        for item in horaTree.get_children():
            horaTree.delete(item)

        horaLabel.config(text = "")

        if item_seleccionado:
            valores = mesTree.item(item_seleccionado, "values")

            if valores:



                mes = valores[0]
                if mes == "Enero":
                    mes = "01"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Febrero":
                    mes = "02"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 30):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Marzo":
                    mes = "03"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Abril":
                    mes = "04"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 31):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Mayo":
                    mes = "05"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Junio":
                    mes = "06"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 31):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Julio":
                    mes = "07"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Agosto":
                    mes = "08"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Septiembre":
                    mes = "09"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 31):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Octubre":
                    mes = "10"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Noviembre":
                    mes = "11"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 31):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Diciembre":
                    mes = "12"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



        for a in mesTree.get_children():
            mesTree.delete(a)



        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

        for i in range(len(months)):
            mesTree.insert("", "end", values=months[i])


    frameMes = tk.Frame(frameGeneral2)
    frameMes.pack(side="left", pady=10, padx=10)

    mesTree = ttk.Treeview(frameMes, columns=("Mes"))
    mesTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,2):
        mesTree.column(f"#{c}", width=120, anchor="center")
        mesTree.column("#0", width=0, anchor="center")

    headings = ["Mes"]  

    for e in range(len(headings)):
        headNum = [1]
        mesTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    mesTree.bind("<Double-1>", lambda event: on_tree_double_click_mes(event))

    scrollbarMes = ttk.Scrollbar(frameMes, orient="vertical", command=mesTree.yview)
    scrollbarMes.grid(row=1, column=2, sticky="ns")
    
    mesTree.configure(yscroll=scrollbarMes.set)

    frameMes.grid_rowconfigure(0, weight=1)
    frameMes.grid_columnconfigure(0, weight=1)

    #--------------------------------------TREEVIEW DE DIA#--------------------------------------

    def on_tree_double_click_dia(event):
        global año
        global mes
        global dia
        item_seleccionado = diaTree.focus()

        if item_seleccionado:
            valores = diaTree.item(item_seleccionado, "values")
            
            if valores:
                dia = valores[0]
                fechaLabel.config(text=f"{dia}/{mes}/{año}")
            
        for a in añoTree.get_children():
            añoTree.delete(a)

        for i in range(2023, 2051):
            añoTree.insert("", "end", values=(i,))

        for a in mesTree.get_children():
            mesTree.delete(a)

        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

        for i in range(len(months)):
            mesTree.insert("", "end", values=months[i])

        # Eliminar todos los elementos previos en el Treeview
        for item in horaTree.get_children():
            horaTree.delete(item)

        horaLabel.config(text = "")
        
        horas = ["08:00", "08:30", "09:00", "09:30", "10:00", "10:30",
                "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
                "14:00", "14:30", "15:00", "15:30", "16:00", "16:30"]

        medicoCod = medicoLabel.cget("text")
        turnoFec = fechaLabel.cget("text")

        for i in range(len(horas)):
            sql = f"SELECT fecha, hora, medico FROM turnos WHERE medico = '{medicoCod}' AND fecha = '{turnoFec}' AND hora = '{horas[i]}'"
            
            cursor = conexion.cursor() 
            cursor.execute(sql)
            resultado =cursor.fetchall()
            cursor.close()

            if resultado:
                color = "red"  # Rojo para coincidencias
                color1 = "white"
                horaTree.insert("", "end", values=horas[i], tags=(color,color1,))

            else:
                color = "green"  # Verde para no coincidencias
                color1 = "white"
                horaTree.insert("", "end", values=horas[i], tags=(color,color1,))


        horaTree.tag_configure("red", background="red")
        horaTree.tag_configure("green", background="green")
        horaTree.tag_configure("white", foreground="white")

    frameDia = tk.Frame(frameGeneral2)
    frameDia.pack(side="left", pady=10, padx=10)

    diaTree = ttk.Treeview(frameDia, columns=("Dia"))
    diaTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,2):
        diaTree.column(f"#{c}", width=120, anchor="center")
        diaTree.column("#0", width=0, anchor="center")

    headings = ["Dia"]  

    for e in range(len(headings)):
        headNum = [1]
        diaTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    diaTree.bind("<Double-1>", lambda event: on_tree_double_click_dia(event))

    scrollbarDia = ttk.Scrollbar(frameDia, orient="vertical", command=diaTree.yview)
    scrollbarDia.grid(row=1, column=2, sticky="ns")
    
    diaTree.configure(yscroll=scrollbarDia.set)

    frameDia.grid_rowconfigure(0, weight=1)
    frameDia.grid_columnconfigure(0, weight=1)


    #--------------------------------------TREEVIEW DE HORA#--------------------------------------

    def on_tree_double_click_hora(event):
        global hora
        item_seleccionado = horaTree.focus()

        if item_seleccionado:
            valores = horaTree.item(item_seleccionado, "values")
            
            if valores:
                hora = valores[0]
                horaLabel.config(text=f"{hora}")

    frameHora = tk.Frame(frameGeneral2)
    frameHora.pack(side="left", pady=10, padx=10)

    horaTree = ttk.Treeview(frameHora, columns=("Hora"))
    horaTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,2):
        horaTree.column(f"#{c}", width=120, anchor="center")
        horaTree.column("#0", width=0, anchor="center")

    headings = ["Hora"]  

    for e in range(len(headings)):
        headNum = [1]
        horaTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    horaTree.bind("<Double-1>", lambda event: on_tree_double_click_hora(event))

    scrollbarHora = ttk.Scrollbar(frameHora, orient="vertical", command=horaTree.yview)
    scrollbarHora.grid(row=1, column=2, sticky="ns")
    
    horaTree.configure(yscroll=scrollbarHora.set)


    frameHora.grid_rowconfigure(0, weight=1)
    frameHora.grid_columnconfigure(0, weight=1)

    def cargar_turno():
        pacienteCode = pacienteLabel.cget("text")
        medicoCode = medicoLabel.cget("text")
        fecha = fechaLabel.cget("text")
        hora = horaLabel.cget("text")

        if pacienteCode == "" or medicoCode == "" or fecha == "" or hora == "":
            messagebox.showerror("Campos vacios", "Uno o mas campos se encuentran vacios.")
        else:
            try:
                sql1 = f"SELECT * FROM turnos WHERE paciente = '{pacienteCode}' AND medico = '{medicoCode}' AND fecha = '{fecha}' AND hora = '{hora}'"
                cursor = conexion.cursor()
                cursor.execute(sql1)
                resultados = cursor.fetchall()
                cursor.close()
                if resultados:
                    messagebox.showinfo("Turno ocupado", "El turno seleccionado se encuentra ocupado.")
                else:
                    valores = (fecha, hora, pacienteCode, medicoCode,)
                    sql2 = "INSERT INTO turnos (fecha, hora, paciente, medico) VALUES (%s,%s,%s,%s)"
                    cursor = conexion.cursor()                
                    cursor.execute(sql2, valores)
                    conexion.commit()
                    cursor.close()
                    messagebox.showinfo("Éxito", "El turno ha sido cargado exitosamente.")
                    pacienteLabel.config(text = "")
                    medicoLabel.config(text = "")
                    fechaLabel.config(text = "")
                    horaLabel.config(text = "")
                    for item in pacienteTree.get_children():
                        pacienteTree.delete(item)
                    for item in medicoTree.get_children():
                        medicoTree.delete(item)
                    for item in especialidadTree.get_children():
                        especialidadTree.delete(item)
                    for item in añoTree.get_children():
                        añoTree.delete(item)
                    for item in mesTree.get_children():
                        mesTree.delete(item)
                    for item in diaTree.get_children():
                        diaTree.delete(item)
                    for item in horaTree.get_children():
                        horaTree.delete(item)


            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    executeButton = tk.Button(frameGeneral3, text="Asignar Turno", width=20, height=1, command=cargar_turno, background="#6c757d", foreground="#fefefe", font=roboto)
    executeButton.grid(row=0, column=7, rowspan=2, columnspan=2, padx=5, pady=2)

    root.mainloop()

def ventanaInternaciones():

    root = tk.Tk()
    root.title("Internaciones")
    root.geometry("1108x560")
    root.iconbitmap("resources/imagenn.ico")
    root.configure(bg="#bc6c25")
    root.resizable(False, False)

    centrar_ventana(root)

    def abrirInicio():
        root.withdraw()
        ventanaInicio()

    def abrirPacientes():
        root.withdraw()
        ventanaPacientes()

    def abrirMedicos():
        root.withdraw()
        ventanaMedicos()

    def abrirHistoriasClinicas():
        root.withdraw()
        ventanaHistoriasClinicas()

    def abrirTurnos():
        root.withdraw()
        ventanaTurnos()

    def abrirAsignarT():
        root.withdraw()
        ventanaAsignarT()

    def abrirInternaciones():
        root.withdraw()
        ventanaInternaciones()

    def abrirAsignarI():
        root.withdraw()
        ventanaAsignarI()

    def abrirEspecialidades():
        root.withdraw()
        ventanaEspecialidades()

    def abrirPatologias():
        root.withdraw()
        ventanaPatologias()

    def abrirUsuarios():
        root.withdraw()
        ventanaUsuarios()

    navFrame = tk.Frame(root)
    navFrame.pack()

    variables = ["btnInicio", "btnPacientes", "btnMedicos", "btnHistoriasClinicas", "Asignar Turnos", "btnTurnos", "btnInternaciones", "Asignar Internacion", "btnEspecialidades", "btnPatologias", "btnUsuarios"]

    textos = ["Inicio", "Pacientes", "Medicos", "Historias Clinicas", "Turnos", "Asignar \n Turnos", "Internaciones", "Asignar \n Internacion", "Especialidades", "Patologias", "Usuarios"]

    comandos = [abrirInicio, abrirPacientes, abrirMedicos, abrirHistoriasClinicas, abrirTurnos, abrirAsignarT, abrirInternaciones, abrirAsignarI, abrirEspecialidades, abrirPatologias, abrirUsuarios]

    roboto = ("Roboto", 8, "bold")

    for i in range(len(variables)):
        button = variables[i]
        button = tk.Button(navFrame, text=f"{textos[i]}", width=13, height=2, command=comandos[i], background="#6c757d", foreground="#fefefe", font=roboto)
        button.pack(side="left")

    def actualizar_treeview():

        cursor = conexion.cursor()
        if tree.get_children():
            tree.delete(*tree.get_children())
        select_query = "SELECT * FROM internaciones" 
        cursor.execute(select_query)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        cursor.close()

    def modificarRegistro():
        codValue = codVar.get()
        fechaValue = fechaVar.get()
        horaValue = horaVar.get()
        pacienteValue = pacienteVar.get()
        medicoValue = medicoVar.get()
        patoValue = patologiaVar.get()
        pisoValue = pisoVar.get()
        numHabValue = numHabVar.get()
        numCamaValue = numCamVar.get()
        altaValue = altaVar.get()
       

        if codValue == "" or fechaValue == "" or horaValue == "" or pacienteValue == "" or medicoValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            valor = (codValue,)
            consulta2 = "SELECT * FROM internaciones WHERE cod_internacion = %s"
            cursor = conexion.cursor()
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchone()
            cursor.close()

            if resultado:
                    cursor = conexion.cursor()
                    valor1 = (pacienteValue,)
                    consulta1 = "SELECT cod_paciente FROM pacientes WHERE dni = %s"
                    cursor.execute(consulta1, valor1)
                    resultado1 = cursor.fetchone()
                    cursor.close()
                    cursor = conexion.cursor()
                    consulta5 = "SELECT * FROM pacientes WHERE cod_paciente = %s"
                    cursor.execute(consulta5, valor1)
                    resultado2 = cursor.fetchone()
                    cursor.close()
                    cursor = conexion.cursor()
                    valor2 = (medicoValue,)
                    consulta3 = "SELECT cod_medico FROM medicos WHERE dni = %s"
                    cursor.execute(consulta3, valor2)
                    resultado3 = cursor.fetchone()
                    cursor.close()
                    cursor = conexion.cursor()
                    consulta4 = "SELECT * FROM medicos WHERE cod_medico = %s"
                    cursor.execute(consulta4, valor2)
                    resultado4 = cursor.fetchone()
                    cursor.close()
                    cursor = conexion.cursor()
                    valor3 = (patoValue,)
                    consulta6 = "SELECT cod_patologia FROM patologias WHERE Patologia = %s"
                    cursor.execute(consulta6, valor3)
                    resultado5 = cursor.fetchone()
                    cursor.close()
                    cursor = conexion.cursor()
                    consulta7 = "SELECT * FROM patologias WHERE cod_patologia = %s"
                    cursor.execute(consulta7, valor3)
                    resultado6 = cursor.fetchone()
                    cursor.close()

                    paciente = None
                    medico = None
                    patologia = None

                    if resultado1 or resultado2: 
                        if resultado1:
                            paciente = resultado1
                        elif resultado2:
                            paciente = resultado2

                    if resultado3 or resultado4: 
                        if resultado3:
                            medico = resultado3
                        elif resultado4:
                            medico = resultado4

                    if resultado5 or resultado6: 
                        if resultado5:
                            patologia = resultado5
                        elif resultado6:
                            patologia = resultado6

                    if paciente and medico and patologia:
                        confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea modificar el registro?")
                        if confirmacion:
                            update_query = f"UPDATE internaciones SET fecha = '{fechaValue}', hora = '{horaValue}', paciente = '{paciente[0]}', medico = '{medico[0]}', patologia = '{patologia[0]}', piso = '{pisoValue}', num_hab = '{numHabValue}', num_cama = '{numCamaValue}', alta = '{altaValue}' WHERE cod_internacion = '{codValue}'"        
                            cursor = conexion.cursor()
                            cursor.execute(update_query)
                            conexion.commit()
                            cursor.close()
                            messagebox.showinfo("Exito", "El registro ha sido modificado exitosamente.")
                            actualizar_treeview()

                            textos = [codVar, fechaVar, horaVar, pacienteVar, medicoVar, patologiaVar, pisoVar, numHabVar, numCamVar, altaVar]

                            for i in range(len(textos)):
                                nuevo_valor = "" 
                                textos[i].delete(0, tk.END)
                                textos[i].insert(0, nuevo_valor)
                        else:
                            messagebox.showinfo("Cancelacion", "El registro no sera modificado.")
                    else:
                        messagebox.showerror("Error", "El codigo de paciente, medico o patologia ingresado no existe.")
            else:
                messagebox.showerror("Error", "El codigo de internacion ingresado no existe.")

    def eliminarRegistro():
        id_to_delete = codVar.get()
        
        if id_to_delete == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else: 
            valor = (id_to_delete,)
            consulta2 = "SELECT * FROM internaciones WHERE cod_internacion = %s"
            cursor = conexion.cursor()
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchall()
            cursor.close()

            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar el registro?")
                if confirmacion:
                    valores = (id_to_delete,)
                    delete_query = "DELETE FROM internaciones WHERE cod_internacion = %s"
                    cursor = conexion.cursor()
                    cursor.execute(delete_query, valores)
                    conexion.commit()
                    cursor.close()
                    messagebox.showinfo("Exito", "El registro ha sido eliminado exitosamente.")
                    actualizar_treeview()

                    textos = [codVar, fechaVar, horaVar, pacienteVar, medicoVar, patologiaVar, pisoVar, numHabVar, numCamVar, altaVar]

                    for i in range(len(textos)):
                        nuevo_valor = "" 
                        textos[i].delete(0, tk.END)
                        textos[i].insert(0, nuevo_valor)
                    
                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera eliminado.")
            else:
                messagebox.showerror("Error", "El codigo de internacion ingresado no existe.")


    def volcarTodo():
        consulta = "SELECT * FROM internaciones"
        cursor = conexion.cursor()
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()
        for a in tree.get_children():
            tree.delete(a)
            

        for registro in registros:
            tree.insert("", "end", values=registro)

    def on_tree_double_click(event):
        item = tree.selection()[0]
        values = tree.item(item, "values")

        textboxx = [codVar, fechaVar, horaVar, pacienteVar, medicoVar, patologiaVar, pisoVar, numHabVar, numCamVar, altaVar]

        for index, value in enumerate(values):
            textboxx[index].delete(0, tk.END)
            textboxx[index].insert(0, value)


    def columnSearch(event):
        comboValue = comboSearch.get()
        searchValue = search.get()

        consulta = None

        if comboValue == "":
            messagebox.showinfo("Campo Vacio", "El selector se encuentra vacio.")
        elif comboValue == "Fecha":
            consulta = "SELECT * FROM internaciones WHERE fecha LIKE %s"
        elif comboValue == "Hora":
            consulta = "SELECT * FROM internaciones WHERE hora LIKE %s"
        elif comboValue == "Paciente (Dni)":
            consulta = "SELECT cod_paciente FROM pacientes WHERE dni LIKE %s"
        elif comboValue == "Medico (Dni)":
            consulta = "SELECT cod_medico FROM medicos WHERE dni LIKE %s"
        elif comboValue == "Patologia":
            consulta = "SELECT cod_patologia FROM patologias WHERE Patologia LIKE %s"
        elif comboValue == "Alta":
            consulta = "SELECT * FROM internaciones WHERE alta LIKE %s"

        if comboValue == "Fecha" or comboValue == "Hora" or comboValue == "Alta":
            cursor = conexion.cursor()
            cursor.execute(consulta, ("%" + searchValue + "%",))
            registros = cursor.fetchall()
            cursor.close()

        elif comboValue == "Paciente (Dni)":
            cursor = conexion.cursor()
            cursor.execute(consulta, ("%" + searchValue + "%",))
            registros = cursor.fetchall()
            cursor.nextset()
            cursor.close()
            if len(registros) > 0:
                cursor = conexion.cursor()
                valor = registros[0]
                consulta1 = "SELECT * FROM internaciones WHERE paciente LIKE %s"
                cursor.execute(consulta1, valor)
                registros = cursor.fetchall()
                cursor.nextset()
                cursor.close()
            else:
                messagebox.showinfo("Sin registros", "No se han encontrado internaciones asociadas a ese paciente.")

        elif comboValue == "Medico (Dni)":
            cursor = conexion.cursor()
            cursor.execute(consulta, ("%" + searchValue + "%",))
            registros = cursor.fetchall()
            cursor.nextset()
            cursor.close()
            if len(registros) > 0:
                cursor = conexion.cursor()
                valor = registros[0]
                consulta1 = "SELECT * FROM internaciones WHERE medico LIKE %s"
                cursor.execute(consulta1, valor)
                registros = cursor.fetchall()
                cursor.nextset()
                cursor.close()
            else:
                messagebox.showinfo("Sin registros", "No se han encontrado internaciones asociadas a ese medico.")

        elif comboValue == "Patologia":
            cursor = conexion.cursor()
            cursor.execute(consulta, ("%" + searchValue + "%",))
            registros = cursor.fetchall()
            cursor.nextset()
            cursor.close()
            if len(registros) > 0:
                cursor = conexion.cursor()
                valor = registros[0]
                consulta1 = "SELECT * FROM internaciones WHERE patologia LIKE %s"
                cursor.execute(consulta1, valor)
                registros = cursor.fetchall()
                cursor.nextset()
                cursor.close()
            else:
                messagebox.showinfo("Sin registros", "No se han encontrado internaciones asociadas a esa patologia.")

        elif comboValue != "Fecha" or comboValue != "Hora" or comboValue != "Paciente (Dni)" or comboValue != "Medico (Dni)" or comboValue != "Patologia" or comboValue != "Alta":
            messagebox.showinfo("Columna no válida", "La columna seleccionada no es válida.")



        for a in tree.get_children():
            tree.delete(a)   

        if searchValue == "":   
            for a in tree.get_children():
                tree.delete(a)
        else:
            for registro in registros:
                tree.insert("", "end", values=registro)


    searchFrame = tk.Frame(root, background="#bc6c25")
    searchFrame.pack(pady=10)

    comboSearch = ttk.Combobox(searchFrame, values=["Fecha", "Hora", "Paciente (Dni)", "Medico (Dni)", "Patologia", "Alta"], width=30)
    comboSearch.pack(side="left", padx=10)

    search = tk.Entry(searchFrame, width=30, font=roboto)
    search.pack(side="left", padx=10)

    search.bind("<KeyRelease>", columnSearch)

    tree_frame = tk.Frame(root, background="#bc6c25")
    tree_frame.pack(pady=10)

    tree = ttk.Treeview(tree_frame, columns=("Cod de Internacion", "Fecha", "Hora", "Paciente", "Medico", "Patologia", "Piso", "Num Hab", "Num Cama", "Alta"))

    for c in range(1,11):
        tree.column(f"#{c}", width=100, anchor="center")
        tree.column("#0", width=0, anchor="center")

    headings = ["Cod de Internacion", "Fecha", "Hora", "Paciente", "Medico", "Patologia", "Piso", "Num Hab", "Num Cama", "Alta"]

    for e in range(len(headings)):
        headNum = [1,2,3,4,5,6,7,8,9,10]
        tree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    tree.bind("<Double-1>", on_tree_double_click)


    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)


    tree.grid(row=0, column=0, sticky="nsew")


    scrollbar.grid(row=0, column=1, sticky="ns")


    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

    textbox_frame = tk.Frame(root, background="#bc6c25")
    textbox_frame.pack(pady=10)

    labels1 = ["Código de Internacion", "Fecha", "Hora", "Paciente", "Medico"]

    for i in range(len(labels1)):
        label = tk.Label(textbox_frame, text=f"{labels1[i]}", background="#bc6c25", foreground="#fefefe", font=roboto)
        label.grid(row=1, column=i, padx=5, pady=5)

    labels2 = ["Patologia", "Piso", "Num Habitacion", "Num Cama", "Alta"]

    for i in range(len(labels2)):
        label = tk.Label(textbox_frame, text=f"{labels2[i]}", background="#bc6c25", foreground="#fefefe", font=roboto)
        label.grid(row=3, column=i, padx=5, pady=5)


    def saltoEntry(event, sigEntry):
        sigEntry.focus_set()

    codVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    codVar.grid(row=2, column=0, padx=10, pady=5)

    fechaVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    fechaVar.grid(row=2, column=1, padx=10, pady=5)

    horaVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    horaVar.grid(row=2, column=2, padx=10, pady=5)

    pacienteVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    pacienteVar.grid(row=2, column=3, padx=10, pady=5)

    pacienteVar = ttk.Combobox(textbox_frame, width=20, font=roboto)
    pacienteVar.grid(row=2, column=3, padx=10, pady=5)

    sqlPac = "SELECT dni FROM pacientes"
    cursor = conexion.cursor()
    cursor.execute(sqlPac)
    resultados = cursor.fetchall()
    cursor.close()

    for i in resultados:
        pacienteVar["values"] = (*pacienteVar["values"], i)


    medicoVar = ttk.Combobox(textbox_frame, width=20, font=roboto)
    medicoVar.grid(row=2, column=4, padx=10, pady=5)

    sqlMed = "SELECT dni FROM medicos"
    cursor = conexion.cursor()
    cursor.execute(sqlMed)
    resultados = cursor.fetchall()
    cursor.close()

    for i in resultados:
        medicoVar["values"] = (*medicoVar["values"], i)

    patologiaVar = ttk.Combobox(textbox_frame, width=20, font=roboto)
    patologiaVar.grid(row=4, column=0, padx=10, pady=5)

    sqlPat = "SELECT Patologia FROM patologias"
    cursor = conexion.cursor()
    cursor.execute(sqlPat)
    resultados = cursor.fetchall()
    cursor.close()

    for i in resultados:
        patologiaVar["values"] = (*patologiaVar["values"], i)

    pisoVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    pisoVar.grid(row=4, column=1, padx=10, pady=5)

    numHabVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    numHabVar.grid(row=4, column=2, padx=10, pady=5)

    numCamVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    numCamVar.grid(row=4, column=3, padx=10, pady=5)

    altaVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    altaVar.grid(row=4, column=4, padx=10, pady=5)

    codVar.bind('<Return>', lambda event, entry=fechaVar: saltoEntry(event, entry))
    fechaVar.bind('<Return>', lambda event, entry=horaVar: saltoEntry(event, entry))
    horaVar.bind('<Return>', lambda event, entry=pacienteVar: saltoEntry(event, entry))
    pacienteVar.bind('<Return>', lambda event, entry=medicoVar: saltoEntry(event, entry))
    medicoVar.bind('<Return>', lambda event, entry=patologiaVar: saltoEntry(event, entry))
    patologiaVar.bind('<Return>', lambda event, entry=pisoVar: saltoEntry(event, entry))
    pisoVar.bind('<Return>', lambda event, entry=numHabVar: saltoEntry(event, entry))
    numHabVar.bind('<Return>', lambda event, entry=numCamVar: saltoEntry(event, entry))
    numCamVar.bind('<Return>', lambda event, entry=altaVar: saltoEntry(event, entry))

    btn_frame = tk.Frame(root, background="#bc6c25")
    btn_frame.pack(pady=10, padx=30)

    btn_modificar = tk.Button(btn_frame, text="Modificar Registro", command=modificarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_eliminar = tk.Button(btn_frame, text="Eliminar Registro", command=eliminarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_volcar = tk.Button(btn_frame, text="Buscar sin Filtros", command=volcarTodo, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)

    btn_modificar.pack(side="left", padx=10, pady=10)
    btn_eliminar.pack(side="left", padx=10, pady=10)
    btn_volcar.pack(side="left", padx=10, pady=10)

    root.mainloop()


def ventanaAsignarI():

    root = tk.Tk()
    root.title("Asignar Internacion")
    root.geometry("1108x640")
    root.iconbitmap("resources/imagenn.ico")
    root.configure(bg="#bc6c25")
    root.resizable(False, False)

    centrar_ventana(root)

    def abrirInicio():
        root.withdraw()
        ventanaInicio()

    def abrirPacientes():
        root.withdraw()
        ventanaPacientes()

    def abrirMedicos():
        root.withdraw()
        ventanaMedicos()

    def abrirHistoriasClinicas():
        root.withdraw()
        ventanaHistoriasClinicas()

    def abrirTurnos():
        root.withdraw()
        ventanaTurnos()

    def abrirAsignarT():
        root.withdraw()
        ventanaAsignarT()

    def abrirInternaciones():
        root.withdraw()
        ventanaInternaciones()

    def abrirAsignarI():
        root.withdraw()
        ventanaAsignarI()

    def abrirEspecialidades():
        root.withdraw()
        ventanaEspecialidades()

    def abrirPatologias():
        root.withdraw()
        ventanaPatologias()

    def abrirUsuarios():
        root.withdraw()
        ventanaUsuarios()

    navFrame = tk.Frame(root)
    navFrame.pack()

    variables = ["btnInicio", "btnPacientes", "btnMedicos", "btnHistoriasClinicas", "Asignar Turnos", "btnTurnos", "btnInternaciones", "Asignar Internacion", "btnEspecialidades", "btnPatologias", "btnUsuarios"]

    textos = ["Inicio", "Pacientes", "Medicos", "Historias Clinicas", "Turnos", "Asignar \n Turnos", "Internaciones", "Asignar \n Internacion", "Especialidades", "Patologias", "Usuarios"]

    comandos = [abrirInicio, abrirPacientes, abrirMedicos, abrirHistoriasClinicas, abrirTurnos, abrirAsignarT, abrirInternaciones, abrirAsignarI, abrirEspecialidades, abrirPatologias, abrirUsuarios]

    roboto = ("Roboto", 8, "bold")

    for i in range(len(variables)):
        button = variables[i]
        button = tk.Button(navFrame, text=f"{textos[i]}", width=13, height=2, command=comandos[i], background="#6c757d", foreground="#fefefe", font=roboto)
        button.pack(side="left")


    frameGeneral3 = tk.Frame(root, background="#bc6c25")
    frameGeneral3.pack(pady=10, padx=10)
    frameGeneral1 = tk.Frame(root, background="#bc6c25")
    frameGeneral1.pack(padx=10)
    frameGeneral2 = tk.Frame(root, background="#bc6c25")
    frameGeneral2.pack(pady=10, padx=10)


    #----------------------------------FRAME LABELS----------------------------------

    def patientSearch():
        pacienteValue = askstring("Ingresar Datos", "Por favor, ingrese un numero de dni sin puntos ni espacios.",parent=root)
        valores = (pacienteValue,)
        consulta = "SELECT cod_paciente, Nombre, Papellido, dni FROM pacientes WHERE dni = %s"
        cursor = conexion.cursor()
        cursor.execute(consulta, valores)
        registros = cursor.fetchall()
        cursor.close()

        pacienteLabel.config(text = "")
        medicoLabel.config(text = "")
        fechaLabel.config(text = "")
        patologiaLabel.config(text = "")
        horaLabel.config(text = "")
        pisoLabel.config(text = "")
        habitacionLabel.config(text = "")
        camaLabel.config(text = "")
        for item in pacienteTree.get_children():
            pacienteTree.delete(item)
        for item in medicoTree.get_children():
            medicoTree.delete(item)
        for item in patologiaTree.get_children():
            patologiaTree.delete(item)
        for item in añoTree.get_children():
            añoTree.delete(item)
        for item in mesTree.get_children():
            mesTree.delete(item)
        for item in diaTree.get_children():
            diaTree.delete(item)
        for item in horaTree.get_children():
            horaTree.delete(item)
        for item in pisoTree.get_children():
            pisoTree.delete(item)
        for item in habitacionTree.get_children():
            habitacionTree.delete(item)
        for item in camaTree.get_children():
            camaTree.delete(item)

        for registro in registros:
            pacienteTree.insert("", "end", values=registro)

    pacienteSearchButton = tk.Button(frameGeneral3, width=20, height=1, command=patientSearch, text="Buscar Paciente", background="#6c757d", foreground="#fefefe", font=roboto)
    pacienteSearchButton.grid(row=0, column=0, rowspan=2, columnspan=2, padx=5, pady=5)

    label1 = tk.Label(frameGeneral3, text="Paciente", background="#bc6c25", foreground="#fefefe", font=roboto)
    label1.grid(row=0, column=3, padx=25, pady=2)
    pacienteLabel = tk.Label(frameGeneral3, height=1, background="#bc6c25", foreground="#fefefe", font=roboto)
    pacienteLabel.grid(row=1, column=3, padx=25, pady=2)

    label2 = tk.Label(frameGeneral3, text="Patologia", background="#bc6c25", foreground="#fefefe", font=roboto)
    label2.grid(row=0, column=4, padx=25, pady=2)
    patologiaLabel = tk.Label(frameGeneral3, height=1, background="#bc6c25", foreground="#fefefe", font=roboto)
    patologiaLabel.grid(row=1, column=4, padx=25, pady=2)

    label3 = tk.Label(frameGeneral3, text="Medico", background="#bc6c25", foreground="#fefefe", font=roboto)
    label3.grid(row=0, column=5, padx=25, pady=2)
    medicoLabel = tk.Label(frameGeneral3, height=1, background="#bc6c25", foreground="#fefefe", font=roboto)
    medicoLabel.grid(row=1, column=5, padx=25, pady=2)

    label4 = tk.Label(frameGeneral3, text="Fecha", background="#bc6c25", foreground="#fefefe", font=roboto)
    label4.grid(row=0, column=6, padx=25, pady=2)
    fechaLabel = tk.Label(frameGeneral3, height=1, background="#bc6c25", foreground="#fefefe", font=roboto)
    fechaLabel.grid(row=1, column=6, padx=25, pady=2)

    label5 = tk.Label(frameGeneral3, text="Hora", background="#bc6c25", foreground="#fefefe", font=roboto)
    label5.grid(row=0, column=7, padx=25, pady=2)
    horaLabel = tk.Label(frameGeneral3, height=1, background="#bc6c25", foreground="#fefefe", font=roboto)
    horaLabel.grid(row=1, column=7, padx=25, pady=2)

    label6 = tk.Label(frameGeneral3, text="Piso", background="#bc6c25", foreground="#fefefe", font=roboto)
    label6.grid(row=0, column=8, padx=25, pady=2)
    pisoLabel = tk.Label(frameGeneral3, height=1, background="#bc6c25", foreground="#fefefe", font=roboto)
    pisoLabel.grid(row=1, column=8, padx=25, pady=2)

    label7 = tk.Label(frameGeneral3, text="Habitacion", background="#bc6c25", foreground="#fefefe", font=roboto)
    label7.grid(row=0, column=9, padx=25, pady=2)
    habitacionLabel = tk.Label(frameGeneral3, height=1, background="#bc6c25", foreground="#fefefe", font=roboto)
    habitacionLabel.grid(row=1, column=9, padx=25, pady=2)

    label8 = tk.Label(frameGeneral3, text="Cama", background="#bc6c25", foreground="#fefefe", font=roboto)
    label8.grid(row=0, column=10, padx=25, pady=2)
    camaLabel = tk.Label(frameGeneral3, height=1, background="#bc6c25", foreground="#fefefe", font=roboto)
    camaLabel.grid(row=1, column=10, padx=25, pady=2)


    #--------------------------------------TREEVIEW DE PACIENTE#--------------------------------------
    
    def on_tree_double_click_paciente(event):
        item_seleccionado = pacienteTree.focus()

        if item_seleccionado:
            # Obtiene los valores de las dos primeras columnas del registro
            valores = pacienteTree.item(item_seleccionado, "values")
            
            if valores:
                # Muestra los valores en el Label
                pacienteLabel.config(text=valores[0])
            
        for a in pacienteTree.get_children():
            pacienteTree.delete(a)

        consulta = "SELECT * FROM patologias"
        cursor = conexion.cursor()
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()

        for a in patologiaTree.get_children():
            patologiaTree.delete(a)

        for registro in registros:
            patologiaTree.insert("", "end", values=registro)



    framePaciente = tk.Frame(frameGeneral1, background="#bc6c25")
    framePaciente.pack(side="left", pady=10, padx=10)

    pacienteTree = ttk.Treeview(framePaciente, columns=("Cod Paciente", "Nombre", "Apellido"))
    pacienteTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,4):
        pacienteTree.column(f"#{c}", width=100, anchor="center")
        pacienteTree.column("#0", width=0, anchor="center")

    headings = ["Cod Paciente", "Nombre", "Apellido"]

    for e in range(len(headings)):
        headNum = [1,2,3]
        pacienteTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")

    pacienteTree.bind("<Double-1>", lambda event: on_tree_double_click_paciente(event))

    scrollbarPaciente = ttk.Scrollbar(framePaciente, orient="vertical", command=pacienteTree.yview)
    scrollbarPaciente.grid(row=1, column=2, sticky="ns")

    pacienteTree.configure(yscroll=scrollbarPaciente.set)

    framePaciente.grid_rowconfigure(0, weight=1)
    framePaciente.grid_columnconfigure(0, weight=1)

    #--------------------------------------TREEVIEW DE PATOLOGIA#--------------------------------------


    def on_tree_double_click_patologia(event):
        item_seleccionado = patologiaTree.focus()

        if item_seleccionado:
            # Obtiene los valores de las dos primeras columnas del registro
            valores = patologiaTree.item(item_seleccionado, "values")
            
            if valores:
                patologiaLabel.config(text=valores[0])
            
        for a in patologiaTree.get_children():
            patologiaTree.delete(a)

        consulta = "SELECT cod_medico, Nombre, Mapellido FROM medicos"
        cursor = conexion.cursor()
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()

        for a in medicoTree.get_children():
            medicoTree.delete(a)

        for registro in registros:
            medicoTree.insert("", "end", values=registro)

    framePatologia = tk.Frame(frameGeneral1, background="#bc6c25")
    framePatologia.pack(side="left", pady=10, padx=10)

    patologiaTree = ttk.Treeview(framePatologia, columns=("Cod Patologia", "Patologia"))
    patologiaTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,3):
        patologiaTree.column(f"#{c}", width=165, anchor="center")
        patologiaTree.column("#0", width=0, anchor="center")

    headings = ["Cod Patologia", "Patologia"]

    for e in range(len(headings)):
        headNum = [1,2]
        patologiaTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    patologiaTree.bind("<Double-1>", lambda event: on_tree_double_click_patologia(event))

    scrollbarPat = ttk.Scrollbar(framePatologia, orient="vertical", command=patologiaTree.yview)
    scrollbarPat.grid(row=1, column=2, sticky="ns")
    
    patologiaTree.configure(yscroll=scrollbarPat.set)

    framePatologia.grid_rowconfigure(0, weight=1)
    framePatologia.grid_columnconfigure(0, weight=1)

    #--------------------------------------TREEVIEW DE MEDICO#--------------------------------------

    def on_tree_double_click_medico(event):
        item_seleccionado = medicoTree.focus()

        if item_seleccionado:
            valores = medicoTree.item(item_seleccionado, "values")
            
            if valores:
                medicoLabel.config(text=valores[0])  # Actualiza el contenido de pacienteLabel
            
        for a in medicoTree.get_children():
            medicoTree.delete(a)

        for a in añoTree.get_children():
            añoTree.delete(a)

        for i in range(2023, 2051):
            añoTree.insert("", "end", values=(i,))


    frameMedico = tk.Frame(frameGeneral1, background="#bc6c25")
    frameMedico.pack(side="left", pady=10, padx=10)

    medicoTree = ttk.Treeview(frameMedico, columns=("Cod Medico", "Nombre", "Apellido"))
    medicoTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,4):
        medicoTree.column(f"#{c}", width=100, anchor="center")
        medicoTree.column("#0", width=0, anchor="center")

    headings = ["Cod Medico", "Nombre", "Apellido"]

    for e in range(len(headings)):
        headNum = [1,2,3]
        medicoTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    medicoTree.bind("<Double-1>", lambda event: on_tree_double_click_medico(event))

    scrollbar = ttk.Scrollbar(frameMedico, orient="vertical", command=medicoTree.yview)
    scrollbar.grid(row=1, column=2, sticky="ns")
    
    medicoTree.configure(yscroll=scrollbar.set)

    frameMedico.grid_rowconfigure(0, weight=1)
    frameMedico.grid_columnconfigure(0, weight=1)


    #--------------------------------------TREEVIEW DE FECHA#--------------------------------------

    #--------------------------------------TREEVIEW DE AÑO#--------------------------------------

    año = tk.StringVar()
    mes = tk.StringVar()
    dia = tk.StringVar()
    hora = tk.StringVar()
    piso = tk.StringVar()
    habitacion = tk.StringVar()
    cama = tk.StringVar()

    def on_tree_double_click_año(event):
        global año
        item_seleccionado = añoTree.focus()

        if item_seleccionado:
            valores = añoTree.item(item_seleccionado, "values")
            
            if valores:
                año = valores[0]
                fechaLabel.config(text=f"00/00/{año}")
            
        for a in añoTree.get_children():
            añoTree.delete(a)

        for i in range(2023, 2051):
            añoTree.insert("", "end", values=(i,))

        horaLabel.config(text = "")
        pisoLabel.config(text = "")
        habitacionLabel.config(text = "")
        camaLabel.config(text = "")
        for item in mesTree.get_children():
            mesTree.delete(item)
        for item in diaTree.get_children():
            diaTree.delete(item)
        for item in horaTree.get_children():
            horaTree.delete(item)
        for item in pisoTree.get_children():
            pisoTree.delete(item)
        for item in habitacionTree.get_children():
            habitacionTree.delete(item)
        for item in camaTree.get_children():
            camaTree.delete(item)

        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

        for i in range(len(months)):
            mesTree.insert("", "end", values=months[i])



    frameAño = tk.Frame(frameGeneral2, background="#bc6c25")
    frameAño.pack(side="left", pady=10, padx=10)

    añoTree = ttk.Treeview(frameAño, columns=("Año"))
    añoTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,2):
        añoTree.column(f"#{c}", width=98, anchor="center")
        añoTree.column("#0", width=0, anchor="center")

    headings = ["Año"]  

    for e in range(len(headings)):
        headNum = [1]
        añoTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    añoTree.bind("<Double-1>", lambda event: on_tree_double_click_año(event))

    scrollbarAño = ttk.Scrollbar(frameAño, orient="vertical", command=añoTree.yview)
    scrollbarAño.grid(row=1, column=2, sticky="ns")
    
    añoTree.configure(yscroll=scrollbarAño.set)

    frameAño.grid_rowconfigure(0, weight=1)
    frameAño.grid_columnconfigure(0, weight=1)

    #--------------------------------------TREEVIEW DE MES#--------------------------------------

    def on_tree_double_click_mes(event):
        global año
        global mes
        item_seleccionado = mesTree.focus()

        horaLabel.config(text = "")
        pisoLabel.config(text = "")
        habitacionLabel.config(text = "")
        camaLabel.config(text = "")
        for item in diaTree.get_children():
            diaTree.delete(item)
        for item in horaTree.get_children():
            horaTree.delete(item)
        for item in pisoTree.get_children():
            pisoTree.delete(item)
        for item in habitacionTree.get_children():
            habitacionTree.delete(item)
        for item in camaTree.get_children():
            camaTree.delete(item)

        if item_seleccionado:
            valores = mesTree.item(item_seleccionado, "values")

            if valores:



                mes = valores[0]
                if mes == "Enero":
                    mes = "01"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Febrero":
                    mes = "02"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 30):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Marzo":
                    mes = "03"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Abril":
                    mes = "04"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 31):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Mayo":
                    mes = "05"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Junio":
                    mes = "06"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 31):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Julio":
                    mes = "07"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Agosto":
                    mes = "08"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Septiembre":
                    mes = "09"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 31):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Octubre":
                    mes = "10"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Noviembre":
                    mes = "11"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 31):
                        diaTree.insert("", "end", values=str(i).zfill(2))



                elif mes == "Diciembre":
                    mes = "12"
                    fechaLabel.config(text=f"00/{mes}/{año}")
                    for i in range(1, 32):
                        diaTree.insert("", "end", values=str(i).zfill(2))



        for a in mesTree.get_children():
            mesTree.delete(a)

        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

        for i in range(len(months)):
            mesTree.insert("", "end", values=months[i])


    frameMes = tk.Frame(frameGeneral2, background="#bc6c25")
    frameMes.pack(side="left", pady=10, padx=10)

    mesTree = ttk.Treeview(frameMes, columns=("Mes"))
    mesTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,2):
        mesTree.column(f"#{c}", width=98, anchor="center")
        mesTree.column("#0", width=0, anchor="center")

    headings = ["Mes"]  

    for e in range(len(headings)):
        headNum = [1]
        mesTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    mesTree.bind("<Double-1>", lambda event: on_tree_double_click_mes(event))

    scrollbarMes = ttk.Scrollbar(frameMes, orient="vertical", command=mesTree.yview)
    scrollbarMes.grid(row=1, column=2, sticky="ns")
    
    mesTree.configure(yscroll=scrollbarMes.set)

    frameMes.grid_rowconfigure(0, weight=1)
    frameMes.grid_columnconfigure(0, weight=1)

    #--------------------------------------TREEVIEW DE DIA#--------------------------------------

    def on_tree_double_click_dia(event):
        global año
        global mes
        global dia
        item_seleccionado = diaTree.focus()

        if item_seleccionado:
            valores = diaTree.item(item_seleccionado, "values")
            
            if valores:
                dia = valores[0]
                fechaLabel.config(text=f"{dia}/{mes}/{año}")
            

        horaLabel.config(text = "")
        pisoLabel.config(text = "")
        habitacionLabel.config(text = "")
        camaLabel.config(text = "")
        for item in horaTree.get_children():
            horaTree.delete(item)
        for item in pisoTree.get_children():
            pisoTree.delete(item)
        for item in habitacionTree.get_children():
            habitacionTree.delete(item)
        for item in camaTree.get_children():
            camaTree.delete(item)

        horas = ["08:00", "08:30", "09:00", "09:30", "10:00", "10:30",
                "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
                "14:00", "14:30", "15:00", "15:30", "16:00", "16:30"]

        for i in range(len(horas)):
            horaTree.insert("", "end", values=horas[i])



    frameDia = tk.Frame(frameGeneral2, background="#bc6c25")
    frameDia.pack(side="left", pady=10, padx=10)

    diaTree = ttk.Treeview(frameDia, columns=("Dia"))
    diaTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,2):
        diaTree.column(f"#{c}", width=98, anchor="center")
        diaTree.column("#0", width=0, anchor="center")

    headings = ["Dia"]  

    for e in range(len(headings)):
        headNum = [1]
        diaTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    diaTree.bind("<Double-1>", lambda event: on_tree_double_click_dia(event))

    scrollbarDia = ttk.Scrollbar(frameDia, orient="vertical", command=diaTree.yview)
    scrollbarDia.grid(row=1, column=2, sticky="ns")
    
    diaTree.configure(yscroll=scrollbarDia.set)

    frameDia.grid_rowconfigure(0, weight=1)
    frameDia.grid_columnconfigure(0, weight=1)


    #--------------------------------------TREEVIEW DE HORA#--------------------------------------

    def on_tree_double_click_hora(event):
        global hora
        item_seleccionado = horaTree.focus()

        if item_seleccionado:
            valores = horaTree.item(item_seleccionado, "values")

            if valores:
                hora = valores[0]
                horaLabel.config(text=f"{hora}")

                pisoLabel.config(text = "")
                habitacionLabel.config(text = "")
                camaLabel.config(text = "")

                for item in pisoTree.get_children():
                    pisoTree.delete(item)
                for item in habitacionTree.get_children():
                    habitacionTree.delete(item)
                for item in camaTree.get_children():
                    camaTree.delete(item)


                for i in range(1,3):
                    pisoTree.insert("", "end", values=i)
            

    frameHora = tk.Frame(frameGeneral2, background="#bc6c25")
    frameHora.pack(side="left", pady=10, padx=10)

    horaTree = ttk.Treeview(frameHora, columns=("Hora"))
    horaTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,2):
        horaTree.column(f"#{c}", width=98, anchor="center")
        horaTree.column("#0", width=0, anchor="center")

    headings = ["Hora"]  

    for e in range(len(headings)):
        headNum = [1]
        horaTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    horaTree.bind("<Double-1>", lambda event: on_tree_double_click_hora(event))

    scrollbarHora = ttk.Scrollbar(frameHora, orient="vertical", command=horaTree.yview)
    scrollbarHora.grid(row=1, column=2, sticky="ns")
    
    horaTree.configure(yscroll=scrollbarHora.set)


    frameHora.grid_rowconfigure(0, weight=1)
    frameHora.grid_columnconfigure(0, weight=1)


    #--------------------------------------TREEVIEW DE LUGAR#--------------------------------------

    #--------------------------------------TREEVIEW DE PISO#--------------------------------------

    def on_tree_double_click_piso(event):
        global piso
        item_seleccionado = pisoTree.focus()

        if item_seleccionado:
            valores = pisoTree.item(item_seleccionado, "values")

            if valores:
                piso = valores[0]
                pisoLabel.config(text=f"{piso}")

                habitacionLabel.config(text = "")
                camaLabel.config(text = "")
                for item in habitacionTree.get_children():
                    habitacionTree.delete(item)
                for item in camaTree.get_children():
                    camaTree.delete(item)

            if piso == "1":
                for a in habitacionTree.get_children():
                    habitacionTree.delete(a)
                for i in range(1,7):
                    habitacionTree.insert("", "end", values=i)

            elif piso == "2":
                for a in habitacionTree.get_children():
                    habitacionTree.delete(a)
                for i in range(7,21):
                    habitacionTree.insert("", "end", values=i)


    framePiso = tk.Frame(frameGeneral2, background="#bc6c25")
    framePiso.pack(side="left", pady=10, padx=10)

    pisoTree = ttk.Treeview(framePiso, columns=("Piso"))
    pisoTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,2):
        pisoTree.column(f"#{c}", width=98, anchor="center")
        pisoTree.column("#0", width=0, anchor="center")

    headings = ["Piso"]  

    for e in range(len(headings)):
        headNum = [1]
        pisoTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    pisoTree.bind("<Double-1>", lambda event: on_tree_double_click_piso(event))

    scrollbarAño = ttk.Scrollbar(framePiso, orient="vertical", command=pisoTree.yview)
    scrollbarAño.grid(row=1, column=2, sticky="ns")
    
    pisoTree.configure(yscroll=scrollbarAño.set)

    framePiso.grid_rowconfigure(0, weight=1)
    framePiso.grid_columnconfigure(0, weight=1)

    #--------------------------------------TREEVIEW DE HABITACION#--------------------------------------

    def on_tree_double_click_habitacion(event):
        global habitacion
        item_seleccionado = habitacionTree.focus()

        if item_seleccionado:
            valores = habitacionTree.item(item_seleccionado, "values")

            if valores:
                    habitacion = valores[0]
                    habitacionLabel.config(text=f"{habitacion}")

                    camaLabel.config(text = "")
                    for item in camaTree.get_children():
                        camaTree.delete(item)

                    pacienteValue = pacienteLabel.cget("text")
                    medicoValue = medicoLabel.cget("text")
                    fechaValue = fechaLabel.cget("text")
                    horaValue = horaLabel.cget("text")
                    pisoValue = pisoLabel.cget("text")
                    habValue = habitacionLabel.cget("text")

                    for i in range(1, 3):
                        sql = f"SELECT paciente, medico, fecha, hora, piso, num_hab, num_cama FROM internaciones WHERE paciente = '{pacienteValue}' AND medico = '{medicoValue}' AND fecha = '{fechaValue}' AND hora = '{horaValue}' AND piso = '{pisoValue}' AND num_hab = '{habValue}' AND num_cama = '{i}'"
                        
                        cursor = conexion.cursor()
                        cursor.execute(sql)
                        resultados = cursor.fetchall()
                        cursor.close()

                        if resultados:
                            color = "red"  # Rojo para coincidencias
                            color1 = "white"
                            camaTree.insert("", "end", values=str(i), tags=(color,color1,))
                        else:
                            color = "green"  # Verde para no coincidencias
                            color1 = "white"
                            camaTree.insert("", "end", values=str(i), tags=(color,color1,))

                    camaTree.tag_configure("red", background="red")
                    camaTree.tag_configure("green", background="green")
                    camaTree.tag_configure("white", foreground="white")


    frameHabitacion = tk.Frame(frameGeneral2, background="#bc6c25")
    frameHabitacion.pack(side="left", pady=10, padx=10)

    habitacionTree = ttk.Treeview(frameHabitacion, columns=("Habitacion"))
    habitacionTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,2):
        habitacionTree.column(f"#{c}", width=98, anchor="center")
        habitacionTree.column("#0", width=0, anchor="center")

    headings = ["Habitacion"]  

    for e in range(len(headings)):
        headNum = [1]
        habitacionTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    habitacionTree.bind("<Double-1>", lambda event: on_tree_double_click_habitacion(event))

    scrollbarMes = ttk.Scrollbar(frameHabitacion, orient="vertical", command=habitacionTree.yview)
    scrollbarMes.grid(row=1, column=2, sticky="ns")
    
    habitacionTree.configure(yscroll=scrollbarMes.set)

    frameHabitacion.grid_rowconfigure(0, weight=1)
    frameHabitacion.grid_columnconfigure(0, weight=1)

    #--------------------------------------TREEVIEW DE CAMA#--------------------------------------

    def on_tree_double_click_cama(event):
        global cama

        item_seleccionado = camaTree.focus()

        if item_seleccionado:
            valores = camaTree.item(item_seleccionado, "values")

            if valores:
                cama = valores[0]
                camaLabel.config(text=f"{cama}")


    frameCama = tk.Frame(frameGeneral2, background="#bc6c25")
    frameCama.pack(side="left", pady=10, padx=10)

    camaTree = ttk.Treeview(frameCama, columns=("Cama"))
    camaTree.grid(row=1, column=0, columnspan=2, sticky="nsew")

    for c in range(1,2):
        camaTree.column(f"#{c}", width=98, anchor="center")
        camaTree.column("#0", width=0, anchor="center")

    headings = ["Cama"]  

    for e in range(len(headings)):
        headNum = [1]
        camaTree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    camaTree.bind("<Double-1>", lambda event: on_tree_double_click_cama(event))

    scrollbarCama = ttk.Scrollbar(frameCama, orient="vertical", command=camaTree.yview)
    scrollbarCama.grid(row=1, column=2, sticky="ns")
    
    camaTree.configure(yscroll=scrollbarCama.set)

    frameCama.grid_rowconfigure(0, weight=1)
    frameCama.grid_columnconfigure(0, weight=1)

    def cargar_internacion():
        pacienteValue = pacienteLabel.cget("text")
        medicoValue = medicoLabel.cget("text")
        fechaValue = fechaLabel.cget("text")
        patologiaValue = patologiaLabel.cget("text")
        horaValue = horaLabel.cget("text")
        pisoValue = pisoLabel.cget("text")
        habValue = habitacionLabel.cget("text")
        camaValue = camaLabel.cget("text")

        if pacienteValue == "" or medicoValue == "" or fechaValue == "" or patologiaValue == "" or horaValue == "" or pisoValue == "" or habValue == "" or camaValue == "":
            messagebox.showerror("Campos vacios", "Uno o mas campos se encuentran vacios.")
        else:
            try:
                sql1 = f"SELECT * FROM internaciones WHERE paciente = '{pacienteValue}' AND medico = '{medicoValue}' AND fecha = '{fechaValue}' AND hora = '{horaValue}' AND piso = '{pisoValue}' AND num_hab = '{habValue}' AND num_cama = '{camaValue}'"
                
                cursor = conexion.cursor()
                cursor.execute(sql1)
                resultados = cursor.fetchall()
                cursor.close()

                if resultados:
                    messagebox.showinfo("Internacion ocupada", "La internacion seleccionada se encuentra ocupada.")
                else:
                    valores = (fechaValue, horaValue, pacienteValue, medicoValue, patologiaValue, pisoValue, habValue, camaValue,)
                    sql2 = "INSERT INTO internaciones (fecha, hora, paciente, medico, patologia, piso, num_hab, num_cama) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor = conexion.cursor()
                    cursor.execute(sql2, valores)
                    conexion.commit()
                    cursor.close()
                    messagebox.showinfo("Éxito", "La internacion ha sido cargada exitosamente.")
                    pacienteLabel.config(text = "")
                    medicoLabel.config(text = "")
                    fechaLabel.config(text = "")
                    patologiaLabel.config(text = "")
                    horaLabel.config(text = "")
                    pisoLabel.config(text = "")
                    habitacionLabel.config(text = "")
                    camaLabel.config(text = "")
                    for item in pacienteTree.get_children():
                        pacienteTree.delete(item)
                    for item in medicoTree.get_children():
                        medicoTree.delete(item)
                    for item in patologiaTree.get_children():
                        patologiaTree.delete(item)
                    for item in añoTree.get_children():
                        añoTree.delete(item)
                    for item in mesTree.get_children():
                        mesTree.delete(item)
                    for item in diaTree.get_children():
                        diaTree.delete(item)
                    for item in horaTree.get_children():
                        horaTree.delete(item)
                    for item in pisoTree.get_children():
                        pisoTree.delete(item)
                    for item in habitacionTree.get_children():
                        habitacionTree.delete(item)
                    for item in camaTree.get_children():
                        camaTree.delete(item)

            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    executeButton = tk.Button(frameGeneral3, text="Asignar Internacion", width=20, height=1, command=cargar_internacion, background="#6c757d", foreground="#fefefe", font=roboto)
    executeButton.grid(row=0, column=11, rowspan=2, columnspan=2, padx=5, pady=2)

    root.mainloop()


def ventanaEspecialidades():

    root = tk.Tk()
    root.title("Especialidades")
    root.geometry("1108x500")
    root.iconbitmap("resources/imagenn.ico")
    root.configure(bg="#bc6c25")
    root.resizable(False, False)

    centrar_ventana(root)

    def abrirInicio():
        root.withdraw()
        ventanaInicio()

    def abrirPacientes():
        root.withdraw()
        ventanaPacientes()

    def abrirMedicos():
        root.withdraw()
        ventanaMedicos()

    def abrirHistoriasClinicas():
        root.withdraw()
        ventanaHistoriasClinicas()

    def abrirTurnos():
        root.withdraw()
        ventanaTurnos()

    def abrirAsignarT():
        root.withdraw()
        ventanaAsignarT()

    def abrirInternaciones():
        root.withdraw()
        ventanaInternaciones()

    def abrirAsignarI():
        root.withdraw()
        ventanaAsignarI()

    def abrirEspecialidades():
        root.withdraw()
        ventanaEspecialidades()

    def abrirPatologias():
        root.withdraw()
        ventanaPatologias()

    def abrirUsuarios():
        root.withdraw()
        ventanaUsuarios()

    navFrame = tk.Frame(root)
    navFrame.pack()

    variables = ["btnInicio", "btnPacientes", "btnMedicos", "btnHistoriasClinicas", "Asignar Turnos", "btnTurnos", "btnInternaciones", "Asignar Internacion", "btnEspecialidades", "btnPatologias", "btnUsuarios"]

    textos = ["Inicio", "Pacientes", "Medicos", "Historias Clinicas", "Turnos", "Asignar \n Turnos", "Internaciones", "Asignar \n Internacion", "Especialidades", "Patologias", "Usuarios"]

    comandos = [abrirInicio, abrirPacientes, abrirMedicos, abrirHistoriasClinicas, abrirTurnos, abrirAsignarT, abrirInternaciones, abrirAsignarI, abrirEspecialidades, abrirPatologias, abrirUsuarios]

    roboto = ("Roboto", 8, "bold")

    for i in range(len(variables)):
        button = variables[i]
        button = tk.Button(navFrame, text=f"{textos[i]}", width=13, height=2, command=comandos[i], background="#6c757d", foreground="#fefefe", font=roboto)
        button.pack(side="left")

    def actualizar_treeview():

        cursor = conexion.cursor()
        if tree.get_children():
            tree.delete(*tree.get_children())
        select_query = "SELECT * FROM especialidades" 
        cursor.execute(select_query)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        cursor.close()

    def modificarRegistro():
        codValue = codVar.get()
        nombreValue = nombreVar.get()      

        update_query = "UPDATE especialidades SET Especialidad = %s WHERE cod_especialidad = %s "
        valores = (nombreValue, codValue)
        
        if codValue == "" or nombreValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            valor = (codValue,)
            consulta2 = "SELECT * FROM especialidades WHERE cod_especialidad = %s"
            cursor = conexion.cursor()
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchall()
            cursor.close()

            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea modificar el registro?")
                if confirmacion:
                    cursor = conexion.cursor()
                    cursor.execute(update_query, valores)
                    conexion.commit()
                    cursor.close()
                    messagebox.showinfo("Exito", "El registro ha sido modificado exitosamente.")
                    actualizar_treeview()

                    textos = [codVar, nombreVar]

                    for i in range(len(textos)):
                        nuevo_valor = "" 
                        textos[i].delete(0, tk.END)
                        textos[i].insert(0, nuevo_valor)
                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera modificado.")
            else:
                messagebox.showerror("Error", "El codigo de especialidad ingresado no existe.")


    def cargarRegistro():
        nombreValue = str(nombreVar.get()).strip()
        
        valores = (nombreValue,)

        insert_query = "INSERT INTO especialidades (Especialidad) VALUES (%s)"
        
        if nombreValue == "":
            messagebox.showerror("Error", "El campo se encuentra vacío.")
        else:
            cursor = conexion.cursor()
            cursor.execute(insert_query, valores)
            messagebox.showinfo("Éxito", "El registro ha sido cargado exitosamente.")
            conexion.commit()
            cursor.close()
            actualizar_treeview()

            textos = [codVar, nombreVar]

            for i in range(len(textos)):
                nuevo_valor = "" 
                textos[i].delete(0, tk.END)
                textos[i].insert(0, nuevo_valor)

    def eliminarRegistro():
        id_to_delete = codVar.get()

        if id_to_delete == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else: 
            valor = (id_to_delete,)
            consulta2 = "SELECT * FROM especialidades WHERE cod_especialidad = %s"
            cursor = conexion.cursor()
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchall()
            cursor.close()

            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar el registro?")
                if confirmacion:
                    valores = (id_to_delete,)
                    delete_query = "DELETE FROM especialidades WHERE cod_especialidad = %s"
                    cursor = conexion.cursor()
                    cursor.execute(delete_query, valores)
                    conexion.commit()
                    cursor.close()
                    messagebox.showinfo("Exito", "El registro ha sido eliminado exitosamente.")
                    actualizar_treeview()

                    textos = [codVar, nombreVar]

                    for i in range(len(textos)):
                        nuevo_valor = "" 
                        textos[i].delete(0, tk.END)
                        textos[i].insert(0, nuevo_valor)
                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera eliminado.")
            else:
                messagebox.showerror("Error", "El codigo de especialidad ingresado no existe.")



    def volcarTodo():
        consulta = "SELECT * FROM especialidades"
        cursor = conexion.cursor()
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()
        for a in tree.get_children():
            tree.delete(a)
            

        for registro in registros:
            tree.insert("", "end", values=registro)

    def on_tree_double_click(event):
        item = tree.selection()[0]
        values = tree.item(item, "values")

        textboxx = [codVar, nombreVar]

        for index, value in enumerate(values):
            textboxx[index].delete(0, tk.END)
            textboxx[index].insert(0, value)


    def columnSearch(event):
        comboValue = comboSearch.get()
        searchValue = search.get()

        consulta = None

        if comboValue == "":
            messagebox.showinfo("Campo Vacio", "El selector se encuentra vacio.")
        elif comboValue == "Especialidad":
            consulta = "SELECT * FROM especialidades WHERE Especialidad LIKE %s"
        elif comboValue != "Especialidad":
            messagebox.showinfo("Columna no válida", "La columna seleccionada no es válida.")

        cursor = conexion.cursor()
        cursor.execute(consulta, ("%" + searchValue + "%",))
        registros = cursor.fetchall()
        cursor.close()
        for a in tree.get_children():
            tree.delete(a)   

        if searchValue == "":  
            for a in tree.get_children():
                tree.delete(a)     
        else:
            for registro in registros:
                tree.insert("", "end", values=registro)


    searchFrame = tk.Frame(root, background="#bc6c25")
    searchFrame.pack(pady=10)

    comboSearch = ttk.Combobox(searchFrame, values=["Especialidad"], width=39)
    comboSearch.pack(side="left", padx=10)

    search = tk.Entry(searchFrame, width=39, font=roboto)
    search.pack(side="left", padx=10)

    search.bind("<KeyRelease>", columnSearch)

    tree_frame = tk.Frame(root, background="#bc6c25")
    tree_frame.pack(pady=10)

    tree = ttk.Treeview(tree_frame, columns=("Cod Especialidad", "Especialidad"))

    for c in range(1,2):
        tree.column(f"#{c}", width=400, anchor="center")
        tree.column("#0", width=0, anchor="center")
        tree.column("#2", width=400, anchor="center")


    headings = ["Cod Especialidad", "Especialidad"]

    for e in range(2):
        headNum = [1,2]
        tree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    tree.bind("<Double-1>", on_tree_double_click)


    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)


    tree.grid(row=0, column=0, sticky="nsew")


    scrollbar.grid(row=0, column=1, sticky="ns")


    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

    textbox_frame = tk.Frame(root, background="#bc6c25")
    textbox_frame.pack(pady=10)

    labels = ["Código de Especialidad", "Especialidad"]

    for i in range(2):
        label = tk.Label(textbox_frame, text=f"{labels[i]}", background="#bc6c25", foreground="#fefefe", font=roboto)
        label.grid(row=1, column=i, padx=5, pady=5)


    def saltoEntry(event, sigEntry):
        sigEntry.focus_set()

    codVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    codVar.grid(row=2, column=0, padx=2, pady=5)

    nombreVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    nombreVar.grid(row=2, column=1, padx=2, pady=5)

    codVar.bind('<Return>', lambda event, entry=nombreVar: saltoEntry(event, entry))


    btn_frame = tk.Frame(root, background="#bc6c25")
    btn_frame.pack(pady=10, padx=30)

    btn_cargar_registro = tk.Button(btn_frame, text="Cargar Registro", command=cargarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_modificar = tk.Button(btn_frame, text="Modificar Registro", command=modificarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_eliminar = tk.Button(btn_frame, text="Eliminar Registro", command=eliminarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_volcar = tk.Button(btn_frame, text="Buscar sin Filtros", command=volcarTodo, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)

    btn_cargar_registro.pack(side="left", padx=10, pady=10)
    btn_modificar.pack(side="left", padx=10, pady=10)
    btn_eliminar.pack(side="left", padx=10, pady=10)
    btn_volcar.pack(side="left", padx=10, pady=10)


    root.mainloop()


def ventanaPatologias():
    root = tk.Tk()
    root.title("Patologias")
    root.geometry("1108x500")
    root.iconbitmap("resources/imagenn.ico")
    root.configure(bg="#bc6c25")
    root.resizable(False, False)

    centrar_ventana(root)

    def abrirInicio():
        root.withdraw()
        ventanaInicio()

    def abrirPacientes():
        root.withdraw()
        ventanaPacientes()

    def abrirMedicos():
        root.withdraw()
        ventanaMedicos()

    def abrirHistoriasClinicas():
        root.withdraw()
        ventanaHistoriasClinicas()

    def abrirTurnos():
        root.withdraw()
        ventanaTurnos()

    def abrirAsignarT():
        root.withdraw()
        ventanaAsignarT()

    def abrirInternaciones():
        root.withdraw()
        ventanaInternaciones()

    def abrirAsignarI():
        root.withdraw()
        ventanaAsignarI()

    def abrirEspecialidades():
        root.withdraw()
        ventanaEspecialidades()

    def abrirPatologias():
        root.withdraw()
        ventanaPatologias()

    def abrirUsuarios():
        root.withdraw()
        ventanaUsuarios()

    navFrame = tk.Frame(root)
    navFrame.pack()

    variables = ["btnInicio", "btnPacientes", "btnMedicos", "btnHistoriasClinicas", "Asignar Turnos", "btnTurnos", "btnInternaciones", "Asignar Internacion", "btnEspecialidades", "btnPatologias", "btnUsuarios"]

    textos = ["Inicio", "Pacientes", "Medicos", "Historias Clinicas", "Turnos", "Asignar \n Turnos", "Internaciones", "Asignar \n Internacion", "Especialidades", "Patologias", "Usuarios"]

    comandos = [abrirInicio, abrirPacientes, abrirMedicos, abrirHistoriasClinicas, abrirTurnos, abrirAsignarT, abrirInternaciones, abrirAsignarI, abrirEspecialidades, abrirPatologias, abrirUsuarios]

    roboto = ("Roboto", 8, "bold")

    for i in range(len(variables)):
        button = variables[i]
        button = tk.Button(navFrame, text=f"{textos[i]}", width=13, height=2, command=comandos[i], background="#6c757d", foreground="#fefefe", font=roboto)
        button.pack(side="left")

    def actualizar_treeview():
        cursor = conexion.cursor()
        if tree.get_children():
            tree.delete(*tree.get_children())
        select_query = "SELECT * FROM patologias" 
        cursor.execute(select_query)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        cursor.close()

    def modificarRegistro():
        codValue = codVar.get()
        nombreValue = nombreVar.get()      

        update_query = "UPDATE patologias SET Patologia = %s WHERE cod_patologia = %s "
        valores = (nombreValue, codValue)
        
        if codValue == "" or nombreValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            valor = (codValue,)
            consulta2 = "SELECT * FROM patologias WHERE cod_patologia = %s"

            cursor = conexion.cursor()
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchone()
            cursor.close()

            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea modificar el registro?")
                if confirmacion:
                    valor = (codValue,)
                    consulta2 = "SELECT * FROM patologias WHERE cod_patologia = %s"

                    cursor = conexion.cursor()
                    cursor.execute(consulta2, valor)
                    resultado = cursor.fetchall()
                    cursor.close()

                    if resultado:
                        cursor = conexion.cursor()
                        cursor.execute(update_query, valores)
                        conexion.commit()
                        cursor.close()
                        messagebox.showinfo("Exito", "El registro ha sido modificado exitosamente.")
                        actualizar_treeview()

                        textos = [codVar, nombreVar]

                        for i in range(len(textos)):
                            nuevo_valor = "" 
                            textos[i].delete(0, tk.END)
                            textos[i].insert(0, nuevo_valor)
                    else:
                        messagebox.showerror("Error", "El codigo de especialidad ingresado no existe.")
                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera modificado.")

            else:
                messagebox.showerror("Error", "El codigo de patologia ingresado no existe.")

    def cargarRegistro():
        nombreValue = str(nombreVar.get()).strip()
        
        valores = (nombreValue,)

        insert_query = "INSERT INTO patologias (Patologia) VALUES (%s)"
        
        if nombreValue == "":
            messagebox.showerror("Error", "El campo se encuentra vacío.")
        else:
            cursor = conexion.cursor()
            cursor.execute(insert_query, valores)
            messagebox.showinfo("Éxito", "El registro ha sido cargado exitosamente.")
            conexion.commit()
            cursor.close()
            actualizar_treeview()

            textos = [codVar, nombreVar]

            for i in range(len(textos)):
                nuevo_valor = "" 
                textos[i].delete(0, tk.END)
                textos[i].insert(0, nuevo_valor)

    def eliminarRegistro():
        id_to_delete = codVar.get()

        if id_to_delete == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else: 
            valor = (id_to_delete,)
            consulta2 = "SELECT * FROM patologias WHERE cod_patologia = %s"
            cursor = conexion.cursor()
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchall()
            cursor.close()

            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar el registro?")
                if confirmacion:
                    valores = (id_to_delete,)
                    delete_query = "DELETE FROM patologias WHERE cod_patologia = %s"
                    cursor = conexion.cursor()
                    cursor.execute(delete_query, valores)
                    conexion.commit()
                    cursor.close()
                    messagebox.showinfo("Exito", "El registro ha sido eliminado exitosamente.")
                    actualizar_treeview()

                    textos = [codVar, nombreVar]

                    for i in range(len(textos)):
                        nuevo_valor = "" 
                        textos[i].delete(0, tk.END)
                        textos[i].insert(0, nuevo_valor)
                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera eliminado.")
            else:
                messagebox.showerror("Error", "El codigo de patologia ingresado no existe.")


    def volcarTodo():
        consulta = "SELECT * FROM patologias"
        cursor = conexion.cursor()
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()
        for a in tree.get_children():
            tree.delete(a)
            

        for registro in registros:
            tree.insert("", "end", values=registro)

    def on_tree_double_click(event):
        item = tree.selection()[0]
        values = tree.item(item, "values")

        textboxx = [codVar, nombreVar]

        for index, value in enumerate(values):
            textboxx[index].delete(0, tk.END)
            textboxx[index].insert(0, value)


    def columnSearch(event):
        comboValue = comboSearch.get()
        searchValue = search.get()

        consulta = None

        if comboValue == "":
            messagebox.showinfo("Campo Vacio", "El selector se encuentra vacio.")
        elif comboValue == "Patologia":
            consulta = "SELECT * FROM patologias WHERE Patologia LIKE %s"
        elif comboValue != "Patologia":
            messagebox.showinfo("Columna no válida", "La columna seleccionada no es válida.")

        cursor = conexion.cursor()
        cursor.execute(consulta, ("%" + searchValue + "%",))
        registros = cursor.fetchall()
        cursor.close()

        for a in tree.get_children():
            tree.delete(a)

        if searchValue == "":  
            for a in tree.get_children():
                tree.delete(a)
        else:
            for registro in registros:
                tree.insert("", "end", values=registro)



    searchFrame = tk.Frame(root, background="#bc6c25")
    searchFrame.pack(pady=10)

    comboSearch = ttk.Combobox(searchFrame, values=["Patologia"], width=39)
    comboSearch.pack(side="left", padx=10)

    search = tk.Entry(searchFrame, width=39, font=roboto)
    search.pack(side="left", padx=10)

    search.bind("<KeyRelease>", columnSearch)

    tree_frame = tk.Frame(root, background="#bc6c25")
    tree_frame.pack(pady=10)

    tree = ttk.Treeview(tree_frame, columns=("Cod Patologia", "Patologia"))

    for c in range(1,2):
        tree.column(f"#{c}", width=400, anchor="center")
        tree.column("#0", width=0, anchor="center")
        tree.column("#2", width=400, anchor="center")


    headings = ["Cod Patologia", "Patologia"]

    for e in range(2):
        headNum = [1,2]
        tree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    tree.bind("<Double-1>", on_tree_double_click)


    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)


    tree.grid(row=0, column=0, sticky="nsew")


    scrollbar.grid(row=0, column=1, sticky="ns")


    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

    textbox_frame = tk.Frame(root, background="#bc6c25")
    textbox_frame.pack(pady=10)

    labels = ["Código de Patologia", "Patologia"]

    for i in range(2):
        label = tk.Label(textbox_frame, text=f"{labels[i]}", background="#bc6c25", foreground="#fefefe", font=roboto)
        label.grid(row=1, column=i, padx=5, pady=5)


    def saltoEntry(event, sigEntry):
        sigEntry.focus_set()

    codVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    codVar.grid(row=2, column=0, padx=5, pady=5)

    nombreVar = tk.Entry(textbox_frame, width=20, font=roboto) 
    nombreVar.grid(row=2, column=1, padx=5, pady=5)

    codVar.bind('<Return>', lambda event, entry=nombreVar: saltoEntry(event, entry))

    btn_frame = tk.Frame(root, background="#bc6c25")
    btn_frame.pack(pady=10, padx=30)

    btn_cargar_registro = tk.Button(btn_frame, text="Cargar Registro", command=cargarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_modificar = tk.Button(btn_frame, text="Modificar Registro", command=modificarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_eliminar = tk.Button(btn_frame, text="Eliminar Registro", command=eliminarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_volcar = tk.Button(btn_frame, text="Buscar sin Filtros", command=volcarTodo, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)

    btn_cargar_registro.pack(side="left", padx=10, pady=10)
    btn_modificar.pack(side="left", padx=10, pady=10)
    btn_eliminar.pack(side="left", padx=10, pady=10)
    btn_volcar.pack(side="left", padx=10, pady=10)


    root.mainloop()


def ventanaUsuarios():
    root = tk.Tk()
    root.title("Usuarios")
    root.geometry("1108x500")
    root.iconbitmap("resources/imagenn.ico")
    root.configure(bg="#bc6c25")
    root.resizable(False, False)

    centrar_ventana(root)

    def abrirInicio():
        root.withdraw()
        ventanaInicio()

    def abrirPacientes():
        root.withdraw()
        ventanaPacientes()

    def abrirMedicos():
        root.withdraw()
        ventanaMedicos()

    def abrirHistoriasClinicas():
        root.withdraw()
        ventanaHistoriasClinicas()

    def abrirTurnos():
        root.withdraw()
        ventanaTurnos()

    def abrirAsignarT():
        root.withdraw()
        ventanaAsignarT()

    def abrirInternaciones():
        root.withdraw()
        ventanaInternaciones()

    def abrirAsignarI():
        root.withdraw()
        ventanaAsignarI()

    def abrirEspecialidades():
        root.withdraw()
        ventanaEspecialidades()

    def abrirPatologias():
        root.withdraw()
        ventanaPatologias()

    def abrirUsuarios():
        root.withdraw()
        ventanaUsuarios()

    navFrame = tk.Frame(root)
    navFrame.pack()

    variables = ["btnInicio", "btnPacientes", "btnMedicos", "btnHistoriasClinicas", "Asignar Turnos", "btnTurnos", "btnInternaciones", "Asignar Internacion", "btnEspecialidades", "btnPatologias", "btnUsuarios"]

    textos = ["Inicio", "Pacientes", "Medicos", "Historias Clinicas", "Turnos", "Asignar \n Turnos", "Internaciones", "Asignar \n Internacion", "Especialidades", "Patologias", "Usuarios"]

    comandos = [abrirInicio, abrirPacientes, abrirMedicos, abrirHistoriasClinicas, abrirTurnos, abrirAsignarT, abrirInternaciones, abrirAsignarI, abrirEspecialidades, abrirPatologias, abrirUsuarios]

    roboto = ("Roboto", 8, "bold")

    for i in range(len(variables)):
        button = variables[i]
        button = tk.Button(navFrame, text=f"{textos[i]}", width=13, height=2, command=comandos[i], background="#6c757d", foreground="#fefefe", font=roboto)
        button.pack(side="left")

    def actualizar_treeview():

        cursor = conexion.cursor()
        if tree.get_children():
            tree.delete(*tree.get_children())
        select_query = "SELECT * FROM usuarios" 
        cursor.execute(select_query)
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        cursor.close()

    def modificarRegistro():
        codUserValue = cod_user_var.get()
        userValue = user_var.get()
        passValue = pass_var.get()
        
        # Actualizar los registros en la base de datos
        update_query = "UPDATE usuarios SET nom_usuario = %s, contraseña = %s WHERE cod_usuario = %s"
        valores = (userValue, passValue, codUserValue,)
        
        if codUserValue == "" or userValue == "" or passValue == "" :
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            valor = (codUserValue,)
            consulta2 = "SELECT * FROM usuarios WHERE cod_usuario = %s"
            cursor = conexion.cursor()
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchone()
            cursor.close()

            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea modificar el registro?")
                if confirmacion:
                    valor = (codUserValue,)
                    consulta2 = "SELECT * FROM usuarios WHERE cod_usuario = %s"
                    cursor = conexion.cursor()
                    cursor.execute(consulta2, valor)
                    resultado = cursor.fetchall()
                    cursor.close()

                    if resultado:
                        cursor = conexion.cursor()
                        cursor.execute(update_query, valores)
                        conexion.commit()
                        cursor.close()
                        messagebox.showinfo("Exito", "El registro ha sido modificado exitosamente.")
                        actualizar_treeview()

                        textCamp = [cod_user_var, user_var, pass_var]

                        for i in range(len(textCamp)):
                            nuevo_valor = ""  # Reemplaza esto con el valor que deseas cargar
                            textCamp[i].delete(0, tk.END)
                            textCamp[i].insert(0, nuevo_valor)
                    else:
                        messagebox.showerror("Error", "El codigo de usuario ingresado no existe.")

                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera modificado.")

            else:
                messagebox.showerror("Error", "El codigo de usuario ingresado no existe.")

    def cargarRegistro():
        userValue = str(user_var.get()).strip()
        passValue = str(pass_var.get()).strip()
        
        valores = (userValue, passValue)

        insert_query = "INSERT INTO usuarios (nom_usuario, contraseña) VALUES (%s, %s)"
        
        if userValue == "" or passValue == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else:
            cursor = conexion.cursor()
            cursor.execute(insert_query, valores)
            messagebox.showinfo("Éxito", "El registro ha sido cargado exitosamente.")
            conexion.commit()
            cursor.close()
            actualizar_treeview()

            textCamp = [cod_user_var, user_var, pass_var]

            for i in range(len(textCamp)):
                nuevo_valor = ""  # Reemplaza esto con el valor que deseas cargar
                textCamp[i].delete(0, tk.END)
                textCamp[i].insert(0, nuevo_valor)


    # Función para eliminar un registro de la base de datos
    def eliminarRegistro():
        id_to_delete = cod_user_var.get()

        if id_to_delete == "":
            messagebox.showerror("Error", "Uno o varios campos se encuentran vacíos.")
        else: 
            valor = (id_to_delete,)
            consulta2 = "SELECT * FROM usuarios WHERE cod_usuario = %s"
            cursor = conexion.cursor()
            cursor.execute(consulta2, valor)
            resultado = cursor.fetchall()
            cursor.close()

            if resultado:
                confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar el registro?")
                if confirmacion:
                    valores = (id_to_delete,)
                    delete_query = "DELETE FROM usuarios WHERE cod_usuario = %s"
                    cursor = conexion.cursor()
                    cursor.execute(delete_query, valores)
                    conexion.commit()
                    cursor.close()
                    messagebox.showinfo("Exito", "El registro ha sido eliminado exitosamente.")
                    actualizar_treeview()

                    textCamp = [cod_user_var, user_var, pass_var]

                    for i in range(len(textCamp)):
                        nuevo_valor = ""  # Reemplaza esto con el valor que deseas cargar
                        textCamp[i].delete(0, tk.END)
                        textCamp[i].insert(0, nuevo_valor)
                else:
                    messagebox.showinfo("Cancelacion", "El registro no sera eliminado.")
            else:
                messagebox.showerror("Error", "El codigo de usuarios ingresado no existe.")

    # Función para volcar datos desde la base de datos al Treeview
    def volcarTodo():
        consulta = "SELECT * FROM usuarios"
        cursor = conexion.cursor()
        cursor.execute(consulta)
        registros = cursor.fetchall()
        cursor.close()
        
        for a in tree.get_children():
            tree.delete(a)
            
            # Llenar el Treeview con los datos
        for registro in registros:
            tree.insert("", "end", values=registro)

    def on_tree_double_click(event):
        item = tree.selection()[0]  # Obtiene el primer elemento seleccionado
        values = tree.item(item, "values")  # Obtiene los valores de la fila seleccionada

        textboxes = [cod_user_var, user_var, pass_var]

        # Asigna los valores a los Textboxes
        for b, value in enumerate(values):
            textboxes[b].delete(0, tk.END)
            textboxes[b].insert(0, value)


    def columnSearch(event):
        comboValue = comboSearch.get()
        searchValue = search.get()

        consulta = None

        if comboValue == "":
            messagebox.showinfo("Campo Vacio", "El selector se encuentra vacio.")
        if comboValue == "Usuario":
            consulta = "SELECT * FROM usuarios WHERE nom_usuario LIKE %s"
        elif comboValue == "Contraseña":
            consulta = "SELECT * FROM usuarios WHERE contraseña LIKE %s"
        elif comboValue != "Usuario" or comboValue != "Contraseña":
            messagebox.showinfo("Columna no válida", "La columna seleccionada no es válida.")

        cursor = conexion.cursor()
        cursor.execute(consulta, ("%" + searchValue + "%",))
        registros = cursor.fetchall()
        cursor.close()

        for a in tree.get_children():
            tree.delete(a)
        
        if searchValue == "":  
            for a in tree.get_children():
                tree.delete(a)
        else:
            for registro in registros:
                tree.insert("", "end", values=registro)



    searchFrame = tk.Frame(root, background="#bc6c25")
    searchFrame.pack(pady=10)

    comboSearch = ttk.Combobox(searchFrame, values=["Usuario", "Contraseña"], width=35)
    comboSearch.pack(side="left", padx=10)

    search = tk.Entry(searchFrame, width=35, font=roboto)
    search.pack(side="left", padx=10)

    search.bind("<KeyRelease>", columnSearch)

    # Treeview
    tree_frame = tk.Frame(root, background="#bc6c25")
    tree_frame.pack(pady=10)

    tree = ttk.Treeview(tree_frame, columns=("Cod Usuario", "Usuario", "Contraseña"))

    for c in range(1,3):
        tree.column(f"#{c}", width=250, anchor="center")
        tree.column("#0", width=0, anchor="center")
        tree.column("#3", width=250, anchor="center")

    headings = ["Cod Usuario", "Usuario", "Contraseña"]

    for e in range(3):
        headNum = [1,2,3]
        tree.heading(f"#{headNum[e]}", text=f"{headings[e]}")


    tree.bind("<Double-1>", on_tree_double_click)

    # Barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    # Colocar el Treeview usando grid
    tree.grid(row=0, column=0, sticky="nsew")

    # Colocar el scrollbar junto al Treeview usando grid
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configurar el peso de las filas y columnas para que el Treeview se expanda correctamente
    tree_frame.grid_rowconfigure(0, weight=1)
    tree_frame.grid_columnconfigure(0, weight=1)

    # Etiquetas y TextBox
    textbox_frame = tk.Frame(root, background="#bc6c25")
    textbox_frame.pack(pady=10)

    labels = ["Codigo de Usuario", "Usuario", "Contraseña"]

    for i in range(len(labels)):
        label = tk.Label(textbox_frame, text=labels[i], background="#bc6c25", foreground="#fefefe", font=roboto)
        label.grid(row=1, column=i, padx=5, pady=5)
        labels.append(label)


    def saltoEntry(event, sigEntry):
        sigEntry.focus_set()

    cod_user_var = tk.Entry(textbox_frame, width=20, font=roboto)
    cod_user_var.grid(row=2, column=0, padx=5, pady=5)

    user_var = tk.Entry(textbox_frame, width=20, font=roboto)
    user_var.grid(row=2, column=1, padx=5, pady=5)

    pass_var = tk.Entry(textbox_frame, width=20, font=roboto)
    pass_var.grid(row=2, column=2, padx=5, pady=5)

    cod_user_var.bind('<Return>', lambda event, entry=user_var: saltoEntry(event, entry))
    user_var.bind('<Return>', lambda event, entry=pass_var: saltoEntry(event, entry))

    btn_frame = tk.Frame(root, background="#bc6c25")
    btn_frame.pack(pady=10, padx=30)

    btn_cargar_registro = tk.Button(btn_frame, text="Cargar Registro", command=cargarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_modificar = tk.Button(btn_frame, text="Modificar Registro", command=modificarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_eliminar = tk.Button(btn_frame, text="Eliminar Registro", command=eliminarRegistro, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)
    btn_volcar = tk.Button(btn_frame, text="Buscar sin Filtros", command=volcarTodo, width=20, height=2, background="#6c757d", foreground="#fefefe", font=roboto)

    btn_cargar_registro.pack(side="left", padx=10, pady=10)
    btn_modificar.pack(side="left", padx=10, pady=10)
    btn_eliminar.pack(side="left", padx=10, pady=10)
    btn_volcar.pack(side="left", padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    ventanaAcceso()


try:
    conexion.close()

except Exception as e:
    messagebox.showerror("Error", f"Ocurrió un error al cerrar la conexion a la base de datos.")