class Solution:
    def calculateScore(self, instructions: list[str], values: list[int]) -> int:
        
        
        score = 0
        i = 0
        while 0<= i<= len(instructions):
            if instructions[i] == 'add':
                score += values[i]
                i +=1

            if instructions[i] == 'jump':
                i = i + values[i]
        return score  