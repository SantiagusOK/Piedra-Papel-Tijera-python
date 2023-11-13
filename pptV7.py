from tkinter import *
import tkinter as tk
import random
import pygame
import time
from threading import Timer
import pickle
from os.path import exists
ventana = Tk()
ventana.geometry("1280x720")
ventana.title("PPT.exe") 
ventana.resizable(0,0)
Font_tuple = ("Gill Sans MT", 50)
fuente_etiquetas_nombres =("Franklin Gothic Heavy",25) 
fuente_etiqueta_rondas = ("NEW ACADEMY",100)
fondo = Label(ventana,borderwidth=0)
fondo.place(x=0,y=0)

pygame.init()
#---------------------------------------------------------------Clases------------------------------------#
class Ppt:
    def __init__(self):
        self.estado = ""
        self.nombre_tu = "Player 1"
        self.nombre_op = "Player 2"

class Entrada_texto:
    def __init__(self):
        self.nombre_tu = ""
        self.nombre_op = ""
        self.entry_tu = Entry(ventana,width=30)
        self.entry_op = Entry(ventana,width=30)
        self.boton_entry = Button(ventana,text="Aceptar",command=self.nombrar,borderwidth=0)

    def mostrar_entradas_Y_botones(self):
        self.boton_entry.place(x=523,y=313)
        self.entry_tu.place(x=325,y=255)
        self.entry_op.place(x=325,y=380)

    def quitar_entradas_y_botones(self):
        self.boton_entry.place_forget()
        self.entry_tu.place_forget()
        self.entry_op.place_forget()
    
    def nombrar(self):
        self.nombre_tu = self.entry_tu.get()
        self.nombre_op = self.entry_op.get()
        if self.nombre_tu == "":
            juego.nombre_tu = "Player 1"
        else:
            juego.nombre_tu = self.nombre_tu
        
        if self.nombre_op == "":
            juego.nombre_op = "Player 2"
        else:
            juego.nombre_op = self.nombre_op

class EstadisticasDelJuego:
    def __init__(self):
        self.ganadas = 0
        self.perdidas = 0
        self.piedra_tu = 0
        self.papel_tu = 0
        self.tijera_tu = 0
        self.piedra_op = 0
        self.papel_op = 0
        self.tijera_op = 0
        self.puntototal_tu = 0
        self.puntototal_op = 0
        self.rondas_ganadas_tu = 0
        self.rondas_ganadas_op = 0

class EstadisticasGUI:
    def dibujar_estadisticas(self):
        self.estats1 = Label(ventana,text=f"Partidas ganadas: {sumar_estadisticas.ganadas}\nPartidas perdidas: {sumar_estadisticas.perdidas}\nPiedra: {sumar_estadisticas.piedra_tu}\nPapel: {sumar_estadisticas.papel_tu}\nTijera: {sumar_estadisticas.tijera_tu}\nPuntos totales: {sumar_estadisticas.puntototal_tu}\nRondas Ganadas: {sumar_estadisticas.rondas_ganadas_tu}\nRondas Perdidas: {sumar_estadisticas.rondas_ganadas_op}",font=fuente_etiquetas_nombres,bg="black",fg="white")
        self.estats1.place(x=200,y=300)
        self.estats2 = Label(ventana,text=f"Partidas ganadas: {sumar_estadisticas.perdidas}\nPartidas perdidas: {sumar_estadisticas.ganadas}\nPiedra: {sumar_estadisticas.piedra_op}\nPapel: {sumar_estadisticas.papel_op}\nTijera: {sumar_estadisticas.tijera_op}\nPuntos totales: {sumar_estadisticas.puntototal_op}\nRondas Ganadas: {sumar_estadisticas.rondas_ganadas_op}\nRondas Perdidas: {sumar_estadisticas.rondas_ganadas_tu}",font=fuente_etiquetas_nombres,bg="black",fg="white")
        self.estats2.place(x=750,y=300)
        self.actualizar_estadisticas()
    def quitar_estadisticas(self):
        reproductor.sonar_seleccion1()
        self.estats1.place_configure(x=2000)
        self.estats2.place_configure(x=2000)
        botones_fin.boton_salirPartida.place_forget()
        cargar_menu()

    def actualizar_estadisticas(self):
        self.estats1.configure(text=f"Partidas ganadas: {sumar_estadisticas.ganadas}\nPartidas perdidas: {sumar_estadisticas.perdidas}\nPiedra: {sumar_estadisticas.piedra_tu}\nPapel: {sumar_estadisticas.papel_tu}\nTijera: {sumar_estadisticas.tijera_tu}\nPuntos totales: {sumar_estadisticas.puntototal_tu}\nRondas Ganadas: {sumar_estadisticas.rondas_ganadas_tu}\nRondas Perdidas: {sumar_estadisticas.rondas_ganadas_op}")
        self.estats2.configure(text=f"Partidas ganadas: {sumar_estadisticas.perdidas}\nPartidas perdidas: {sumar_estadisticas.ganadas}\nPiedra: {sumar_estadisticas.piedra_op}\nPapel: {sumar_estadisticas.papel_op}\nTijera: {sumar_estadisticas.tijera_op}\nPuntos totales: {sumar_estadisticas.puntototal_op}\nRondas Ganadas: {sumar_estadisticas.rondas_ganadas_op}\nRondas Perdidas: {sumar_estadisticas.rondas_ganadas_tu}")    
        
