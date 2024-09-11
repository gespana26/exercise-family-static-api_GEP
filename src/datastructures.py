
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        # example list of members
        self._members = [
            {
                "id": 1,
                "first_name": "John Jackson",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "Jane Jackson",
                "age": 35,
                "lucky_numbers": [10,14,3]
            },
            {
                "id": 3,
                "first_name": "Jimmy Jackson",
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id
       

    def add_member(self, member):
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        for i in range(len(self._members)):
            print(self._members[i].get('id'), "VAlor de i:  ",i )
            if self._members[i].get('id') == id:
                self._members.remove(self._members[i])
                return self._members
        return "ID member doesn't exists"

    def get_member(self, id):
        for i in range(len(self._members)):
            print(self._members[i].get('id'), "VAlor de i:  ",i )
            if self._members[i].get('id') == id:
                return self._members[i]
        return "ID member doesn't exists"    

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
