"""
File:    proj3.py
Author:  Hamza Qureshi
Date:    05/05/2020
Section: 15
E-mail:  hamz1@umbc.edu
Description:

"""
from person import Person
import json


class DynasticDescent:
    def __init__(self):
        # one family per dict
        self.family_tree = {}

    def add_person(self):
        next_name = str(input('What is the name of the human? '))
        next_name.lower()
        self.new_node = Person(next_name).jsonify()
        if next_name not in self.family_tree:
            self.family_tree[next_name] = self.new_node
            print(self.family_tree)

    def relate_people(self):
        # assigns children to parents
        parent_name = str(input('What is the name of the parent? '))
        parent_name.lower()
        child_name = str(input('What is the name of the child? '))
        child_name.lower()
        if parent_name in self.family_tree and child_name in self.family_tree:
            self.family_tree[parent_name]['children'].append(child_name)
        else:
            print('That name is not in the family')

        def make_tree(dict, degree=0):
            for key, value in dict.items():
                print('\t' * degree + str(key))
                if key == dict[key]['children']:
                    make_tree(value, degree + 2)
                else:
                    print('\t' * (degree + 1) + str(value))




        make_tree(self.family_tree, 0)

    def get_ancestors(self):
        pass

    def save(self, file_name):

        final_dict = {}
        for element in self.family_tree:

            print(self.family_tree[element].jsonify())

            final_dict.update(self.family_tree[element].jsonify())

        with open(file_name, 'w') as game_file:
            # everything in one dictionary
            file_save_dictionary = {'Names': self.family_tree}
            # save everything as one json file
            game_file.write(json.dumps(file_save_dictionary))
            # close file

    def load(self, file_name):
        with open(file_name, 'r') as read_json:
            the_entire_file = read_json.read()
            the_entire_dict = json.loads(the_entire_file)

            for name in the_entire_dict:
                name_dict = the_entire_dict[name]
                new_name = Person(name_dict)

                # avoid double loading ??
                if name not in self.family_tree:

                    self.family_tree[name] = new_name

        return name_dict

    def play_game(self):
        self.next_move = str(input('What would you like to do next? '))
        self.next_move.lower()

        while self.next_move != 'quit':

            if self.next_move == 'add':
                self.add_person()

            elif self.next_move == 'get parents':
                self.get_ancestors()

            elif self.next_move == 'get siblings':
                self.get_ancestors()

            elif self.next_move == 'relate':
                self.relate_people()

            elif self.next_move == 'load tree':
                Tree = input('What tree would you like to load? ')
                self.load(Tree)

            elif self.next_move == 'save tree':
                Tree = input('Save as: ')
                self.save(Tree)

            self.next_move = str(input('What would you like to do next? '))

if __name__ == "__main__":

    new_game = DynasticDescent()
    new_game.play_game()