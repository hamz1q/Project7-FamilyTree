class Person:
    def __init__(self, name):
        self.name = name
        self.children = []

    def jsonify(self):
        return {'children': self.children}