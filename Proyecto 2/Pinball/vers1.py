from tkinter import *
from tkinter import Tk, PhotoImage, Checkbutton, IntVar, DISABLED, NORMAL
import time
import pygame




def ventana_principal():
    window = Tk()
    window.minsize(height=800, width=600)
    window.title("Ventana Principal")
    window.configure(bg="#e1e6f2", cursor='hand2')

    # Add background music
    def play_music():
        pygame.mixer.init()
        pygame.mixer.music.load("bg_music.mp3")
        pygame.mixer.music.play()  # Play the music once
        
        window.after(10000, pygame.mixer.music.stop)

    play_music()
    bg_image = PhotoImage(file="BG.png")
    bg_label = Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image 

    titulo = Label(window, text="PINBALL", font=("Courier", 75), fg='black', bg="#e1e6f2")
    titulo.place(x=140, y=5)

    # Estética de los botones
    boton_preliminar = Button(window, text="Preliminar juego", width=20, height=3, fg='black', font=("Courier", 16), borderwidth=5,command=lambda: preliminar_juego(window))
    boton_preliminar.place(relx=0.5, y=250, anchor=CENTER)

    boton_configurations = Button(window, text='Configuración Inicial', width=25, height=3, fg='black', font=("Courier", 16), borderwidth=5, command=lambda: ventana_configuracion(window))
    boton_configurations.place(relx=0.5, y=390, anchor=CENTER)

    boton_about = Button(window, text='About', width=20, height=3, fg='black', font=("Courier", 16), borderwidth=5, command=lambda: ventana_about(window))
    boton_about.place(relx=0.5, y=530, anchor=CENTER)

    botones = [boton_about, boton_configurations, boton_preliminar]
    for boton in botones:
        boton['border'] = '2' 
        boton['relief'] = 'raised'  
        boton['bg'] = '#d3d3d3'  
        boton['activebackground'] = '#a9a9a9'  # Dark gray when pressed
    
    window.mainloop()
    

def regresar(window):
    window.destroy()
    ventana_principal()
#############################################################################################

def ventana_about(window):
    window.destroy()
    window = Tk()
    window.configure(bg="#faf5e8", cursor='hand2')
    window.geometry("600x800")
    window.title("About")

    bg_image = PhotoImage(file="BG1.png")
    bg_label = Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image 

    about_text = Label(window, text="Información sobre Autora", font=("Courier", 24), fg='white', bg="#9467fe")
    about_text.pack(pady=20)
    
    info_text = """ 
Universidad Tecnológico de Costa Rica
Ingeniería en Computadores
Materia: Fundamentos de Sistemas
Computacionales
Profesor: Luis Alberto Chavarría Zamora
2024
Made in Costa Rica
Versión 4

Paola Barquero Morales       
2024801145                     
    """

    info_label = Label(window, text=info_text, font=("Courier", 16), fg='white', bg="#9467fe", wraplength=500, justify=CENTER)
    info_label.pack(pady=10)

    image = PhotoImage(file="au0.png")
    image = image.subsample(2, 2)  
    image_label = Label(window, image=image, bg="#e1e6f2")
    image_label.image = image
    

    boton_return = Button(window, text="Return", width=15, height=3, fg='black', font=("Courier", 16), borderwidth=5, command=lambda: regresar(window))
    boton_return.place(x=400, y=700)


    window.mainloop()

##########################################################################################################
def ventana_configuracion(window):
    window.destroy()
    window = Tk()
    window.configure(bg="#faf5e8", cursor='hand2')
    window.geometry("600x800")
    
    window.title("Configuración Inicial")
    bg_image = PhotoImage(file="BG1.png")
    bg_label = Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image 
    profile_label = Label(window, text="Select Profile", font=("Courier", 30), fg='#f2eadc', bg="#9467fe")
    profile_label.place(x=150, y=20)

    boton_return = Button(window, text="Return", width=15, height=3, fg='black', font=("Courier", 16), borderwidth=5, command=lambda: regresar(window))
    boton_return.place(x=400, y=700)

    profile1_image = PhotoImage(file="Prof1.png")
    profile2_image = PhotoImage(file="Prof2.png")
    profile1_image = profile1_image.subsample(2, 2)
    profile2_image = profile2_image.subsample(2, 2)

    profile1_label = Label(window, text="Profile 1", font=("Courier", 20), fg='#f2eadc', bg="#9467fe")
    profile1_label.place(x=250, y=150)
    boton_profile1 = Button(window, image=profile1_image, width=150, height=150, command=lambda: profile1(window))
    boton_profile1.image = profile1_image
    boton_profile1.place(x=225, y=200)

    profile2_label = Label(window, text="Profile 2", font=("Courier", 20), fg='#f2eadc', bg="#9467fe")
    profile2_label.place(x=250, y=410)
    boton_profile2 = Button(window, image=profile2_image, width=150, height=150, command=lambda: profile2(window))
    boton_profile2.image = profile2_image
    boton_profile2.place(x=225, y=450)