class BotonesFinPartida:
    def __init__(self):
        self.imagen_bJugarDeNuevo = PhotoImage(file="sprites/botones/partida/boton_JugarDeNuevo_spr.png")
        self.imagen_bsalirPartida = PhotoImage(file="sprites/botones/partida/boton_salirpartida_spr.png")
    def boton_fin_partida(self):
        self.boton_JugarDeNuevo = tk.Button(image=self.imagen_bJugarDeNuevo,height=173,width=245,bg="white",relief="flat",borderwidth=0,command=self.quitar_y_empezar)
        self.boton_JugarDeNuevo.place(x=1035,y=547)

        self.boton_salirPartida = tk.Button(image=self.imagen_bsalirPartida,height=173,width=245,bg="white",relief="flat",borderwidth=0)
        self.boton_salirPartida.configure(command=quitar_y_ir_menu)
        self.boton_salirPartida.place(x=0,y=547)
    
    def quitar_botones_fin(self):
        self.boton_JugarDeNuevo.place_forget()
        self.boton_salirPartida.place_forget()
    
    def quitar_y_empezar(self):
        puntos.reiniciar_resultados()
        rondas.ronda = 0
        self.quitar_botones_fin()
        mostrar_ronda()

class BotonesMenu:
    def __init__(self):
        self.puslado_play = True
        self.imagen_bsalir = PhotoImage(file="sprites/botones/menu/boton_salir_spr.png")
        self.imagen_bjugar = PhotoImage(file="sprites/botones/menu/boton_jugar_spr.png")
        self.imagen_bEstadisticas = PhotoImage(file="sprites/botones/menu/boton_estadisticas_spr.png")
        self.imagen_bconfig = PhotoImage(file="sprites/botones/menu/boton_config_spr.png")
        
        self.boton_jugar = tk.Button(image=self.imagen_bjugar,height=214,width=303,bg="white",relief="flat",
        borderwidth=0,command=self.quitar_y_empezar_ronda)

        self.boton_salir = tk.Button(image=self.imagen_bsalir,height=75,width=107,bg="white",relief="flat",
        borderwidth=0,command=self.salir)

        self.boton_estadisticas = tk.Button(image=self.imagen_bEstadisticas,height=214,width=303,bg="white",relief="flat",
        borderwidth=0,command=self.estadisticas)


        self.boton_config = tk.Button(image=self.imagen_bconfig,height=214,width=303,bg="white",relief="flat",
        borderwidth=0,command=self.configuracion)


    def mostrar_botones_menu(self):
        self.boton_jugar.place(x=493,y=336)
        self.boton_salir.place(x=14,y=14)
        self.boton_estadisticas.place(x=808,y=336)
        self.boton_config.place(x=179,y=336)

    def quitar_botones_menu(self):
        self.boton_jugar.place_forget()
        self.boton_salir.place_forget()
        self.boton_estadisticas.place_forget()
        self.boton_config.place_forget()

    def quitar_y_empezar_ronda(self):
        reproductor.sonar_seleccion2()
        botones_menu.quitar_botones_menu()
        mostrar_ronda()
    
    def salir(self):
        with open("estadisticas","wb") as archivo:
            pickle.dump(sumar_estadisticas, archivo)
        exit()
    
    def estadisticas(self):
        dibujar_nombres()
        etiqueta_user_name.place_configure(x=170,y=230)
        etiqueta_op_name.place_configure(x=720,y=230)
        estadisticas_gui.dibujar_estadisticas()
        reproductor.sonar_seleccion1()
        dibujar_fondo_estadisticas()
        reproductor.reproducir_estadisticas()
        botones_menu.quitar_botones_menu()
        botones_fin.boton_fin_partida()
        botones_fin.boton_salirPartida.place_configure(x=10,y=10)
        botones_fin.boton_JugarDeNuevo.place_configure(x=2000)
        botones_fin.boton_salirPartida.configure(command=estadisticas_gui.quitar_estadisticas)
    
    def configuracion(self):
        barra_textos.mostrar_entradas_Y_botones()
        reproductor.sonar_seleccion1()
        reproductor.reproducir_config()
        botones_fondo.mostrar_botones_fondos()
        botones_fondo.dibujar_marco_seleccion()
        botones_config.press_config = True
        mostrar_fondo_config()
        botones_menu.quitar_botones_menu()
        botones_fin.boton_fin_partida()
        botones_fin.boton_salirPartida.configure(command=botones_config.quitar_botones)
        botones_fin.boton_salirPartida.place_configure(y=0)
        botones_fin.boton_JugarDeNuevo.place_forget()
        botones_config.mostrar_boton_volumen_musica()
        botones_config.mostrar_boton_volumen_sonido()
        
