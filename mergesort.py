import random


def merge_sort(lst:[])->[]:
    if len(lst) <= 1:
        return lst
    else:
        middle_of_list = len(lst)//2
        left_part = lst[:middle_of_list]
        right_part = lst[middle_of_list:]
        sorted_left_part = merge_sort(left_part)
        sorted_right_part = merge_sort(right_part)

        return merge_left_right(sorted_left_part,sorted_right_part)

def merge_left_right(left_part:[],right_part:[])->[]:
    merge_result = []
    left_pos = right_pos = 0
    while left_pos < len(left_part) and right_pos < len(right_part):
        left_element = left_part[left_pos]
        right_element = right_part[right_pos]
        if isinstance(left_element,str) and isinstance(right_element,str):
            min_len = min(len(left_element),len(right_element))
            cur_pos = 0
            while cur_pos<min_len:
                left_element_code = ord(left_element[cur_pos])
                right_element_code = ord(right_element[cur_pos])
                if left_element_code < right_element_code:
                    merge_result.append(left_element)
                    left_pos +=1
                    break
                elif left_element_code == right_element_code:
                    if cur_pos<min_len-1:
                        cur_pos +=1
                    else:
                        if min_len == len(left_element):
                            merge_result.append(left_element)
                            left_pos +=1
                            break
                        else:
                            merge_result.append(right_element)
                            right_pos +=1
                            break
                else:
                    merge_result.append(right_element)
                    right_pos +=1
                    break

        elif isinstance(left_element,int|float) and isinstance(right_element,int|float):
            if left_part[left_pos] < right_part[right_pos]:
                merge_result.append(left_part[left_pos])
                left_pos += 1
            else:
                merge_result.append(right_part[right_pos])
                right_pos += 1
        else:
            raise TypeError("Types of list elements do not support sorting in such a way!")
    merge_result.extend(left_part[left_pos:])
    merge_result.extend(right_part[right_pos:])

    return merge_result

#generate list filled with random ints
list_items_count:int=20
unsorted_list = [random.randint(0-(list_items_count*50),list_items_count*50) for x in range(list_items_count)]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)
#create list filled with strings
unsorted_list = ["bee", "apples", "apple", "ape"]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)
unsorted_list = ["bee","apples","apple",1,"ape"]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)