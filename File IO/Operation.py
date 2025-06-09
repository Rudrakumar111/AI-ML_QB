#Reading Operation
def reading_op():

    f = open("demo1.txt","r+")

    data = f.readline()

    print(data)
    print(f)

    f.close()

#Writing Operation
def writing_op():
    with open("demo1.txt","w+") as f:
        f.write("hello Rudrakumar")



#append at the end
def append_op():
    with open("demo1.txt", "a") as f:
        f.write("Hello")

reading_op()
writing_op()
append_op()