class BotonesPPT:
    def __init__(self):
        self.imagen_bpiedra = PhotoImage(file="sprites/botones/partida/boton_piedra_spr.png")
        self.imagen_bpapel = PhotoImage(file="sprites/botones/partida/boton_papel_spr.png")
        self.imagen_btijera = PhotoImage(file="sprites/botones/partida/boton_tijera_spr.png")

        self.img_boton_pidra_on = PhotoImage(file="sprites/botones/partida/boton_piedra_spr_on.png")
        self.img_boton_papel_on = PhotoImage(file="sprites/botones/partida/boton_papel_spr_on.png")
        self.img_boton_tijera_on = PhotoImage(file="sprites/botones/partida/boton_tijera_spr_on.png")
    def mostrar_botones_juego(self):
        self.boton_piedra = tk.Button(image=self.imagen_bpiedra,height=136,width=400,bg="black",relief="flat",borderwidth=0,command=piedra)
        self.boton_piedra.place(x=30,y=570)
        
        self.boton_papel = tk.Button(image=self.imagen_bpapel,height=136,width=400,bg="black",relief="flat",
        borderwidth=0,command=papel)
        self.boton_papel.place(x=440,y=570)
        
        self.boton_tijera = tk.Button(image=self.imagen_btijera,height=136,width=400,bg="black",relief="flat",
        borderwidth=0,command=tijera)
        self.boton_tijera.place(x=850,y=570)

        self.boton_piedra.bind("<Enter>",self.iluminar_boton_piedra)
        self.boton_piedra.bind("<Leave>",self.quitar_iluminar_boton_piedra)

        self.boton_papel.bind("<Enter>",self.iluminar_boton_papel)
        self.boton_papel.bind("<Leave>",self.quitar_iluminar_boton_papel)

        self.boton_tijera.bind("<Enter>",self.iluminar_boton_tijera)
        self.boton_tijera.bind("<Leave>",self.quitar_iluminar_boton_tijera)

    def iluminar_boton_piedra(self,event):
        self.boton_piedra.configure(image=self.img_boton_pidra_on)
    def quitar_iluminar_boton_piedra(self,event):
        self.boton_piedra.configure(image=self.imagen_bpiedra)

    def iluminar_boton_papel(self,event):
        self.boton_papel.configure(image=self.img_boton_papel_on)
    def quitar_iluminar_boton_papel(self,event):
        self.boton_papel.configure(image=self.imagen_bpapel)

    def iluminar_boton_tijera(self,event):
        self.boton_tijera.configure(image=self.img_boton_tijera_on)
    def quitar_iluminar_boton_tijera(self,event):
        self.boton_tijera.configure(image=self.imagen_btijera)

    def quitar_botones_juego(self):
        self.boton_piedra.place_forget()
        self.boton_papel.place_forget()
        self.boton_tijera.place_forget()

class Puntuación:
    def __init__(self):
        self.puntos_tu = 0
        self.puntos_op = 0
        self.ganadas = 0
        self.perdidas = 0
        self.resultados = ""
        self.etiqueta_resultados = tk.Label(ventana,text=f"{self.puntos_tu}  -  {self.puntos_op}",bg="black",fg="white",font=Font_tuple,height=1,width=15)
    
    def punto_tu(self):
        self.puntos_tu += 1
        sumar_estadisticas.puntototal_tu += 1

    def reiniciar_resultados(self):
        self.puntos_tu = 0
        self.puntos_op = 0

    def punto_op(self):
        self.puntos_op += 1
        sumar_estadisticas.puntototal_op += 1

    def revisar_resultados(self):
        if rondas.ronda == 1:
            while True:
                if self.puntos_tu == 3:
                    sumar_estadisticas.rondas_ganadas_tu += 1
                    reproductor.reproducir_ganaste_ronda()
                    ganaste()
                    break
                if self.puntos_op == 3:
                    sumar_estadisticas.rondas_ganadas_op += 1
                    reproductor.reproducir_perdiste_ronda() 
                    perdiste()
                    break
                tiempo_esperar2()
                break
        if rondas.ronda == 2:
            while True:
                if self.puntos_tu == 6:
                    reproductor.reproducir_ganaste_ronda()
                    sumar_estadisticas.rondas_ganadas_tu += 1
                    ganaste()
                    break
                if self.puntos_op == 6:
                    sumar_estadisticas.rondas_ganadas_op += 1
                    reproductor.reproducir_perdiste_ronda()  
                    perdiste()
                    break
                tiempo_esperar2()
                break
        if rondas.ronda == 3:
            while True:
                if self.puntos_tu == 9:
                    sumar_estadisticas.ganadas += 1
                    sumar_estadisticas.rondas_ganadas_tu += 1
                    reproductor.reproducir_ganaste_partida()
                    ganaste()
                    break
                if self.puntos_op == 9:
                    sumar_estadisticas.rondas_ganadas_op += 1
                    sumar_estadisticas.perdidas += 1
                    reproductor.reproducir_perdiste_partida()  
                    perdiste()
                    break
                tiempo_esperar2()
                break
    
    def dibujar_resultados(self):
        self.etiqueta_resultados.place_configure(x=545,y=40)  
    
    def actualizar_resultados(self):
        self.etiqueta_resultados.configure(text=f"{self.puntos_tu}  -  {self.puntos_op}",bg="black",fg="white",font=Font_tuple,height=1,width=5)
    
    def quitar_resultados(self):
        self.etiqueta_resultados.place_configure(x=2000)

