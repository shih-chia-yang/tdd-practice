
def word_count(words):
    word_count={}
    for word in words:
        try:
            count=word_count.setdefault(word,0)
        except TypeError:
            pass
        word_count[word]+=1
    return word_count

def calculate(word_count):
    word_list=list(word_count.items())
    word_list.sort(key=lambda x:x[1])
    try:
        least_common=word_list[:5]
        most_common=word_list[-1:-6:-1]
    except  IndexError as e:
        least_common=word_list
        most_common=list(reversed(word_list))
    return most_common,least_common