#############################################################################################

def mostrar_estadisticas(window, jugadores):
 
    window.destroy()
    stats_window = Tk()
    stats_window.title("Estadísticas del Juego")
    stats_window.geometry("400x600")
    stats_window.configure(bg="#faf5e8")

    Label(stats_window, text="Estadísticas del Juego", font=("Courier", 24), bg="#faf5e8").pack(pady=20)

    for jugador in jugadores:
        Label(stats_window, text=f"Jugador: {jugador['nombre']}", font=("Courier", 18), bg="#faf5e8").pack(pady=10)
        Label(stats_window, text=f"Puntuación: {jugador['puntuacion']}", font=("Courier", 16), bg="#faf5e8").pack()
        Label(stats_window, text=f"Tiempo Jugado: {jugador['tiempo']} minutos", font=("Courier", 16), bg="#faf5e8").pack()
        Label(stats_window, text=f"Disparos Restantes: {jugador['disparos']}", font=("Courier", 16), bg="#faf5e8").pack()
        Label(stats_window, text="-----------------------------", bg="#faf5e8").pack()

    Button(stats_window, text="Cerrar", font=("Courier", 16), command=stats_window.destroy).pack(pady=20)

    stats_window.mainloop()
#############################################################################################

def profile1(window):
    window.destroy()
    window = Tk()
    window.configure(bg="#faf5e8", cursor='hand2')
    window.geometry("600x800")
    window.title("Profile 1")  
    print("Profile 1 selected")

    bg_image = PhotoImage(file="BG1.png")
    bg_label = Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image 

    boton_return = Button(window, text="Return", width=15, height=3, fg='black', font=("Courier", 16), borderwidth=5, command=lambda: ventana_configuracion(window))
    boton_return.place(x=400, y=700)
    
    profile1_image = PhotoImage(file="c2.png")
    profile2_image = PhotoImage(file="c1.png")
    profile1_image = profile1_image.subsample(2, 2)
    profile2_image = profile2_image.subsample(6, 6)

    profile1_label = Label(window, text="SINGLE PLAYER", font=("Courier", 20), fg='#f2eadc', bg="#9467fe")   
    profile1_label.place(x=220, y=150)
    boton_profile1 = Button(window, image=profile1_image, width=150, height=150, command=lambda: single_player(window))
    boton_profile1.image = profile1_image
    boton_profile1.place(x=225, y=200)
    
    profile2_label = Label(window, text="MULTIPLAYER", font=("Courier", 20), fg='#f2eadc', bg="#9467fe")
    profile2_label.place(x=230, y=410)
    boton_profile2 = Button(window, image=profile2_image, width=150, height=150, command=lambda: multiplayer(window))
    boton_profile2.image = profile2_image
    boton_profile2.place(x=225, y=450)

#############################################################################################

