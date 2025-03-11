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
        left_element = left_part[left_pos]
        right_element = right_part[right_pos]
        #Check if both elements are strings and if so start comparing them as strings
        if isinstance(left_element,str) and isinstance(right_element,str):
            #Find out which element has the shortest length to avoid IndexError
            min_len = min(len(left_element),len(right_element))
            #Set the current position to 0
            cur_pos = 0
            #Iterate through all positions unti min_length is reached
            while cur_pos<min_len:
                #Get the ascii value of both elements which we will compare
                left_element_code = ord(left_element[cur_pos])
                right_element_code = ord(right_element[cur_pos])
                #Self-explanatory
                if left_element_code < right_element_code:
                    merge_result.append(left_element)
                    left_pos +=1
                    #If the ascii code value is less append and move to next element,
                    #also exit the inner while loop
                    break
                #If the ascii code values are equal then move to the next letter of the word
                elif left_element_code == right_element_code:
                    #If the current position hasn't reacche the end of the word
                    #Move to the next symbol
                    if cur_pos<min_len-1:
                        cur_pos +=1
                    #If the end of the word has been reached
                    else:
                        #Check which element has been 'depleted' and then
                        #consider it to be with 'less' value than the other
                        #since whitespace characters ( empty ) are with smaller
                        #value than alphabetical characters
                        if min_len == len(left_element):
                            merge_result.append(left_element)
                            left_pos +=1
                            break
                        else:
                            merge_result.append(right_element)
                            right_pos +=1
                            break
                #Self-explanatory
                else:
                    merge_result.append(right_element)
                    right_pos +=1
                    break
        #If the elements are ints or floats, compare them as numbers
        elif isinstance(left_element,int|float) and isinstance(right_element,int|float):
            #Self-explanatory
            if left_part[left_pos] < right_part[right_pos]:
                merge_result.append(left_part[left_pos])
                left_pos += 1
            else:
            #Self-explanatory
                merge_result.append(right_part[right_pos])
                right_pos += 1
        else:
            #If both elements cannot be compared raise TypeError
            raise TypeError("Types of list elements do not support sorting in such a way!")
    #If
    merge_result.extend(left_part[left_pos:])
    merge_result.extend(right_part[right_pos:])

    return merge_result