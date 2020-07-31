

def revert(s):

    if s:
        s=s[-1]+revert(s[:-1])
    return s


def revert2(s):

    return s[::-1]


def reverse_sentence(string):
    to_string=list(string)

    reversed=to_string[::-1]

    return "".join(reversed)


def string_compression(string):
    count,last=1,""
    list_aux=[]
    for i,c in enumerate(string):
        if last==c:
            count+=1
        else:
            if i!=0:
                list_aux.append(str(count))

            list_aux.append(c)
            count=1
            last=c
    list_aux.append(str(count))

    return "".join(list_aux)



if __name__=="__main__":
    a="aaabbbbccc"
    print(string_compression(a))




