import mio

def main():
    mio.capture_output("example.txt","1234","567","8910")
    mio.print_file("example.txt")

if __name__=="__main__":
    main()