def single_player(window):
    window.destroy()
    window = Tk()
    window.configure(bg="#faf5e8", cursor='hand2')
    window.geometry("600x800")
    window.title("Single Player")  
    
    boton_return = Button(window, text="Return", width=15, height=3, fg='black', font=("Courier", 16), borderwidth=5, command=lambda: profile1(window))
    boton_return.place(x=400, y=700)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()

    image1 = PhotoImage(file="p1.png")
    image2 = PhotoImage(file="p2.png")
    image3 = PhotoImage(file="p3.png")
    image1 = image1.subsample(3, 3)
    image2 = image2.subsample(3, 3)
    image3 = image3.subsample(3, 3)

    # Función para limitar la selección a un solo checkbox
    def limit_checkboxes():
        selected = var1.get() + var2.get() + var3.get()
        if selected >= 1:
            if not var1.get():
                checkbox_jug1.config(state=DISABLED)
            if not var2.get():
                checkbox_jug2.config(state=DISABLED)
            if not var3.get():
                checkbox_jug3.config(state=DISABLED)
        else:
            checkbox_jug1.config(state=NORMAL)
            checkbox_jug2.config(state=NORMAL)
            checkbox_jug3.config(state=NORMAL)

    # Trace de cambios en los checkboxes
    var1.trace_add("write", limit_checkboxes)
    var2.trace_add("write", limit_checkboxes)
    var3.trace_add("write", limit_checkboxes)
    
    # Crear los checkboxes con imágenes
    checkbox_jug1 = Checkbutton(window, image=image1, variable=var1, onvalue=1, offvalue=0, indicatoron=False, width=150, height=150)
    checkbox_jug1.image = image1
    checkbox_jug1.place(x=225, y=100)

    # Entrada para el nombre del Jugador 1
    entry_jug1 = Entry(window, font=("Courier", 16), justify='center')
    entry_jug1.place(x=225, y=260)

    checkbox_jug2 = Checkbutton(window, image=image2, variable=var2, onvalue=1, offvalue=0, indicatoron=False, width=150, height=150)
    checkbox_jug2.image = image2
    checkbox_jug2.place(x=225, y=300)

    # Entrada para el nombre del Jugador 2
    entry_jug2 = Entry(window, font=("Courier", 16), justify='center')
    entry_jug2.place(x=225, y=460)

    checkbox_jug3 = Checkbutton(window, image=image3, variable=var3, onvalue=1, offvalue=0, indicatoron=False, width=150, height=150)
    checkbox_jug3.image = image3
    checkbox_jug3.place(x=225, y=500)

    # Entrada para el nombre del Jugador 3
    entry_jug3 = Entry(window, font=("Courier", 16), justify='center')
    entry_jug3.place(x=225, y=660)

    # Función para verificar si exactamente 1 jugador está seleccionado y empezar el juego
    def check_start_game():
        selected_name = ""
        selected_image = None
        
        if var1.get() == 1:
            selected_name = entry_jug1.get()
            selected_image = image1
        elif var2.get() == 1:
            selected_name = entry_jug2.get()
            selected_image = image2
        elif var3.get() == 1:
            selected_name = entry_jug3.get()
            selected_image = image3
        
        if selected_name and selected_image:
            game_single_player(window, selected_name, selected_image)

    # Trace de cambios en los checkboxes para empezar el juego
    var1.trace_add("write", check_start_game)
    var2.trace_add("write", check_start_game)
    var3.trace_add("write", check_start_game)
    

#############################################################################################   

