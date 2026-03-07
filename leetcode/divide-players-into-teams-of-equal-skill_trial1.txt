class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total_skill  = skill[0] + skill[len(skill) - 1]
        left, right = 0, len(skill) - 1

        chemistry_sum = 0
        while left < right:
            if skill[left] + skill[right] == total_skill:
                chemistry_sum += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
        return chemistry_sum
        

        