def selection_sort(nums: list[int]):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(selection_sort([3, 4, 2, 9, 1, 11, 2, 7]))
# [1, 2, 2, 3, 4, 7, 9, 11]