def game_single_player(window, player_name):
    game_ended = False
    # Destroy the previous window and create a new one
    window.destroy()
    window = Tk()
    window.configure(bg="#faf5e8", cursor='hand2')
    window.geometry("600x800")
    window.title("Game")
  
    bg_image = PhotoImage(file="BG.png")
    bg_label = Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image

    # Display the player's name in the upper right corner
    Label(window, text=player_name, font=("Courier", 25), fg='black', bg="#faf5e8").place(x=450, y=230)

    # Create a label to display the timer
    timer_label = Label(window, text="00:00", font=("Courier", 24), fg='black', bg="#faf5e8")
    timer_label.place(x=250, y=50)

    game_ended = False  # Track whether the game has ended

    # Function to update the timer
    def update_timer(start_time):
        if not game_ended:
            elapsed_time = int(time.time() - start_time)
            minutes = elapsed_time // 60
            seconds = elapsed_time % 60
            timer_label.config(text=f"{minutes:02}:{seconds:02}")
            window.after(1000, update_timer, start_time)

    # Start the timer
    start_time = time.time()
    update_timer(start_time)

    # Make the timer label larger
    timer_label.config(font=("Courier", 48))
    timer_label.place(x=230, y=30)

    # Function to end the game when shots are exhausted
    def end_game():
        nonlocal game_ended
        game_ended = True
        window.destroy()
        ventana_principal()

    # Create a label to display the score
    score_label = Label(window, text="Score: 0", font=("Courier", 25), fg='black', bg="#faf5e8")
    score_label.place(x=100, y=300)

    # Initialize score
    score = 0

    # Function to update the score
    def update_score(points):
        nonlocal score
        score += points  # Increment the score by the given points
        score_label.config(text=f"Score: {score}")
        
    # Define functions to update score for different zones
    def score_zone_1(): pass

    def score_zone_1():
        update_score(50)

    def score_zone_2():
        update_score(10)

    def score_zone_3():
        update_score(5)

    def score_zone_4():
        update_score(30)
    
    def score_zone_5():
        update_score(20)


    # Track the player's shots
    shots_label = Label(window, text="Shots: 3", font=("Courier", 25), fg='black', bg="#faf5e8")
    shots_label.place(x=100, y=250)
    shots_remaining = 3

    # Function to handle losing a shot
    def lose_shot():
        nonlocal shots_remaining
        if shots_remaining > 0:
            shots_remaining -= 1
            shots_label.config(text=f"Shots: {shots_remaining}")
            if shots_remaining == 0:
                end_game()

    # Function to check if the ball has not scored in 15 seconds
    def check_no_score():
        if not game_ended:
            lose_shot()
            window.after(15000, check_no_score)

    # Start checking for no score after 15 seconds
    window.after(15000, check_no_score)

    # Function to display game statistics
    def show_statistics():
        stats_window = Tk()
        stats_window.title("Estadísticas del Juego")
        stats_window.geometry("600x600")
        stats_window.configure(bg="#faf5e8")

        Label(stats_window, text="Estadísticas del Juego", font=("Courier", 24), bg="#faf5e8").pack(pady=20)
        Label(stats_window, text=f"Jugador: {player_name}", font=("Courier", 18), bg="#faf5e8").pack(pady=10)
        Label(stats_window, text=f"Puntuación: {score}", font=("Courier", 16), bg="#faf5e8").pack()
        elapsed_time = int(time.time() - start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        Label(stats_window, text=f"Tiempo Jugado: {minutes} minutos {seconds} segundos", font=("Courier", 16), bg="#faf5e8").pack()
        Label(stats_window, text=f"Disparos Restantes: {shots_remaining}", font=("Courier", 16), bg="#faf5e8").pack()
        Label(stats_window, text="-----------------------------", bg="#faf5e8").pack()

        Button(stats_window, text="Cerrar", font=("Courier", 16), command=stats_window.destroy).pack(pady=20)

        stats_window.mainloop()

    # Modify end_game function to show statistics
    def end_game():
        nonlocal game_ended
        game_ended = True
        window.destroy()
        show_statistics()

    window.mainloop()

#############################################################################################
def multiplayer(window):
    window.destroy()
    window = Tk()
    window.configure(bg="pink", cursor='hand2')
    window.geometry("600x800")
    window.title("Multiplayer")  
    print("Multiplayer selected")
  
    bg_image = PhotoImage(file="BG1.png")
    bg_label = Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image 

    # Label for selecting game mode
    mode_label = Label(window, text="Select Game Mode", font=("Courier", 20), fg='#f2eadc', bg="#9467fe")
    mode_label.place(x=180, y=20)

    # Variable to store the game mode
    game_mode = IntVar(value=1)  # Default to manual mode

    # Radio buttons for selecting game mode
    manual_mode = Radiobutton(window, text="Manual", variable=game_mode, value=1, font=("Courier", 16), fg='black', bg="#faf5e8")
    manual_mode.place(x=200, y=60)


    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()

    image1 = PhotoImage(file="p1.png")
    image2 = PhotoImage(file="p2.png")
    image3 = PhotoImage(file="p3.png")
    image1 = image1.subsample(3, 3)
    image2 = image2.subsample(3, 3)
    image3 = image3.subsample(3, 3)

    # Function to limit the number of selected checkboxes to 2
    def limit_checkboxes(*args):
        selected = var1.get() + var2.get() + var3.get()
        if selected >= 2:
            if not var1.get():
                checkbox_jug1.config(state=DISABLED)
            if not var2.get():
                checkbox_jug2.config(state=DISABLED)
            if not var3.get():
                checkbox_jug3.config(state=DISABLED)
        else:
            checkbox_jug1.config(state=NORMAL)
            checkbox_jug2.config(state=NORMAL)
            checkbox_jug3.config(state=NORMAL)

    # Trace changes in checkbox variables
    var1.trace_add("write", limit_checkboxes)
    var2.trace_add("write", limit_checkboxes)
    var3.trace_add("write", limit_checkboxes)
    
    # Create checkboxes with images
    checkbox_jug1 = Checkbutton(window, image=image1, variable=var1, onvalue=1, offvalue=0, indicatoron=False, width=150, height=150)
    checkbox_jug1.image = image1
    checkbox_jug1.place(x=225, y=100)

    # Entry for Player 1 name
    entry_jug1 = Entry(window, font=("Courier", 16), justify='center')
    entry_jug1.place(x=225, y=260)

    checkbox_jug2 = Checkbutton(window, image=image2, variable=var2, onvalue=1, offvalue=0, indicatoron=False, width=150, height=150)
    checkbox_jug2.image = image2
    checkbox_jug2.place(x=225, y=300)

    # Entry for Player 2 name
    entry_jug2 = Entry(window, font=("Courier", 16), justify='center')
    entry_jug2.place(x=225, y=460)

    checkbox_jug3 = Checkbutton(window, image=image3, variable=var3, onvalue=1, offvalue=0, indicatoron=False, width=150, height=150)
    checkbox_jug3.image = image3
    checkbox_jug3.place(x=225, y=500)

    # Entry for Player 3 name
    entry_jug3 = Entry(window, font=("Courier", 16), justify='center')
    entry_jug3.place(x=225, y=660)

    # Function to check if exactly 2 players are selected and start the game
    def check_start_game(*args):
        if var1.get() + var2.get() + var3.get() == 2:
            ventana_juegomulti2(window)

    # Trace changes in checkbox variables to start the game
    var1.trace_add("write", check_start_game)
    var2.trace_add("write", check_start_game)
    var3.trace_add("write", check_start_game)

    boton_return = Button(window, text="Return", width=15, height=3, fg='black', font=("Courier", 16), borderwidth=5, command=lambda: ventana_configuracion(window))
    boton_return.place(x=400, y=700)

    window.mainloop()


#############################################################################################

import time  # Ensure the time module is imported

def game_multiplayer(window, player_names):
    # Destroy the previous window and create a new one
    window.destroy()
    window = Tk()
    window.configure(bg="#faf5e8", cursor='hand2')
    window.geometry("600x800")
    window.title("Game")
  
    # Background image for the window
    bg_image = PhotoImage(file="BG.png")
    bg_label = Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image

    # Display the players' names in the upper right corner
    Label(window, text=player_names[0], font=("Courier", 25), fg='black', bg="#faf5e8").place(x=450, y=230)
    Label(window, text=player_names[1], font=("Courier", 25), fg='black', bg="#faf5e8").place(x=450, y=270)

    # Create a label to display the timer
    timer_label = Label(window, text="00:00", font=("Courier", 24), fg='black', bg="#faf5e8")
    timer_label.place(x=250, y=50)

    # Track whether the game has ended
    game_ended = False

    # Function to update the timer
    def update_timer(start_time):
        if not game_ended:
            elapsed_time = int(time.time() - start_time)
            minutes = elapsed_time // 60
            seconds = elapsed_time % 60
            timer_label.config(text=f"{minutes:02}:{seconds:02}")
            window.after(1000, update_timer, start_time)

    # Start the timer
    start_time = time.time()
    update_timer(start_time)

    # Make the timer label larger
    timer_label.config(font=("Courier", 48))
    timer_label.place(x=230, y=30)

    # Function to end the game when shots are exhausted
    def end_game():
        nonlocal game_ended
        game_ended = True
        print("Game Over!")
        window.destroy()
        ventana_principal()  # Make sure this function is correctly defined and doesn't interfere with the game window.

    # Create labels to display the scores for both players
    score_labels = [
        Label(window, text="Score: 0", font=("Courier", 25), fg='black', bg="#faf5e8"),
        Label(window, text="Score: 0", font=("Courier", 25), fg='black', bg="#faf5e8")
    ]
    score_labels[0].place(x=100, y=300)
    score_labels[1].place(x=100, y=350)

    # Initialize scores for both players
    scores = [0, 0]

    # Function to update the score for a player
    def update_score(player_index, points):
        scores[player_index] += points  # Increment the score by the given points
        score_labels[player_index].config(text=f"Score: {scores[player_index]}")
        

    # Track the players' shots
    shots_labels = [
        Label(window, text="Shots: 3", font=("Courier", 25), fg='black', bg="#faf5e8"),
        Label(window, text="Shots: 3", font=("Courier", 25), fg='black', bg="#faf5e8")
    ]
    shots_labels[0].place(x=100, y=250)
    shots_labels[1].place(x=100, y=400)
    shots_remaining = [3, 3]

    # Function to handle losing a shot for a player
    def lose_shot(player_index):
        if shots_remaining[player_index] > 0:
            shots_remaining[player_index] -= 1
            shots_labels[player_index].config(text=f"Shots: {shots_remaining[player_index]}")
            if shots_remaining[player_index] == 0:
                end_game()

    # Function to check if the ball has not scored in 15 seconds for both players
    def check_no_score():
        if not game_ended:
            lose_shot(0)
            lose_shot(1)
            window.after(15000, check_no_score)

    # Start checking for no score after 15 seconds
    window.after(15000, check_no_score)

    # Ensure the window keeps refreshing with the mainloop
    window.mainloop()

#############################################################################################

def profile2(window):
    window.destroy()
    window = Tk()
    window.configure(bg="#faf5e8", cursor='hand2')
    window.geometry("600x800")
    window.title("Profile 2")  
    print("Profile 2 selected")

    bg_image = PhotoImage(file="BG1.png")
    bg_label = Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image 
    
    
    boton_return = Button(window, text="Return", width=15, height=3, fg='black', font=("Courier", 16), borderwidth=5, command=lambda: ventana_configuracion(window))
    boton_return.place(x=400, y=700)

    profile1_image = PhotoImage(file="c2.png")
    profile2_image = PhotoImage(file="c1.png")
    profile1_image = profile1_image.subsample(2, 2)
    profile2_image = profile2_image.subsample(6, 6)

    profile1_label = Label(window, text="SINGLE PLAYER", font=("Courier", 20), fg='#f2eadc', bg="#9467fe")   
    profile1_label.place(x=220, y=150)
    boton_profile1 = Button(window, image=profile1_image, width=150, height=150, command=lambda: single_player2(window))
    boton_profile1.image = profile1_image
    boton_profile1.place(x=225, y=200)
    
    profile2_label = Label(window, text="MULTIPLAYER", font=("Courier", 20), fg='#f2eadc', bg="#9467fe")
    profile2_label.place(x=230, y=410)
    boton_profile2 = Button(window, image=profile2_image, width=150, height=150, command=lambda: multiplayer2(window))
    boton_profile2.image = profile2_image
    boton_profile2.place(x=225, y=450)

    window.mainloop()

#############################################################################################

def single_player2(window):
    window.destroy()
    window = Tk()
    window.configure(bg="#faf5e8", cursor='hand2')
    window.geometry("600x800")
    window.title("Single Player")  
    print("Single Player selected")

    boton_return = Button(window, text="Return", width=15, height=3, fg='black', font=("Courier", 16), borderwidth=5, command=lambda: profile2(window))
    boton_return.place(x=400, y=700)

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()

    image1 = PhotoImage(file="p1.png")
    image2 = PhotoImage(file="p2.png")
    image3 = PhotoImage(file="p3.png")
    image1 = image1.subsample(3, 3)
    image2 = image2.subsample(3, 3)
    image3 = image3.subsample(3, 3)

    # Función para limitar la selección a un solo checkbox
    def limit_checkboxes(*args):
        selected = var1.get() + var2.get() + var3.get()
        if selected >= 1:
            if not var1.get():
                checkbox_jug1.config(state=DISABLED)
            if not var2.get():
                checkbox_jug2.config(state=DISABLED)
            if not var3.get():
                checkbox_jug3.config(state=DISABLED)
        else:
            checkbox_jug1.config(state=NORMAL)
            checkbox_jug2.config(state=NORMAL)
            checkbox_jug3.config(state=NORMAL)

    # Trace de cambios en los checkboxes
    var1.trace_add("write", limit_checkboxes)
    var2.trace_add("write", limit_checkboxes)
    var3.trace_add("write", limit_checkboxes)
    
    # Crear los checkboxes con imágenes
    checkbox_jug1 = Checkbutton(window, image=image1, variable=var1, onvalue=1, offvalue=0, indicatoron=False, width=150, height=150)
    checkbox_jug1.image = image1
    checkbox_jug1.place(x=225, y=100)

    # Entrada para el nombre del Jugador 1
    entry_jug1 = Entry(window, font=("Courier", 16), justify='center')
    entry_jug1.place(x=225, y=260)

    checkbox_jug2 = Checkbutton(window, image=image2, variable=var2, onvalue=1, offvalue=0, indicatoron=False, width=150, height=150)
    checkbox_jug2.image = image2
    checkbox_jug2.place(x=225, y=300)

    # Entrada para el nombre del Jugador 2
    entry_jug2 = Entry(window, font=("Courier", 16), justify='center')
    entry_jug2.place(x=225, y=460)

    checkbox_jug3 = Checkbutton(window, image=image3, variable=var3, onvalue=1, offvalue=0, indicatoron=False, width=150, height=150)
    checkbox_jug3.image = image3
    checkbox_jug3.place(x=225, y=500)

    # Entrada para el nombre del Jugador 3
    entry_jug3 = Entry(window, font=("Courier", 16), justify='center')
    entry_jug3.place(x=225, y=660)

    # Función para verificar si exactamente 1 jugador está seleccionado y empezar el juego
    def check_start_game(*args):
        selected_name = ""
        selected_image = None
        
        if var1.get() == 1:
            selected_name = entry_jug1.get()
            selected_image = image1
        elif var2.get() == 1:
            selected_name = entry_jug2.get()
            selected_image = image2
        elif var3.get() == 1:
            selected_name = entry_jug3.get()
            selected_image = image3
        
        if selected_name and selected_image:
            game_single_player(window, selected_name, selected_image)

    # Trace de cambios en los checkboxes para empezar el juego
    var1.trace_add("write", check_start_game)
    var2.trace_add("write", check_start_game)
    var3.trace_add("write", check_start_game)

#############################################################################################   

def game_single_player2(window, player_name):
    # Destroy the previous window and create a new one
    window.destroy()
    window = Tk()
    window.configure(bg="pink", cursor='hand2')
    window.geometry("600x800")
    window.title("Game")
  
    bg_image = PhotoImage(file="BG.png")
    bg_label = Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image

    # Display the player's name in the upper right corner
    Label(window, text=player_name, font=("Courier", 25), fg='black', bg="#faf5e8").place(x=450, y=230)

    # Create a label to display the timer
    timer_label = Label(window, text="00:00", font=("Courier", 24), fg='black', bg="#faf5e8")
    timer_label.place(x=250, y=50)

    game_ended = False

    # Function to update the timer
    def update_timer(start_time):
        if not game_ended:
            elapsed_time = int(time.time() - start_time)
            minutes = elapsed_time // 60
            seconds = elapsed_time % 60
            timer_label.config(text=f"{minutes:02}:{seconds:02}")
            window.after(1000, update_timer, start_time)

    # Start the timer
    start_time = time.time()
    update_timer(start_time)

    # Make the timer label larger
    timer_label.config(font=("Courier", 48))
    timer_label.place(x=230, y=30)

    # Function to end the game when shots are exhausted
    def end_game():
        nonlocal game_ended
        game_ended = True
        window.destroy()
        ventana_principal()

    # Create a label to display the score
    score_label = Label(window, text="Score: 0", font=("Courier", 25), fg='black', bg="#faf5e8")
    score_label.place(x=100, y=300)

    # Initialize score
    score = 0

    # Function to update the score
    def update_score(points):
        nonlocal score
        score += points  # Increment the score by the given points
        score_label.config(text=f"Score: {score}")
        
    # Define functions to update score for different zones
    def score_zone_1():
        update_score(100)

    def score_zone_2():
        update_score(70)

    def score_zone_3():
        update_score(30)

    def score_zone_4():
        update_score(20)
    
    def score_zone_5():
        update_score(50)


    # Track the player's shots
    shots_label = Label(window, text="Shots: 3", font=("Courier", 25), fg='black', bg="#faf5e8")
    shots_label.place(x=100, y=250)
    shots_remaining = 3

    # Function to handle losing a shot
    def lose_shot():
        nonlocal shots_remaining
        if shots_remaining > 0:
            shots_remaining -= 1
            shots_label.config(text=f"Shots: {shots_remaining}")
            if shots_remaining == 0:
                end_game()

    # Function to check if the ball has not scored in 15 seconds
    def check_no_score():
        if not game_ended:
            lose_shot()
            window.after(15000, check_no_score)

    # Start checking for no score after 15 seconds
    window.after(15000, check_no_score)

    window.mainloop()  
#############################################################################################

def multiplayer2(window):
    window.destroy()
    window = Tk()
    window.configure(bg="pink", cursor='hand2')
    window.geometry("600x800")
    window.title("Multiplayer")  
    print("Multiplayer selected")
  
    bg_image = PhotoImage(file="BG1.png")
    bg_label = Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image 

    # Label for selecting game mode
    mode_label = Label(window, text="Select Game Mode", font=("Courier", 20), fg='#f2eadc', bg="#9467fe")
    mode_label.place(x=180, y=20)

    # Variable to store the game mode
    game_mode = IntVar(value=1)  # Default to manual mode

    # Radio buttons for selecting game mode
    manual_mode = Radiobutton(window, text="Manual", variable=game_mode, value=1, font=("Courier", 16), fg='black', bg="#faf5e8")
    manual_mode.place(x=200, y=60)


    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()

    image1 = PhotoImage(file="p1.png")
    image2 = PhotoImage(file="p2.png")
    image3 = PhotoImage(file="p3.png")
    image1 = image1.subsample(3, 3)
    image2 = image2.subsample(3, 3)
    image3 = image3.subsample(3, 3)

    # Function to limit the number of selected checkboxes to 2
    def limit_checkboxes(*args):
        selected = var1.get() + var2.get() + var3.get()
        if selected >= 2:
            if not var1.get():
                checkbox_jug1.config(state=DISABLED)
            if not var2.get():
                checkbox_jug2.config(state=DISABLED)
            if not var3.get():
                checkbox_jug3.config(state=DISABLED)
        else:
            checkbox_jug1.config(state=NORMAL)
            checkbox_jug2.config(state=NORMAL)
            checkbox_jug3.config(state=NORMAL)

    # Trace changes in checkbox variables
    var1.trace_add("write", limit_checkboxes)
    var2.trace_add("write", limit_checkboxes)
    var3.trace_add("write", limit_checkboxes)
    
    # Create checkboxes with images
    checkbox_jug1 = Checkbutton(window, image=image1, variable=var1, onvalue=1, offvalue=0, indicatoron=False, width=150, height=150)
    checkbox_jug1.image = image1
    checkbox_jug1.place(x=225, y=100)

    # Entry for Player 1 name
    entry_jug1 = Entry(window, font=("Courier", 16), justify='center')
    entry_jug1.place(x=225, y=260)

    checkbox_jug2 = Checkbutton(window, image=image2, variable=var2, onvalue=1, offvalue=0, indicatoron=False, width=150, height=150)
    checkbox_jug2.image = image2
    checkbox_jug2.place(x=225, y=300)

    # Entry for Player 2 name
    entry_jug2 = Entry(window, font=("Courier", 16), justify='center')
    entry_jug2.place(x=225, y=460)

    checkbox_jug3 = Checkbutton(window, image=image3, variable=var3, onvalue=1, offvalue=0, indicatoron=False, width=150, height=150)
    checkbox_jug3.image = image3
    checkbox_jug3.place(x=225, y=500)

    # Entry for Player 3 name
    entry_jug3 = Entry(window, font=("Courier", 16), justify='center')
    entry_jug3.place(x=225, y=660)

    # Function to check if exactly 2 players are selected and start the game
    def check_start_game(*args):
        if var1.get() + var2.get() + var3.get() == 2:
            ventana_juegomulti2(window)

    # Trace changes in checkbox variables to start the game
    var1.trace_add("write", check_start_game)
    var2.trace_add("write", check_start_game)
    var3.trace_add("write", check_start_game)

    boton_return = Button(window, text="Return", width=15, height=3, fg='black', font=("Courier", 16), borderwidth=5, command=lambda: ventana_configuracion(window))
    boton_return.place(x=400, y=700)

    window.mainloop()

#############################################################################################

def ventana_juegomulti2(window):
    window.destroy()
    window = Tk()
    window.configure(bg="pink", cursor='hand2')
    window.geometry("600x800")
    window.title("Juego Multiplayer")  



    window.mainloop()

#############################################################################################

def preliminar_juego(window):
    window.destroy()
    window = Tk()
    window.configure(bg="pink", cursor='hand2')
    window.geometry("600x800")
    window.title("Preliminar juego")

    bg_image = PhotoImage(file="BG1.png")
    bg_label = Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image

    boton_return = Button(window, text="Return", width=15, height=3, fg='black', font=("Courier", 16), borderwidth=5, command=lambda: regresar(window))
    boton_return.place(x=400, y=700)
    preliminar_text = Label(window, text="Preliminar del Juego", font=("Courier", 24), fg='white', bg="#9467fe")
    preliminar_text.pack(pady=20)
    
    info_text = """ 
El proyecto tiene como objetivo crear un juego de Pinball que integre tanto software como hardware. Utilizando Python, Tkinter y Thonny para la interfaz gráfica, junto con una Raspberry Pi Pico W para realizar la interacción con el hardware.  
Se ha elaborado un tablero en el cual los jugadores manejan una bolincha metálica que se desplaza por el tablero hasta llegar con alguna zona de anotación.
Cada zona de anotacion funciona como un sensor que simula el cierre de un circuito cuando la bolincha lo activa, registrando puntos y generando eventos en el juego.
    """

    info_label = Label(window, text=info_text, font=("Courier", 16), fg='white', bg="#9467fe", wraplength=500, justify=LEFT)
    info_label.pack(pady=10)
    window.mainloop()


#############################################################################################


ventana_principal()