class Musica_fondo:
    def __init__(self):
        self.mute_musica = False
        self.mute_sonido = False
        self.volumen_musica = 0.4
        self.volumen_sonido = 5
        self.musica_menu = ("musica/menu_music.wav")
        self.musica_estadisticas = ("musica/estadisticas.wav")
        self.musica_config = ("musica/configuracion.wav")
        self.musica_partida = ("musica/partida.wav")
        self.musica_partida1 = ("musica/partida1.wav")
        self.musica_partida2 = ("musica/partida2.wav")
        self.musica_partida3 = ("musica/partida3.wav")

        self.musica_ganaste_partida = ("musica/ganaste.wav")
        self.musica_perdiste_partida = ("musica/perdiste.wav")


        self.musica_perdiste_ronda = ("musica/fail.wav")
        self.musica_ganaste_ronda = ("musica/victory.wav")
        self.sonido_coin = ("sonido/coin.wav")
        self.sonido_ronda1 = ("sonido/round1.wav")
        self.sonido_ronda2 = ("sonido/round2.wav")
        self.sonido_ronda3 = ("sonido/round3.wav")
        self.sonido_select1 = ("sonido/select1.wav")
        self.sonido_select2 = ("sonido/select2.wav")

        self.ronda1 = pygame.mixer.Sound(self.sonido_ronda1)
        self.ronda2 = pygame.mixer.Sound(self.sonido_ronda2)
        self.ronda3 = pygame.mixer.Sound(self.sonido_ronda3)
        self.seleccion1 = pygame.mixer.Sound(self.sonido_select1)
        self.seleccion2 = pygame.mixer.Sound(self.sonido_select2)
        self.sonido_coin = pygame.mixer.Sound(self.sonido_coin)

    def mutear_musica(self):
        self.volumen_musica = 0

    def mutear_sonido(self):
        self.volumen_sonido = 0
    
    def desmutear_musica(self):
        self.volumen_musica = 0.4
    
    def desmutear_sonido(self):
        self.volumen_sonido = 5
    
    def revisar_ronda(self):
        if rondas.ronda == 1:
            self.sonar_ronda1()
        if rondas.ronda == 2:
            self.sonar_ronda2()
        if rondas.ronda ==3:
            self.sonar_ronda3()
    
    def reproducir_menu(self):
        pygame.mixer.music.load(self.musica_menu)
        pygame.mixer.music.set_volume(self.volumen_musica)
        pygame.mixer.music.play(999)
    
    def reproducir_config(self):
        pygame.mixer.music.load(self.musica_config)
        pygame.mixer.music.set_volume(self.volumen_musica)
        pygame.mixer.music.play(999)
    
    def reproducir_estadisticas(self):
        pygame.mixer.music.load(self.musica_estadisticas)
        pygame.mixer.music.set_volume(self.volumen_musica)
        pygame.mixer.music.play(999)
    
    def reproducir_aleatorio(self):
        r = random.randint(0,3)
        if r == 0:
            self.reproducir_partida()
        if r == 1:
            self.reproducir_partida1()
        if r == 2:
            self.reproducir_partida2()
        if r == 3:
            self.reproducir_partida3()

    def reproducir_partida(self):
        pygame.mixer.music.load(self.musica_partida)
        pygame.mixer.music.set_volume(self.volumen_musica)
        pygame.mixer.music.play(999)     

    def reproducir_partida1(self):
        pygame.mixer.music.load(self.musica_partida1)
        pygame.mixer.music.set_volume(self.volumen_musica)
        pygame.mixer.music.play(999)
    
    def reproducir_partida2(self):
        pygame.mixer.music.load(self.musica_partida2)
        pygame.mixer.music.set_volume(self.volumen_musica)
        pygame.mixer.music.play(999)
    
    def reproducir_partida3(self):
        pygame.mixer.music.load(self.musica_partida3)
        pygame.mixer.music.set_volume(self.volumen_musica)
        pygame.mixer.music.play(999)

    
    def reproducir_perdiste_ronda(self):
        pygame.mixer.music.load(self.musica_perdiste_ronda)
        pygame.mixer.music.play()
    
    def reproducir_ganaste_ronda(self):
        pygame.mixer.music.load(self.musica_ganaste_ronda)
        pygame.mixer.music.play()

    def reproducir_ganaste_partida(self):
        pygame.mixer.music.load(self.musica_ganaste_partida)
        pygame.mixer.music.set_volume(self.volumen_musica)
        pygame.mixer.music.play()

    def reproducir_perdiste_partida(self):
        pygame.mixer.music.load(self.musica_perdiste_partida)
        pygame.mixer.music.set_volume(self.volumen_musica)
        pygame.mixer.music.play()
    
    def sonar_seleccion1(self):
        self.seleccion1.set_volume(self.volumen_sonido)
        self.seleccion1.play()

    def sonar_seleccion2(self):
        self.seleccion2.set_volume(self.volumen_sonido)
        self.seleccion2.play()

    def sonar_coin(self):
        self.sonido_coin.set_volume(self.volumen_sonido)
        self.sonido_coin.play()

    def sonar_ronda1(self):
        self.ronda1.set_volume(self.volumen_sonido)
        self.ronda1.play()
    
    def sonar_ronda2(self):
        self.ronda2.set_volume(self.volumen_sonido)
        self.ronda2.play()

    def sonar_ronda3(self):
        self.ronda3.set_volume(self.volumen_sonido)
        self.ronda3.play()

class ContadorRondas:
    def __init__(self):
        self.ronda = 0
        self.etiqueta_ronda = Label(ventana,font=fuente_etiqueta_rondas,bg="black",fg="white")
        self.etiqueta_ronda.place(x=2000)
    
    def dibujar_rondas(self):
        self.etiqueta_ronda.place_configure(x=320,y=280)
        fondo.configure(image=imagen_fondo_negro)
    
    def quitar_rondas(self):
        self.etiqueta_ronda.place_configure(x=2000)
    
    def actualizar_rondas(self):
        self.etiqueta_ronda.configure(text=f"RONDA {self.ronda}")
    
