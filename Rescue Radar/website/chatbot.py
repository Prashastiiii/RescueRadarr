import pickle
import os

class Chatbot:
    def __init__(self, training_file='training_data.txt', learned_file='learned_data.pkl'):
        self.training_file = training_file
        self.learned_file = learned_file
        self.responses = {}
        self.load_initial_data()
        self.load_learned_data()

    def load_initial_data(self):
        if os.path.exists(self.training_file):
            with open(self.training_file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split('::')
                    if len(parts) == 2:
                        self.responses[parts[0].strip().lower()] = parts[1].strip()

    def load_learned_data(self):
        if os.path.exists(self.learned_file):
            with open(self.learned_file, 'rb') as file:
                self.responses.update(pickle.load(file))

    def save_learned_data(self):
        with open(self.learned_file, 'wb') as file:
            pickle.dump(self.responses, file)

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        return self.responses.get(user_input, None)

    def learn_response(self, user_input, response):
        self.responses[user_input.lower().strip()] = response.lower().strip()
        self.save_learned_data()
