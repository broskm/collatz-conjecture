import sys
from typing import Counter
x = 999999999
sys.setrecursionlimit(x)


# # binary_ex = "1001101101111010101010101010101010100"


# # def remove_zeros(x):
# #     check = True
# #     zeros_removed=0
# #     while(check):
# #         if x[-1]=="0":
# #             zeros_removed+=1
# #             x=x[:-1]
# #         else:
# #             check = False
# #     return x,zeros_removed


# # def catlas(x):

# #     # zero_start_count = 0
# #     original_num = x
# #     end_zero_count = 0
# #     ones_count = 0
# #     zeros_count = 0
# #     last_zeros_count = 0
# #     length_of_longest_zero = 0

# #     y=remove_zeros(x)
# #     x= y[0]
# #     zero_start_count = y[1]
# #     print(" "+x)
# #     while (x!="1"):
# #         y=x+"1"
# #         print(y)
# #         print("_______________________________________________________________")
# #         ones_count +=1
# #         x = int(x, 2) + int(y, 2)
# #         x =  bin(x)
# #         x = str(x[2:])
# #         print(x)
# #         d = remove_zeros(x)
# #         x = d[0]
# #         print("_______________________________________________________________")
# #         print(" "+x)
# #         if (d[1]>length_of_longest_zero):
# #             length_of_longest_zero = d[1]
# #         zeros_count +=d[1]
# #         last_zeros_count = d[1]
# #     zeros_count -=last_zeros_count
# #     print ("binary_num =",original_num[2:])
# #     print ("end_zero_count=",end_zero_count)
# #     print ("ones_count=",ones_count)
# #     print ("zeros_count",zeros_count)
# #     print ("last_zeros_count=",last_zeros_count)
# #     print("length_of_longest_zero=",length_of_longest_zero)

# #     return x,end_zero_count,ones_count,zeros_count,last_zeros_count


# # catlas(binary_ex)

def even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False


def mutli_two(num, two_div, max_steps, two_streak, max_two_div):
    if two_div > 0 and max_steps > 0 and two_streak < max_two_div:
        num *= 2
        two_div -= 1
        max_steps -= 1
        two_streak += 1


