import tkinter as tk
from tkinter import messagebox
from transformers import pipeline
from PIL import Image, ImageTk


clasificador = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')


comentarios_red_social = [
    "¡Qué película tan emocionante! Me encantó cada momento.",
    "No me gustó nada el servicio en este restaurante.",
    "¡Qué día tan maravilloso! Disfrutando del sol y la playa.",
    "Estoy muy emocionado por el concierto de esta noche.",
    "Qué desastre de película, ¡no la recomiendo en absoluto!"
]

def analizar_sentimiento_hf(texto):
    resultado = clasificador(texto)
    label = resultado[0]['label']


    if label == '1 star':
        emotion = 'Sentimiento muy negativo'
    elif label == '2 stars':
        emotion = 'Sentimiento negativo'
    elif label == '3 stars':
        emotion = 'Sentimiento neutral'
    elif label == '4 stars':
        emotion = 'Sentimiento positivo'
    elif label == '5 stars':
        emotion = 'Sentimiento muy positivo'
    else:
        emotion = 'Sentimiento no identificado'

    return resultado, emotion

def analizar_texto():
    texto = entrada_texto.get("1.0", "end-1c")
    if texto:
        resultado, emocion = analizar_sentimiento_hf(texto)
        messagebox.showinfo("Resultado", f"Sentimiento: {resultado[0]['label']}\nEmoción predominante: {emocion}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, elija o ingrese una frase para analizar.")

def analizar_comentario_red_social():
    comentario_seleccionado = lista_comentarios.curselection()
    if comentario_seleccionado:
        comentario = lista_comentarios.get(comentario_seleccionado)
        resultado, emocion = analizar_sentimiento_hf(comentario)
        messagebox.showinfo("Resultado", f"Sentimiento: {resultado[0]['label']}\nEmoción predominante: {emocion}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un comentario de la lista para analizar.")

def cerrar_ventana():
    ventana.destroy()


ventana = tk.Tk()
ventana.title("Análisis de Sentimientos")
ventana.attributes('-fullscreen', True)


imagen_fondo = Image.open("222.jpg")
imagen_fondo = imagen_fondo.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()))
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)


entrada_texto = tk.Text(ventana, height=20, width=100)
entrada_texto.pack(pady=10)


boton_analizar_frase = tk.Button(ventana, text="Analizar Frase", command=analizar_texto)
boton_analizar_frase.pack()


separador = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
separador.pack(fill=tk.X, padx=5, pady=5)


etiqueta_comentarios_red_social = tk.Label(ventana, text="Seleccione un comentario de Red Social:")
etiqueta_comentarios_red_social.pack()

lista_comentarios = tk.Listbox(ventana, selectmode=tk.SINGLE, height=10, width=100)
for comentario in comentarios_red_social:
    lista_comentarios.insert(tk.END, comentario)
lista_comentarios.pack()


boton_analizar_comentario_red_social = tk.Button(ventana, text="Analizar Comentario de Red Social", command=analizar_comentario_red_social)
boton_analizar_comentario_red_social.pack()


boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()


ventana.mainloop()
