#The key steps in the merge sort algorithm are
#1 Divide
#2 Conquer
#3 Merge
def merge_sort(lst:[])->[]:
    #check if length of list is one -> already sorted
    #also cover the edge case where there is an empty list
    if len(lst) <= 1:
        return lst
    else:
        #Get the middle of the list and start dividing the list into two parts
        middle_of_list = len(lst)//2
        left_part = lst[:middle_of_list]
        right_part = lst[middle_of_list:]
        #Pass the left part and divide it into smaller parts recursively
        sorted_left_part = merge_sort(left_part)
        #Pass the right part and divide it into smaller parts recursively
        sorted_right_part = merge_sort(right_part)

        return merge_left_right(sorted_left_part,sorted_right_part)

def merge_left_right(left_part:[],right_part:[])->[]:
    merge_result = []
    left_pos = right_pos = 0
    while left_pos < len(left_part) and right_pos < len(right_part):
        #If the left part element's value is smaller than the right part append the
        #left part element to the list
        if left_part[left_pos] < right_part[right_pos]:
            merge_result.append(left_part[left_pos])
            left_pos += 1
        else:
        #If the right part element's value is greater it will be appended to the list
            merge_result.append(right_part[right_pos])
            right_pos += 1
    #If one of the parts ( left or right ) has been exhausted for example the left part
    #we must extend the list with the remaining elements of the right part.
    merge_result.extend(left_part[left_pos:])
    merge_result.extend(right_part[right_pos:])

    return merge_result