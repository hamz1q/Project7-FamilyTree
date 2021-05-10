class DynasticDescent:
    def __init__(self):
        pass
    def get_parents(self):
        current_person = 'current person'  # place holder

        if current_person:
            pass
    def get_children(self):
        current_person = 'current person'  # place holder

        if current_person:
            pass

    def get_siblings(self):
        current_person = 'current person' # place holder

        if current_person:
            pass

    def add_person(self):
        person_entered = 'person' # place holder

        if person_entered in self.family_tree():
            print('Passed')
        else:
            print('Failed')



    def relate_people(self):
        parent = 'person'
        child_human = 'human'
        family_tree = {{}}

        if parent not in family_tree:
            print('failed')
        else:
            print('true')

        if child_human not in family_tree:
            print('Failed')
        else:
            print('True')

        if parent == child_human:
            print('failed')
        else:
            print('Passed')

        if parent != family_tree[parent]:
            print('failed')
        else:
            print('Passed')


    def family_tree(self):
        pass