class BotonesConfiguracion:
    def __init__(self):
        self.press_config = False
        self.imagen_bvolumen_on = PhotoImage(file="sprites/botones/config/boton_volumen_on.png")
        self.imagen_bvolumen_off = PhotoImage(file="sprites/botones/config/boton_volumen_off.png")
    def mostrar_boton_volumen_musica(self):
        self.boton_volumen = Button(ventana,image=imagen_bvolumen_on,height=84,width=144)
        self.boton_volumen.place(x=1058,y=145)
        self.revisar_mute_y_boton_musica()
    
    def mostrar_boton_volumen_sonido(self):
        self.boton_volumen_sonido = Button(ventana,image=imagen_bvolumen_on,height=84,width=144)
        self.boton_volumen_sonido.place(x=1058,y=328)
        self.revisar_mute_y_boton_sonido()

    def quitar_botones(self):
        barra_textos.quitar_entradas_y_botones()
        reproductor.sonar_seleccion1()
        botones_fondo.quitar_botones_fondos()
        self.boton_volumen.place_forget()
        self.boton_volumen_sonido.place_forget()
        botones_fin.boton_salirPartida.place_forget()
        cargar_menu()

    def mutear_musica(self):
        reproductor.sonar_seleccion1()
        reproductor.mute_musica = True
        reproductor.mutear_musica()
        reproductor.reproducir_config()
        self.revisar_mute_y_boton_musica()
    
    def desmutear_musica(self):
        reproductor.sonar_seleccion1()
        reproductor.desmutear_musica()
        reproductor.mute_musica = False
        reproductor.reproducir_config()
        self.revisar_mute_y_boton_musica()

    def mutear_sonido(self):
        reproductor.sonar_seleccion1()
        reproductor.mute_sonido = True
        reproductor.mutear_sonido()
        self.revisar_mute_y_boton_sonido()
    
    def desmutear_sonido(self):
        reproductor.sonar_seleccion1()
        reproductor.mute_sonido = False
        reproductor.desmutear_sonido()
        self.revisar_mute_y_boton_sonido()
    
    def revisar_mute_y_boton_musica(self):
        if reproductor.mute_musica:
            self.boton_volumen.configure(image=imagen_bvolumen_off,command=self.desmutear_musica)
        else:
            self.boton_volumen.configure(image=imagen_bvolumen_on,command=self.mutear_musica)
    
    def revisar_mute_y_boton_sonido(self):
        if reproductor.mute_sonido:
            self.boton_volumen_sonido.configure(image=imagen_bvolumen_off,command=self.desmutear_sonido)
        else:
            self.boton_volumen_sonido.configure(image=imagen_bvolumen_on,command=self.mutear_sonido)

