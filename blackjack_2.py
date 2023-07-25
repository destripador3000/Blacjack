
import tkinter as tk
from tkinter import messagebox
from random import choice

ventana = tk.Tk()
ventana.configure(bg="green")
ventana.title("Blackjack")
ventana.geometry("600x400")


palos = ['♠', '♡', '♢', '♣']
rangos = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
mazo = [(rango, palo) for palo in palos for rango in rangos]

mano_jugador = []
valor_jugador = 0

def calcular_valor_mano(mano):
    valor_total = 0
    numero_ases = 0

    for carta in mano:
        rango = carta[0]
        if rango in ['J', 'Q', 'K']:
            valor_total += 10
        elif rango == 'A':
            valor_total += 11
            numero_ases += 1
        else:
            valor_total += int(rango)

    while valor_total > 21 and numero_ases > 0:
        valor_total -= 10
        numero_ases -= 1

    return valor_total

def nuevo_juego():
    global mano_jugador, valor_jugador
    mano_jugador = []
    mano_crupier = []

    mano_jugador.append(choice(mazo))
    mano_crupier.append(choice(mazo))

    valor_jugador = calcular_valor_mano(mano_jugador)
    valor_crupier = calcular_valor_mano(mano_crupier)

    cartas_jugador = ", ".join([f"{carta[0]}{carta[1]}" for carta in mano_jugador])
    jugador_label.config(text=f"Jugador: {cartas_jugador} (Valor: {valor_jugador})")
    crupier_label.config(text=f"Crupier: {mano_crupier[0][0]}{mano_crupier[0][1]} (Valor: ?)")

    pedir_carta_button.config(state=tk.NORMAL)
    plantarse_button.config(state=tk.NORMAL)

def pedir_carta():
    global mano_jugador, valor_jugador
    nueva_carta = choice(mazo)
    mano_jugador.append(nueva_carta)
    valor_jugador = calcular_valor_mano(mano_jugador)
    cartas_jugador = ", ".join([f"{carta[0]}{carta[1]}" for carta in mano_jugador])
    jugador_label.config(text=f"Jugador: {cartas_jugador} (Valor: {valor_jugador})")

    if valor_jugador > 21:
        fin_juego("¡Te has pasado de 21! Has perdido.")

def plantarse():
    mano_crupier = []
    mano_crupier.append(crupier_label.cget("text").split()[1])
    valor_crupier = calcular_valor_mano(mano_crupier)

    while valor_crupier < 17:
        nueva_carta = choice(mazo)
        mano_crupier.append(nueva_carta)
        valor_crupier = calcular_valor_mano(mano_crupier)

    cartas_crupier = ", ".join([f"{carta[0]}{carta[1]}" for carta in mano_crupier])
    crupier_label.config(text=f"Crupier: {cartas_crupier} (Valor: {valor_crupier})")

    if valor_crupier > 21 or valor_crupier < valor_jugador:
        fin_juego("¡Has ganado!")
    elif valor_crupier == valor_jugador:
        fin_juego("Se reparten las ganancias entre la casa y el jugador")
    else:
        fin_juego("Ha ganado el crupier")    

def fin_juego(mensaje):
    pedir_carta_button.config(state=tk.DISABLED)
    plantarse_button.config(state=tk.DISABLED)
    messagebox.showinfo("Fin del juego", mensaje)

jugador_label = tk.Label(ventana, text="Jugador: ", font=("Sans Serif", 15))
jugador_label.pack()

crupier_label = tk.Label(ventana, text="Crupier: ", font=("Sans Serif", 15))
crupier_label.pack()

pedir_carta_button = tk.Button(ventana, text="Pedir carta", command=pedir_carta, state=tk.DISABLED, font=("Sans Serif", 15))
pedir_carta_button.pack()

plantarse_button = tk.Button(ventana, text="Plantarse", command=plantarse, state=tk.DISABLED, font=("Sans Serif", 15))
plantarse_button.pack()

nuevo_juego_button = tk.Button(ventana, text="Nuevo Juego", fg="red", command=nuevo_juego, font=("Sans Serif", 15))
nuevo_juego_button.pack()

titulo = tk.Label(ventana, text="BLACKJACK", font=("Georgia", 30), bg="green")
titulo.pack()

palos_label = tk.Label(ventana, text="♠ ♡ ♢ ♣", font=("Georgia", 30), bg="green")
palos_label.pack()

ventana.mainloop()
