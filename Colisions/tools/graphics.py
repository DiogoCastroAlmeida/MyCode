# import pygame
import time
# import pygame
class Graph():
    def __init__(self, initial_velocity:list, final_velocity:list):
        global pygame
        import pygame
        self.initial_velocity = initial_velocity
        self.final_velocity = final_velocity
        # this variable is here so that we can decide if we use the initial velocity values or the final velocity values
        self.initial = True
        self.COLORS = {
            "white": (255, 255, 255),
            "black": (0,0,0)
        }
        self.ball_radius = 50
        self.RESOLUTION = (1000, 700)
        self.win = pygame.display.set_mode(self.RESOLUTION)
        self.ball1_position = [self.ball_radius, self.RESOLUTION[1]/2]
        self.ball2_position = [self.RESOLUTION[0]-self.ball_radius, self.RESOLUTION[1]/2]
        pygame.init()
    
    
    def set_background_color(self):
        self.win.fill(self.COLORS["white"])
    
    def set_velocity_values(self, values):
        self.velocity1 = values[0]
        self.velocity2 = values[1]

    def check_if_balls_have_touched(self):
        if round(self.ball2_position[0], 20) - round(self.ball1_position[0], 20) < self.ball_radius*2:
            self.initial = False

    def update_balls_position(self):
        # this variable is here so that we can decide if we use the initial velocity values or the final velocity values
        #self.initial = True
        if self.initial == True:
            self.set_velocity_values(self.initial_velocity)
            self.ball1_position[0] += self.velocity1
            self.ball2_position[0] += self.velocity2
            self.check_if_balls_have_touched()

        else:
            self.set_velocity_values(self.final_velocity)
            self.ball1_position[0] += self.velocity1
            self.ball2_position[0] += self.velocity2

            

    
    def draw_balls(self):
        balls_color = self.COLORS["black"]
        ball_radius = 50
        pygame.draw.circle(self.win, balls_color, self.ball1_position, ball_radius)
        pygame.draw.circle(self.win, balls_color, self.ball2_position, ball_radius)
        self.update_balls_position()


    
    def game_loop(self):
        running = True
        while running:
            time.sleep(0.01)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            self.set_background_color()
            self.draw_balls()
            pygame.display.update()
            #print(self.initial)
            #print(self.velocity1)
            #print(self.velocity2)




#gg = Graph((1, -2), (-0.3, -0.3))
#gg.game_loop()


