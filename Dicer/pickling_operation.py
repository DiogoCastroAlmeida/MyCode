import pickle



def picklle(file_path, object):
        with open(file_path, "wb") as file:
            pickle.dump(object, file)


def unpickle(file_path):
        with open(file_path, "rb") as file:
            pickled = pickle.load(file)
            return pickled