class BotonesFondos:
    def __init__(self):
        self.fondo_elegido = "fondo1"
        self.imagen_bfondo1 = PhotoImage(file="sprites/botones/config/boton_fondo1.png")
        self.imagen_bfondo1_select = PhotoImage(file="sprites/botones/config/boton_fondo1_select.png")
        self.imagen_bfondo2 = PhotoImage(file="sprites/botones/config/boton_fondo2.png")
        self.imagen_bfondo2_select = PhotoImage(file="sprites/botones/config/boton_fondo2_select.png")
        self.imagen_bfondo3 = PhotoImage(file="sprites/botones/config/boton_fondo3.png")
        self.imagen_bfondo3_select = PhotoImage(file="sprites/botones/config/boton_fondo3_select.png")
        self.imagen_bfondo4 = PhotoImage(file="sprites/botones/config/boton_fondo4.png")
        self.imagen_bfondo4_select = PhotoImage(file="sprites/botones/config/boton_fondo4_select.png")
        self.imagen_bfondo5 = PhotoImage(file="sprites/botones/config/boton_fondo5.png")
        self.imagen_bfondo5_select = PhotoImage(file="sprites/botones/config/boton_fondo5_select.png")
        self.imagen_bfondo6 = PhotoImage(file="sprites/botones/config/boton_fondo6.png")
        self.imagen_bfondo6_select = PhotoImage(file="sprites/botones/config/boton_fondo6_select.png")

    def mostrar_botones_fondos(self):
        self.boton_fondo1 = Button(ventana,image=self.imagen_bfondo1,height=116,width=205,borderwidth=0,relief="flat",bg="black",command=self.eleccion_fondo1)
        self.boton_fondo1.place(x=208,y=452)

        self.boton_fondo2 = Button(ventana,image=self.imagen_bfondo2,height=116,width=205,borderwidth=0,relief="flat",bg="black",command=self.eleccion_fondo2)
        self.boton_fondo2.place(x=429,y=452)

        self.boton_fondo3 = Button(ventana,image=self.imagen_bfondo3,height=116,width=205,borderwidth=0,relief="flat",bg="black",command=self.eleccion_fondo3)
        self.boton_fondo3.place(x=656,y=452)

        self.boton_fondo4 = Button(ventana,image=self.imagen_bfondo4,height=116,width=205,borderwidth=0,relief="flat",bg="black",command=self.eleccion_fondo4)
        self.boton_fondo4.place(x=206,y=587)

        self.boton_fondo5 = Button(ventana,image=self.imagen_bfondo5,height=116,width=205,borderwidth=0,relief="flat",bg="black",command=self.eleccion_fondo5)
        self.boton_fondo5.place(x=429,y=587)

        self.boton_fondo6 = Button(ventana,image=self.imagen_bfondo6,height=116,width=205,borderwidth=0,relief="flat",bg="black",command=self.eleccion_fondo6)
        self.boton_fondo6.place(x=655,y=587)

    def quitar_botones_fondos(self):
        self.boton_fondo1.place_forget()
        self.boton_fondo2.place_forget()
        self.boton_fondo3.place_forget()
        self.boton_fondo4.place_forget()
        self.boton_fondo5.place_forget()
        self.boton_fondo6.place_forget()

    def eleccion_fondo1(self):
        reproductor.sonar_seleccion1()
        self.fondo_elegido = "fondo1"
        self.dibujar_marco_seleccion()
    
    def eleccion_fondo2(self):
        reproductor.sonar_seleccion1()
        self.fondo_elegido = "fondo2"
        self.dibujar_marco_seleccion()

    def eleccion_fondo3(self):
        reproductor.sonar_seleccion1()
        self.fondo_elegido = "fondo3"
        self.dibujar_marco_seleccion()
    
    def eleccion_fondo4(self):
        reproductor.sonar_seleccion1()
        self.fondo_elegido = "fondo4"
        self.dibujar_marco_seleccion()

    def eleccion_fondo5(self):
        reproductor.sonar_seleccion1()
        self.fondo_elegido = "fondo5"
        self.dibujar_marco_seleccion()

    def eleccion_fondo6(self):
        reproductor.sonar_seleccion1()
        self.fondo_elegido = "fondo6"
        self.dibujar_marco_seleccion()

    def dibujar_marco_seleccion(self):
        if self.fondo_elegido == "fondo1":
            self.boton_fondo1.configure(image=self.imagen_bfondo1_select)
            self.fondo_elegido = "fondo1"
        else:
            self.boton_fondo1.configure(image=self.imagen_bfondo1)
            
        if self.fondo_elegido == "fondo2":
            self.boton_fondo2.configure(image=self.imagen_bfondo2_select)
            self.fondo_elegido = "fondo2"
        else:
            self.boton_fondo2.configure(image=self.imagen_bfondo2)       

        if self.fondo_elegido == "fondo3":
            self.boton_fondo3.configure(image=self.imagen_bfondo3_select)
            self.fondo_elegido = "fondo3"
        else:
            self.boton_fondo3.configure(image=self.imagen_bfondo3)

        if self.fondo_elegido == "fondo4":
            self.boton_fondo4.configure(image=self.imagen_bfondo4_select)
            self.fondo_elegido = "fondo4"
        else:
            self.boton_fondo4.configure(image=self.imagen_bfondo4)

        if self.fondo_elegido == "fondo5":
            self.boton_fondo5.configure(image=self.imagen_bfondo5_select)
            self.fondo_elegido = "fondo5"
        else:
            self.boton_fondo5.configure(image=self.imagen_bfondo5)

        if self.fondo_elegido == "fondo6":
            self.boton_fondo6.configure(image=self.imagen_bfondo6_select)
            self.fondo_elegido = "fondo6"       
        else:
            self.boton_fondo6.configure(image=self.imagen_bfondo6)
#----------------------------------------------------------------------------------------
barra_textos = Entrada_texto()
sumar_estadisticas = EstadisticasDelJuego()
estadisticas_gui = EstadisticasGUI()
botones_fondo = BotonesFondos()
botones_config = BotonesConfiguracion()
reproductor = Musica_fondo()
rondas = ContadorRondas()
botones_fin = BotonesFinPartida()
botones_menu = BotonesMenu()
puntos = Puntuación()
juego = Ppt()
botones_juego = BotonesPPT()
#--------------------------------------------------------------FUNCIONES--------------------------------#
def piedra():
    sumar_estadisticas.piedra_tu += 1
    reproductor.sonar_seleccion2()
    botones_juego.quitar_botones_juego()
    eleccion_tu.configure(image=imagen_piedra_tu)
    eleccion_bot = random.randint(0,2)
    
    if eleccion_bot == 0:#--------el bot eligio PIEDRA-----------------#
        sumar_estadisticas.piedra_op += 1
        eleccion_op.configure(image=imagen_piedra_op)
        tiempo_esperar()

    if eleccion_bot == 1:#--------el bot eligio PAPEL-----------------#
        sumar_estadisticas.papel_op += 1
        eleccion_op.configure(image=imagen_papel_op)
        puntos.punto_op()
        puntos.revisar_resultados()

    if eleccion_bot == 2:#--------el bot eligio TIJERA-----------------#
        sumar_estadisticas.tijera_op += 1
        eleccion_op.configure(image=imagen_tijera_op)
        puntos.punto_tu()
        puntos.revisar_resultados()

