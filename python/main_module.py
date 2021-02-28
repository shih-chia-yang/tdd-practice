def create_divider(title,count=0,align="^",symbol=" "):
    length=80
    while count!=0:count -=1;print(' ')
    else:print(f'{title:{symbol}{align}{length}}')
    print(' ')


if __name__ == "__main__":
    create_divider()