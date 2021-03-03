import  tkinter as tk
import tools.graphics as graphics
import tools.colisions as colisions
import threading

class Menu():

    def __init__(self):
        self.game_threads = []
        self.gui()
    
    def put_final_velocity_values(self):
        tk.Label(self.root, text=f"Final velocity 1: {self.result[0]}").grid(row=5, column=0)
        tk.Label(self.root, text=f"Final velocity 2: {self.result[1]}").grid(row=5, column=1)

    
    def elastic(self):
        interactor1 = colisions.Colision.Interactor(float(self.mass1.get()), float(self.initial_velocity1.get()))
        interactor2 = colisions.Colision.Interactor(float(self.mass2.get()), float(self.initial_velocity2.get()))
        c = colisions.ElasticColision(interactor1, interactor2)
        self.result = c.calculate()
        self.put_final_velocity_values()
        self.game_threads.append(threading.Thread(target=self.graph_colision))
        self.game_threads[-1].start()
        # print(len(self.game_threads))

    def inelastic(self):
        interactor1 = colisions.Colision.Interactor(float(self.mass1.get()), float(self.initial_velocity1.get()))
        interactor2 = colisions.Colision.Interactor(float(self.mass2.get()), float(self.initial_velocity2.get()))
        c = colisions.InelasticColision(interactor1, interactor2)
        self.result = c.calculate()
        self.put_final_velocity_values()
        self.game_threads.append(threading.Thread(target=self.graph_colision))
        self.game_threads[-1].start()
    
    def graph_colision(self):
        game = graphics.Graph([float(self.initial_velocity1.get()), float(self.initial_velocity2.get())], self.result)
        game.game_loop()
    
    def gui(self):
        self.root = tk.Tk()
        self.root.title("Collisions simulator")
        ###LABELS FOR MASS AND INITIAL VELOCITY###
        tk.Label(self.root, text="Mass 1:").grid(row=0, column=0)
        tk.Label(self.root, text="Mass 2:").grid(row=1, column=0)
        tk.Label(self.root, text="Initial velocity 1:").grid(row=2, column=0)
        tk.Label(self.root, text="Initial velocity 2:").grid(row=3, column=0)
        ###ENTRIES FOR MASS AND INITIAL VELOCITY###
        self.mass1 = tk.Entry(self.root)
        self.mass2 = tk.Entry(self.root)
        self.initial_velocity1 = tk.Entry(self.root)
        self.initial_velocity2 = tk.Entry(self.root)

        self.mass1.grid(row=0, column=1)
        self.mass2.grid(row=1, column=1)
        self.initial_velocity1.grid(row=2, column=1)
        self.initial_velocity2.grid(row=3, column=1)

        ###BUTTONS###
        tk.Button(self.root, command=self.elastic, text="Elastic").grid(row=4, column=0)
        tk.Button(self.root, command=self.inelastic, text="Inelastic").grid(row=4, column=1)


        
        

        self.root.mainloop()




menu = Menu()