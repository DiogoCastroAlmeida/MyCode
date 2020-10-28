import dice_simulator
import pickle
class PicklingOperations():
    @staticmethod
    def picklle(file_path, object):
        with open(file_path, "wb") as file:
            pickle.dump(object, file)
            return True

    @staticmethod
    def unpickle(file_path):
        with open(file_path, "rb") as file:
            pickled = pickle.load(file)
            return pickled


class Profile():
    profiles = {

    }
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
        pass



    @staticmethod
    def make_profile(profile_name, number_of_faces=6, number_of_dices=1):
        Profile.profiles[str(profile_name)] = Profile(number_of_faces, number_of_dices)


    @staticmethod
    def view_profiles():
        to_return = [f"{key_value}: {Profile.profiles[key_value]}" for key_value in Profile.profiles]
        return "\n".join(to_return)

    @staticmethod
    def del_profile(profile_name):
        del Profile.profiles[str(profile_name)]


    @staticmethod
    def roll_profile(profile_name):
        return Profile.profiles[str(profile_name)].roll()