def papel():
    sumar_estadisticas.papel_tu += 1
    reproductor.sonar_seleccion2()
    botones_juego.quitar_botones_juego()
    eleccion_tu.configure(image=imagen_papel_tu)
    eleccion_bot = random.randint(0,2)
        
    if eleccion_bot == 0:#--------el bot eligio PIEDRA-----------------#
        eleccion_op.configure(image=imagen_piedra_op)
        sumar_estadisticas.piedra_op += 1
        puntos.punto_tu()
        puntos.revisar_resultados()

    if eleccion_bot == 1:#--------el bot eligio PAPEL-----------------#
        sumar_estadisticas.papel_op += 1
        eleccion_op.configure(image=imagen_papel_op)
        tiempo_esperar()

    if eleccion_bot == 2:#--------el bot eligio TIJERA-----------------#
        sumar_estadisticas.tijera_op += 1
        eleccion_op.configure(image=imagen_tijera_op)
        puntos.punto_op()
        puntos.revisar_resultados()

def tijera():
    sumar_estadisticas.tijera_tu += 1
    print(sumar_estadisticas.tijera_tu)
    reproductor.sonar_seleccion2()
    botones_juego.quitar_botones_juego()
    eleccion_tu.configure(image=imagen_tijera_tu)
    eleccion_bot = random.randint(0,2)
    
    lista_ppt = ["piedra","papel","tijera"]

    if eleccion_bot == 0:#--------el bot eligio PIEDRA-----------------#
        sumar_estadisticas.piedra_op += 1
        eleccion_op.configure(image=imagen_piedra_op)
        puntos.punto_op()
        puntos.revisar_resultados()

    if eleccion_bot == 1:#--------el bot eligio PAPEL-----------------#
        sumar_estadisticas.papel_op += 1
        eleccion_op.configure(image=imagen_papel_op)
        puntos.punto_tu()
        puntos.revisar_resultados()

    if eleccion_bot == 2:#--------el bot eligio TIJERA-----------------#
        sumar_estadisticas.tijera_op += 1
        eleccion_op.configure(image=imagen_tijera_op)
        tiempo_esperar()

def congelar_programa():
    for i in range(0,1):
        time.sleep(1)
        
def mostrar_pantalla_fin():
    fondo.configure(image=imagen_fondo_negro)
    quitar_sprite()
    puntos.etiqueta_resultados.place_configure(y=300)
    etiqueta_op_name.place_configure(y=330)
    etiqueta_user_name.place_configure(y=330)
    botones_fin.boton_fin_partida()
    rondas.ronda = 0

def mostrar_ronda():
    congelar_programa()
    print(rondas.ronda)
    rondas.ronda += 1 
    print(rondas.ronda)
    reproductor.reproducir_aleatorio()
    reproductor.revisar_ronda()
    rondas.dibujar_rondas()
    rondas.actualizar_rondas()
    print(botones_menu.puslado_play)
    quitar_nombres()
    quitar_sprite()
    puntos.quitar_resultados()
    if botones_menu.puslado_play == True:
        t = Timer(3, empezar_juego)
        t.start()
    else:
        t = Timer(3, empezar_denuevo)
        t.start()



def mostrar_fondo_config():
    fondo.configure(image=imagen_fondo_config)

def contador_fin():
    t1 = Timer(7, mostrar_ronda)
    t1.start()

def sonar_puntos():
    puntos.actualizar_resultados()
    reproductor.sonar_coin()
    tiempo_esperar()

def sonar_puntos_fin():
    puntos.actualizar_resultados()
    reproductor.sonar_coin()

def tiempo_esperar4():
    t3 = Timer(2,sonar_puntos_fin)
    t3.start()

def tiempo_esperar2():
    t2 = Timer(1,sonar_puntos)
    t2.start()

def tiempo_esperar3():
    t4 = Timer(10,mostrar_pantalla_fin)
    t4.start()

def tiempo_esperar():
    t2 = Timer(1,quitar_boton_y_sprite)
    t2.start()




    
def quitar_boton_y_sprite():
    eleccion_tu.configure(image=imagen_nada_azul)
    eleccion_op.configure(image=imagen_nada_rojo)
    botones_juego.mostrar_botones_juego()

def quitar_sprite():
    eleccion_op.place_configure(x=2000)
    eleccion_tu.place_configure(x=2000)

def dibujar_fondo_partida():
    fondo.configure(image=imagen_fondo1)

def dibujar_fondo_estadisticas():
    fondo.configure(image=imagen_fondo_estadisticas)

def empezar_juego():
    puntos.dibujar_resultados()
    puntos.actualizar_resultados()
    cambiar_fondo()
    botones_menu.puslado_play = False
    rondas.quitar_rondas()
    dibujar_nombres()
    eleccion_tu.configure(image=imagen_nada_azul)
    eleccion_op.configure(image=imagen_nada_rojo)
    eleccion_tu.place_configure(x=133,y=207)
    eleccion_op.place_configure(x=756,y=207)
    botones_juego.mostrar_botones_juego()
    botones_menu.quitar_botones_menu()

def cambiar_fondo():
    print(botones_fondo.fondo_elegido)
    if botones_fondo.fondo_elegido == "fondo1":
        fondo.configure(image=imagen_fondo1)

    if botones_fondo.fondo_elegido == "fondo2":
        fondo.configure(image=imagen_fondo2)

    if botones_fondo.fondo_elegido == "fondo3":
        fondo.configure(image=imagen_fondo3)

    if botones_fondo.fondo_elegido == "fondo4":
        fondo.configure(image=imagen_fondo4)

    if botones_fondo.fondo_elegido == "fondo5":
        fondo.configure(image=imagen_fondo5)

    if botones_fondo.fondo_elegido == "fondo6":
        fondo.configure(image=imagen_fondo6)

