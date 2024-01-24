def bubble_sort(nums: list[int]):
    for k in range(len(nums)):
        for j in range(len(nums) - 1 - k):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print(bubble_sort([3, 4, 2, 9, 1, 11, 2, 7]))
# [1, 2, 2, 3, 4, 7, 9, 11]
