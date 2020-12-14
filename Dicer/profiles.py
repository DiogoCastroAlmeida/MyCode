import dice_simulator
import pickling_operation as picklle



class Profile():
    profiles_file_name = r"Dicer\profiles.pickle"


    @classmethod
    def create_profiles_file(cls):
        profiles_temp = { 
            "cubic" : Profile(6, 1)
            }
        picklle.picklle(cls.profiles_file_name, profiles_temp)

    @classmethod
    def load_profiles_file(cls):
        cls.profiles = picklle.unpickle(cls.profiles_file_name)
    

    @classmethod
    def load_profiles(cls):
        try:
            cls.load_profiles_file()
        except:
            cls.create_profiles_file()
            cls.load_profiles_file()
 

    def __init__(self, number_of_faces, number_of_dices):
        self.number_of_faces = number_of_faces
        self.number_of_dices=number_of_dices


    def __str__(self):
        return f"number of faces -> {self.number_of_faces}; number of dices -> {self.number_of_faces}"


    def roll(self):
        return dice_simulator.RollDices.roll_dices(self.number_of_faces, self.number_of_dices)




class ManageProfiles():

    @staticmethod
    def pickle_profiles():
        picklle.picklle(Profile.profiles_file_name, Profile.profiles)


    @staticmethod
    def make_profile(profile_name, number_of_faces=6, number_of_dices=1):
        Profile.profiles[profile_name] = Profile(number_of_faces, number_of_dices)
        ManageProfiles.pickle_profiles()


    @staticmethod
    def view_profiles():
        to_return = [f"{key_value}: {Profile.profiles[key_value]}" for key_value in Profile.profiles]
        
        if len(to_return) == 0:
            return "No Profiles yet!"
        else:
            return "\n".join(to_return)

    @staticmethod
    def del_profile(profile_name):
        del Profile.profiles[profile_name]
        ManageProfiles.pickle_profiles()


    @staticmethod
    def roll_profile(profile_name):
        return Profile.profiles[profile_name].roll()
    

    @staticmethod
    def reset_settings():
        Profile.create_profiles_file()
        return "Settings reset!"




#IMPORTANT - Load profiles file "profiles.pickle"
#don't delete this line!


Profile.load_profiles()
