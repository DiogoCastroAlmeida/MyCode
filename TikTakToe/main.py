import building_blocks as bb
import ai
import utils


class Config ():
    #an abject of this class will be pickled so that the configuration options remain the same
    def __init__(self):
        self.players = []
        self.command_history = []
        self.commands = {
            "ls": self.list_players,
            "create": self.create_player,
            "del": self.remove_player,
            "help": self.helpe,
            "clean": self.clean_config,
        }
    
    def __str__(self):
        #for debugging purposes
        return "baFAebf"

    def prompt(self):
        while True:
            self.user_input = input("Enter command: ").lower()
            if self.user_input == "exit":
                break
            else:
                self.execute_command()

    def execute_command(self):
        if self.user_input in self.commands.keys():
            self.commands[self.user_input]()
        else:
            print("[ERROR] Command not found.")
        

    def create_player(self):
        name = input("""Creting new player
    Enter Player name: """)
        self.players.append(bb.Player(name))

    def list_players(self):
        for player in self.players:
            print(player)

    def remove_player(self):
        self.list_players()
        player_id = int(input("Enter player ID:"))
        for player in self.players:
            if player.id ==player_id:
                self.players.remove(player)
                print("Player Deleted")
                break
        else:
            print("[ERROR] player not found.")
        
    
    def helpe(self):
        help_page=\
f"""Help Page for configuring this programm:
Commands:
        {list(self.commands.keys())[0]} - list players
        {list(self.commands.keys())[1]} - create players
        {list(self.commands.keys())[2]} - delete players
        {list(self.commands.keys())[3]} - show help page

    """
        print(help_page)
    
    def clean_config(self):
        pass


class LoadConfig():

    def __init__(self):
        self.PATH = r"d:\\repos\\mypython\\TikTakToe\\config.pi"
    
    def load(self):
        if utils.file_exits(self.PATH):
            self.config = utils.unpicklle(self.PATH)
        else:
            self.config = Config()
    
    def save(self):
        utils.picklle(self.PATH, self.config)
    
    def start_config_prompt(self):
        self.config.prompt()
        


configuration = LoadConfig()
configuration.load()
configuration.start_config_prompt()