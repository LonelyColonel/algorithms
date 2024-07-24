def bubble_sort(nums: list[int]):
    for k in range(len(nums)):
        for j in range(len(nums) - 1 - k):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
