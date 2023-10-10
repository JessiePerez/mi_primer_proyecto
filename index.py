# Bibliotecas 
from tkinter import *
from tkinter import filedialog
from newspaper import Article
from gtts import gTTS

# FUNCIONES:

# Funcion para mostrar una ventana emergente
def ventana_exitosa():
    caja_dialogo = Toplevel()
    caja_dialogo.geometry('350x150')
    caja_dialogo.resizable(False, False)
    caja_dialogo.title('Conversion')
    mensaje = Label(caja_dialogo, text="Conversion exitosa!", font='arial 20')
    mensaje.pack(pady=50)

# Funcion para mostrar una ventana emergente de error 
def ventana_fallida():
    caja_dialogo = Toplevel()
    caja_dialogo.geometry('350x150')
    caja_dialogo.resizable(False, False)
    caja_dialogo.title('Conversion')
    mensaje = Label(caja_dialogo, text="Conversion fallida!", font='arial 20')
    mensaje.pack(pady=50)

# Funcion que realiza la conversión
def convertir():
    url = caja.get()
    try:
        # Descarga y analiza el artículo de la URL proporcionada
        noticia = Article(url)
        noticia.download()
        noticia.parse()
        texto = noticia.text

        # Convierte el texto en un archivo de audio MP3
        articulo_texto = gTTS(texto, lang='es')
        archivo_guardado = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Archivos de audio MP3", "*.mp3")])
        articulo_texto.save(archivo_guardado)

        # Funcion que muestra una ventana emergente
        ventana_exitosa()
        
    except:
        # Funcion que muestra una ventana emergente Fallida
        ventana_fallida()

# Crear la ventana
ventana = Tk()
ventana.geometry("600x300")
ventana.title("Articulos a mp3 🔊")
ventana.resizable(False, False)
ventana.configure(bg='light blue')

# Titulos y descripciones
titulo = Label(ventana, text="Articulos a voz", font="impact 50", bg=ventana['bg'])
titulo.pack()

descripcion1 = Label(ventana, text="Convierte articulos", font="impact 20", bg=ventana['bg'])
titulo.pack()
descripcion1.pack()

descripcion2 = Label(ventana, text="a formato mp3", font="impact 20", bg=ventana['bg'])
titulo.pack()
descripcion2.pack()

# Caja de texto para ingresar la URL del artículo
caja = Entry(width=30, font="arial 20")
caja.pack(pady=10)

# Boton que inicia la conversion
boton = Button(text="Convertir!", width=10, font="impact 20", command=convertir)
boton.pack()

# Bucle de la interfaz gráfica
ventana.mainloop()
