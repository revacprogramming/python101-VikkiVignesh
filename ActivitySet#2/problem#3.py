

def get_str():
   """get string input"""
   string=''
   string=input("Enter the string:")
   return string


def str_to_lst(cs):
    """convert connected string to list of strings"""
    lst=list()
    for word in cs:
      lst.append(word)
    return lst

def main():
   name=get_str()
   list=str_to_lst(name)
   print(list)


if __name__ == '__main__':
    main()
