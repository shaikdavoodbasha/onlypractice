arr = list(map(int,input("Enter a list of array elements :").split(",")))

arr_sorted = sorted(arr)
set_arr = set(arr_sorted)
return_arr = list(set_arr)
again_sorted = sorted(return_arr)
if(len(again_sorted)>1):
  print("The largest is {} ,The second largest is {}".format(again_sorted[-1],again_sorted[-2]))
else:
  print("No second largets element is presented")