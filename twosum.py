def twoSum(self, nums: list[int], target: int) -> list[int]:
    hasil = []
    for i in range(len(nums)):
        j = i + 1
        while j < len(nums):
            if (nums[j] + nums[i] == target):
                hasil.append(i)
                hasil.append(j)
                return hasil
            else:
                j += 1
    return None

            