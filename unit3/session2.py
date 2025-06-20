# CODEPATH W3S2 Mock Interview Question
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at
# list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.

# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# findRestaurant(list1, list2)
# ['Shogun']     # index sum = 0 + 3 = 3, the smallest possible


# Understand: return sums of indices where a string appears in list1 and list2
# Match: potential 2 pointer, potential set solution
# Plan:
# Implement:


def solution(list1, list2):

    list1_dict = {}
    # create a dictionary of strings -> indices in list1
    for i in range(len(list1)):
        if list1[i] not in list1_dict:
            list1_dict[list1[i]] = i

    ret = []
    existing_min = float("inf")

    # iterate through list2 checking if strings in list2 appear in the dictionary
    for i in range(len(list2)):
        # if a string does appear in list2, sum the indices together and create a new dict of common strings -> index sum.
        # alternative idea: store a minimum index sum string: check the index sum of new common string values against a minimum
        if list2[i] in list1_dict:

            index_sum = i + list1_dict[list2[i]]

            # if new sum is less than existing sum, replace everything in ret and replace existing_min
            if index_sum < existing_min:
                ret = [list2[i]]
                existing_min = index_sum
            # if new sum is equal to existing minimum, return this common string as well.
            elif index_sum == existing_min:
                ret.append(list2[i])

    return ret
