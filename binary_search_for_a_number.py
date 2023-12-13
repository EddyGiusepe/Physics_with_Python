"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Link de estudo: https://www.youtube.com/watch?v=Dt4FKOF25ZY
"""

"""
Binary Search
=============
Dado um array de inteiros 'nums' que é classificado em ordem crescente e um 'alvo' inteiro,
escreva uma função para pesquisar o 'alvo' em 'nums'. Se o destino existir, retorne seu índice.
Caso contrário, retorne -1.
Você deve escrever um algoritmo com complexidade de tempo de execução 0(log n).
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right + left) // 2

            if nums[middle] == target:
                return middle
            
            elif nums[middle] > target:
                right = middle - 1

            else:
                left = middle + 1

        return -1 


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 6

    solution = Solution()
    resultado = solution.search(nums=nums, target=target)

    print(f"O índice do {target} é: {resultado}")
