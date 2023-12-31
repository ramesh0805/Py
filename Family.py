class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.parents = []
        self.spouse = None
        self.children = []

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_spouse(self, spouse):
        self.spouse = spouse

    def add_child(self, child):
        self.children.append(child)

    def find_relationship(self, person2):
        if person2 in self.parents:
            return "parent"
        elif person2 in self.children:
            return "child"
        elif self.spouse == person2:
            return "spouse"
        elif person2.spouse == self:
            return "spouse"
        else:
            return "No direct relationship"

    def display_family_tree(self, level=0):
        print(" " * level + self.name)
        for child in self.children:
            child.display_family_tree(level + 1)

if __name__ == "__main__":
    john = Person("John", "Male")
    mary = Person("Mary", "Female")
    alice = Person("Alice", "Female")
    bob = Person("Bob", "Male")

    john.add_spouse(mary)
    mary.add_child(alice)
    mary.add_child(bob)

    print("Family Tree:")
    john.display_family_tree()

    relationship_john_bob = john.find_relationship(bob)
    relationship_mary_alice = mary.find_relationship(alice)

    print(f"Relationship between John and Bob: {relationship_john_bob}")
    print(f"Relationship between Mary and Alice: {relationship_mary_alice}")




OUTPUT:



Family Tree:
John
Relationship between John and Bob: No direct relationship
Relationship between Mary and Alice: child