def empezar_denuevo():
    rondas.quitar_rondas()
    puntos.dibujar_resultados()
    empezar_juego()

def quitar_y_ir_menu():
    reproductor.sonar_seleccion1()
    puntos.reiniciar_resultados()
    puntos.quitar_resultados()
    botones_fin.quitar_botones_fin()
    cargar_menu()

def ganaste():
    tiempo_esperar4()
    botones_juego.quitar_botones_juego()
    juego.estado = "ganaste"
    fondo.configure(image=imagen_ganaste_fondo)
    print(rondas.ronda)
    if rondas.ronda >= 3:
        tiempo_esperar3()
    if rondas.ronda < 3:
        contador_fin()

def perdiste():
    tiempo_esperar4()
    juego.estado = "perdiste"
    botones_juego.quitar_botones_juego()
    fondo.configure(image=imagen_perdiste_fondo)
    print(rondas.ronda)
    if rondas.ronda >= 3:
        tiempo_esperar3()
    if rondas.ronda < 3:
        contador_fin()

def cargar_menu():
    botones_menu.mostrar_botones_menu()
    if exists("estadisticas.pkl"):
        with open("estadisticas","rb") as archivo:
            sumar_estadisticas = EstadisticasDelJuego()
    else:
        sumar_estadisticas = EstadisticasDelJuego()
    rondas.ronda = 0
    reproductor.reproducir_menu()
    botones_menu.puslado_play = True
    quitar_nombres()
    eleccion_tu.place_configure(x=2000)
    eleccion_op.place_configure(x=2000)
    fondo.configure(image=imagen_fondo_menu)

def dibujar_nombres():
    etiqueta_user_name.place_configure(x=50,y=67)
    etiqueta_op_name.place_configure(x=845,y=67)
    actualizar_nombres()

def actualizar_nombres():
    etiqueta_user_name.configure(text=juego.nombre_tu)
    etiqueta_op_name.configure(text=juego.nombre_op)

def quitar_nombres():
    etiqueta_user_name.place_configure(x=2000)
    etiqueta_op_name.place_configure(x=2000)



#----------------------------------------------------------codigo------------------------------------#
etiqueta_user_name = Label(ventana,font=fuente_etiquetas_nombres,text=juego.nombre_tu,bg="black",fg="white",anchor="center",height=1,width=20)
etiqueta_op_name = Label(ventana,font=fuente_etiquetas_nombres,text=juego.nombre_op,bg="black",fg="white",anchor="center",height=1,width=20)
veces = Label(ventana,bg="black",fg="white",font="Impact 15",text=f"Tu le ganaste: {puntos.ganadas} veces \n El rival te gano: {puntos.perdidas} veces")

imagen_bvolumen_on = PhotoImage(file="sprites/botones/config/boton_volumen_on.png")
imagen_bvolumen_off = PhotoImage(file="sprites/botones/config/boton_volumen_off.png")

imagen_ganaste_fondo = PhotoImage(file="fondos/fondo_ganaste.png")
imagen_perdiste_fondo = PhotoImage(file="fondos/fondo_perdiste.png")
imagen_fondo1 = PhotoImage(file="fondos/fondo.png")
imagen_fondo2 = PhotoImage(file="fondos/fondov2.png")
imagen_fondo3 = PhotoImage(file="fondos/fondov3.png")
imagen_fondo4 = PhotoImage(file="fondos/fondov4.png")
imagen_fondo5 = PhotoImage(file="fondos/fondov5.png")
imagen_fondo6 = PhotoImage(file="fondos/fondov6.png")
imagen_fondo_menu = PhotoImage(file="fondos/fondo_menu.png")
imagen_fondo_config = PhotoImage(file="fondos/fondo_config.png")
imagen_fondo_estadisticas = PhotoImage(file="fondos/fondo_estadisticas.png")
imagen_fondo_negro = PhotoImage(file="fondos/fondo_negro.png")
#---nada------
imagen_nada_azul = PhotoImage(file = "fondos/nada_azul.png")
imagen_nada_rojo = PhotoImage(file = "fondos/nada_rojo.png")
#---sprites del juego------
imagen_piedra_tu = PhotoImage(file = "Sprites/manos/manos_azul/tu_piedra_azul_spr.png")
imagen_papel_tu = PhotoImage(file = "sprites/manos/manos_azul/tu_papel_azul_spr.png")
imagen_tijera_tu = PhotoImage(file = "sprites/manos/manos_azul/tu_tijera_azul_spr.png")

imagen_piedra_op = PhotoImage(file="sprites/manos/manos_rojo/op_piedra_rojo_spr.png")
imagen_papel_op = PhotoImage(file="sprites/manos/manos_rojo/op_papel_rojo_spr.png")
imagen_tijera_op = PhotoImage(file="sprites/manos/manos_rojo/op_tijera_rojo_spr.png")

#crea una etiqueta en el fondo
eleccion_tu = Label(ventana,borderwidth=0,image=imagen_nada_azul)
eleccion_tu.place(x=133,y=207)

eleccion_op = Label(ventana,borderwidth=0,image=imagen_nada_rojo)
eleccion_op.place(x=756,y=207)

cargar_menu() #-----------> aca empieza el juego
ventana.mainloop()