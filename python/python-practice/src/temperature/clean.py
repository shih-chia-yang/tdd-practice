def clean_line(line):
    clean_line=line.replace("\n","")
    return clean_line

def get_words(clean_line):
    return clean_line.split("|")
