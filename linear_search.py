def linear_search(search_list:[],search_element,pos=0)->int:
    if pos == len(search_list):
        return -1
    else:
        if search_element == search_list[pos]:
            return pos
        else:
            return linear_search(search_list,search_element,pos+1)

search_lst = [1,2,3,4,5]
search_elem = 3
print(linear_search(search_lst,search_elem))