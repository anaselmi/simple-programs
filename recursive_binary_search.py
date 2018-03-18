from math import ceil

def recursive_binary_search(target, sorted_list, lo=0, hi=-1):
    if lo == hi:
    	if sorted_list[lo] == target:
    		return lo
    	else:
    		return "Target not in list"
    if hi == 0:
    	hi = len(sorted_list) - 1

    mid = hi - ceil((hi - lo) - 1 / 2)

    if sorted_list[mid] == target:
    	return mid
    elif sorted_list[mid] > target:
        hi = mid - 1
        return recursive_binary_search(target, sorted_list, lo, hi)
    elif sorted_list[mid] < target:
        lo = mid + 1
        return recursive_binary_search(target, sorted_list, lo, hi)

print(recursive_binary_search(26, [1, 5, 9, 13, 17, 26]))
