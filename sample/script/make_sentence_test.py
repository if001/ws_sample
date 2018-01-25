import time

def make_sentence():
    time.sleep(5)
    arr = ["hello","world"]
    return arr

def main():
    mess = make_sentence()
    print(mess)
    print("end")


if __name__ == "__main__":
   main()
