"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class PersonSearch:
    def search_by_name(self, people: list[Person], target_name: str) -> int:
        left = 0
        right = len(people) - 1
        while left <= right:
            middle = (right + left) // 2

            if people[middle].name == target_name:
                return middle
            
            elif people[middle].name > target_name:
                right = middle - 1

            else:
                left = middle + 1

        return -1

# Exemplo de uso
people_list = [
    Person("Alice", 25),
    Person("Bob", 30),
    Person("Charlie", 22),
    Person("David", 35),
    Person("Eva", 28),
    Person("Frank", 40)
]

target_name = "Eddy" #"Charlie"

person_search = PersonSearch()
result_index = person_search.search_by_name(people_list, target_name)

if result_index != -1:
    print(f"A pessoa com o nome '{target_name}' foi encontrada no índice {result_index}.")
else:
    print(f"A pessoa com o nome '{target_name}' não foi encontrada na lista.")
