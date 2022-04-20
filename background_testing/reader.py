
def read_from_file(file):
    f = open(file, "r")
    r = f.read()
    f.close
    return r

if __name__ == "__main__":
    print(read_from_file("db.txt"))