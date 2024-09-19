s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')   
        

print("\n")
def bin_search(L, e, low, high):
    if high == low:
        return L[low] == e
    mid = (low + high) // 2
    if L[mid] == e:
        return True
    elif L[mid] > e:
        if low == mid: #nothing left to searh
            return False
        else:
            return bin_search(L, e, low, mid - 1)
    else:
         return bin_search(L,e, mid+1 , high)


def make_list(num):
    my_list = []
    for number in range(num):
        my_list.append(number)
    return my_list

my_list = make_list(12323)
print(my_list)

print(bin_search(my_list, 253, 0, 1750))