# #note that n must be string value
def divider(n, m):
    number = n
    get = ''
    cost = ''
    start = 0
    rem = 0
    # My long divition algorithem
    for i in range(0, len(n)):
        number = int(cost+n[start:i+1])
        if number >= m:
            rem = 1
            get += str(number//m)
            cost = str(number % m)
            start = i+1
        else:
            # rem can find first loop
            if rem == 1:
                get += '0'
                if i == len(n)-1:
                    cost = str(number)
    return (get, cost)

def div_three_finder(an_array):
    help_array = []
    counter = 0
    for i in range (1,len(an_array)):
        x=i*(-1)
        y=(i+1)*(-1)
        if an_array[x]<an_array[y]:
            help_array.append(y*-1)
            counter+=1
            if counter >1 : 
                break
    if len(help_array)==0:
        return None
    elif len(help_array)>1:
        return(help_array[1]+help_array[0])
    else:
        return(help_array[0])



def collatz(num):
    is_even = False
    max_steps = 0
    two_div = 0
    three_multi = 0
    max_two_div = 0
    help_array = [0]
    last_two_div = 0
    tenth_element = 0
    fiftith_element = 0
    hunderdth_element = 0
    befor_last_step = str(num)[-1]
    process = []
    if (num % 2 == 0):
        is_even = True
    

    while num != 1:
        process.append(num)
        max_steps += 1
        if (num % 2 == 0):
            num //= 2
            two_div += 1
            help_array[-1] += 1
            # print("2")
        else:
            num *= 3
            num += 1
            three_multi += 1
            help_array.append(0)
            # print("3")
        #print(num)
    last_two_div = help_array[-1]
    help_array.pop()
    max_two_rep = 0
    if help_array:
        max_two_div = max(help_array)
    else:
        max_two_div = 1
    two_div -= last_two_div
    if two_div == 0:
        max_two_div = 0
        max_two_rep = 0
    else:
        for i in help_array:
            if i == max_two_div:
                max_two_rep += 1
    process.append(1)
    process.reverse()
    #befor_last_step = div_three_finder(process)
    if len(process) > 9:
        x = process[9]
        for i in str(x):
            tenth_element += int(i)
    else:
        tenth_element = None

    if len(process) > 49:
        x = process[49]
        for i in str(x):
            fiftith_element += int(i)
    else:
        fiftith_element = None

    if len(process) > 99:
        x = process[99]
        for i in str(x):
            hunderdth_element += int(i)
    else:
        hunderdth_element = None

    #print(len(process))
    #print(process)
    #print("collatz status")
    #print(max_steps, two_div, three_multi, max_two_div, last_two_div, is_even,befor_last_step, max_two_rep, tenth_element, fiftith_element, hunderdth_element)
    print("max_steps=", max_steps, "two_div=", two_div, "three_multi=", three_multi,
          "max_two_div=", max_two_div, "last_two_div=", last_two_div, "is_even=", is_even,"max_two_rep=",max_two_rep,
          "tenth_element",tenth_element,"fiftith_element",fiftith_element,"hunderdth_element",hunderdth_element)
    return(max_steps, two_div, three_multi, max_two_div, last_two_div, is_even,befor_last_step, max_two_rep, tenth_element, fiftith_element, hunderdth_element)


def check_element(the_element, tenth_element):
    if tenth_element == None:
        return True
    else:
        x = 0
        for i in str(the_element):
            x += int(i)
        if x == tenth_element:
            return True
        else:
            return False


def reset_ancer(ancer_record):
    while ancer_record:
        while ancer_record[-1]["procces"][-1] != ancer_record[-1]["ancers"][-1]:
            ancer_record[-1]["procces"].pop()
        num = ancer_record[-1]["num"]
        max_steps = ancer_record[-1]["max_steps"]
        two_div = ancer_record[-1]["two_div"]
        three_multi = ancer_record[-1]["three_multi"]
        max_two_div = ancer_record[-1]["max_two_div"]
        procces = ancer_record[-1]["procces"]
        ancers = ancer_record[-1]["ancers"]
        two_streak = ancer_record[-1]["two_streak"]
        max_two_rep = ancer_record[-1]["max_two_rep"]
        is_even = ancer_record[-1]["is_even"]
        befor_last_step =ancer_record[-1]["befor_last_step"]
        tenth_element = ancer_record[-1]["tenth_element"]
        fiftith_element = ancer_record[-1]["fiftith_element"]
        hunderdth_element = ancer_record[-1]["hunderdth_element"]
        #print("correction operations")
        # print(ancer_record[-1])
        ancer_record.pop()
        ancers.pop()
        if two_div > 0 and max_steps > 0 and two_streak < max_two_div and two_div-three_multi > -1:
            #print("two op")
            num *= 2
            two_div -= 1
            max_steps -= 1
            two_streak += 1
            if max_two_rep != 0 and two_streak == max_two_div:
                max_two_rep -= 1
                if max_two_rep == 0:
                    max_two_div -= 1
            procces.append(num)
            # print("red")
            # print(num)
            # print(num,max_steps,two_div, three_multi, max_two_div,procces,ancers,two_streak,ancer_record)
            return has_R(num, max_steps, two_div, three_multi, max_two_div,
                  procces, ancers, two_streak, ancer_record, is_even,befor_last_step, max_two_rep, tenth_element, fiftith_element, hunderdth_element)
            break
    if not ancer_record:
        print("recored is empty")


def has_R(num, max_steps, two_div, three_multi, max_two_div, procces, ancers, two_streak, ancer_record, is_even,befor_last_step, max_two_rep, tenth_element, fiftith_element, hunderdth_element):
    # print(procces)
    # print("num=",num,"max_steps=",max_steps,"two_div=",two_div,"Two_streak=",two_streak,"three_multi=",three_multi,"max_two_div=",max_two_div,"is_even=",is_even)
    # print(ancers)
    # print("________________________________________________________________________________________________________________________________________")
    num_help = num-1
    if len(procces) == 10 and check_element(procces[9], tenth_element) != True:
        return reset_ancer(ancer_record)
    elif len(procces) == 50 and check_element(procces[49], fiftith_element) != True:
        return reset_ancer(ancer_record)
    elif len(procces) == 100 and check_element(procces[99], hunderdth_element) != True:
        return reset_ancer(ancer_record)
    elif max_steps == 0 and two_div == 0 and three_multi == 0 and even_odd(num) == is_even and max_two_rep == 0 and str(num)[-1]==befor_last_step:
        #if div_three_finder(procces) == befor_last_step:
            #print(procces)
            #print("result = ", num)
            return(num)
        # else: 
        #     return reset_ancer(ancer_record)

    elif divider(str(num_help), 3)[1] == '0' and three_multi > 0 and max_steps > 0 and divider(str(num_help), 6)[1] != '0' and two_div-three_multi >= -1:
        #print("three operatin")
        # print(num)
        # print(procces)
        #print(max_steps,two_div, three_multi, max_two_div)
        ancers.append(num)
        ancer_record.append({"num": num, "max_steps": max_steps, "two_div": two_div, "three_multi": three_multi,
                            "max_two_div": max_two_div, "procces": procces, "ancers": ancers, "two_streak": two_streak,
                             "max_two_rep": max_two_rep, "tenth_element": tenth_element, "is_even": is_even,"befor_last_step":befor_last_step, "fiftith_element": fiftith_element,"hunderdth_element":hunderdth_element})
        num -= 1
        num //= 3
        three_multi -= 1
        max_steps -= 1
        procces.append(num)
        two_streak = 0
        # print("ancers operations")
        # print(ancer_record)
        #print("three operatin")
        # print(num)
        #print(num,max_steps,two_div, three_multi, max_two_div,procces,ancers,two_streak,ancer_record)
        return has_R(num, max_steps, two_div, three_multi, max_two_div,
              procces, ancers, two_streak, ancer_record, is_even,befor_last_step, max_two_rep, tenth_element, fiftith_element, hunderdth_element)

    elif two_div > 0 and max_steps > 0 and two_streak < max_two_div and two_div-three_multi > -1:
        #print("two op")
        num *= 2
        two_div -= 1
        max_steps -= 1
        two_streak += 1
        if max_two_rep != 0 and two_streak == max_two_div:
            max_two_rep -= 1
            if max_two_rep == 0:
                max_two_div -= 1
        procces.append(num)
        # print("two_op")
        # print(num)
        return has_R(num, max_steps, two_div, three_multi, max_two_div,
              procces, ancers, two_streak, ancer_record, is_even,befor_last_step, max_two_rep, tenth_element, fiftith_element, hunderdth_element)
    elif ancer_record:
        return reset_ancer(ancer_record)
    else:
        print("num=", num, "max_steps=", max_steps, "two_div=", two_div, "Two_streak=", two_streak, "three_multi=",
              three_multi, "max_two_div=", max_two_div, "ancer_record=", ancer_record, "ancer=", ancers, "max_two_rep=", max_two_rep)
        print("something went wrongg")
        return


def rverse_collatz(max_steps, two_div, three_multi, max_two_div, last_two_div, is_even,befor_last_step, max_two_rep, tenth_element, fiftith_element, hunderdth_element):
    # print(max_steps)
    procces = [1]
    ancers = []
    ancer_record = []
    num = 1
    max_steps -= last_two_div
    while(last_two_div > 0):
        procces.append(procces[-1]*2)
        num *= 2
        last_two_div -= 1
    two_streak = 0
    # print("num=", num, "max_steps=", max_steps, "two_div=", two_div, "Two_streak=", two_streak,
    #      "three_multi=", three_multi, "max_two_div=", max_two_div, "is_even=", is_even)
    return has_R(num, max_steps, two_div, three_multi, max_two_div,
          procces, ancers, two_streak, ancer_record, is_even,befor_last_step, max_two_rep, tenth_element, fiftith_element, hunderdth_element)


# you have to put some stations for the function to prevent the prutal force search :::::

for i in range (27,1000):
    print(i)
    print(rverse_collatz(*collatz(i)))
# x =326541656515646616154665654654661651654461654646

# while x>1:
#     x-=1000
#     print(len(str(x)))
#     print(len(str(bin(x))))
#     print(check_element(80,None))

#     collatz(x)
# for i in range(1,1000):
#     print(i)
#     if i == 231:
#         continue
#     if rverse_collatz(*collatz(i)) != i: 
#         print(rverse_collatz(*collatz(i)))
#         print("_________________________________________________")


# note that n must be string value 67


# x = 78456419195712045404065470987054564056549994
# print(len(str(x)))
# print(len(bin(x)))
# counter = 0
# while x!=1:
#     y = divider(str(x),2)
#     if int(y[1])==0:
#         x=int(y[0])
#         # print(x)
#         # print("2")
#         counter+=1
#     else:
#         x*=3
#         x+=1
#         # print(x)
#         # print("3")
#         counter+=1
# print(counter)


# z =10000000000000000000000000000000000000000000000000
# print(len(str(z)))
# Counter = 0
# while z%1000000 == 0:
#     z = z//1000000
#     print(z)
#     Counter +=1
#     print(Counter)

# def string2bits(s=''):
#     return ''.join([bin(ord(x))[2:].zfill(8) for x in s])

# def bits2string(b=None):
#     return ''.join([chr(int(x, 2)) for x in b])
# my_string = 'adkfjladskjfks asdfs'
# # print(len(my_string))
# my_binary = string2bits(my_string)
# my_decimal = int(my_binary,2)
# print("string_len")
# print(len(my_string))
# print("bin len")
# print(len(my_binary))
# print("dis len")
# print(len(str(my_decimal)))

# print(len(my_binary))
# print(80**3)
