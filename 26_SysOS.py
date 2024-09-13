#!/usr/bin/env py
import sys
import os


def demo_sys():
    if len(sys.argv) == 3:
        print("Valid args, Will continue")
    else:
        print(f"Invalid args {len(sys.argv)}. Will abort.")
        return 
    
    for arg in sys.argv:
        print(arg, end=" ")
    print()

    print(f"{sys.path=}")
    print(f"{sys.version=}")


def demo_os():
    curr_dir = os.getcwd()
    print(curr_dir)

    new_dir = os.path.join(curr_dir, "newFolder")
    print(new_dir)

    if os.path.exists(new_dir):
        print("Directory exists already")
    else:
        os.mkdir(new_dir)
        print("Created directory!")

    print(os.listdir(new_dir))


    new_file = os.path.join(new_dir, "newFile.txt")
    print(new_file)

    # try:
    #     file = open(new_file, mode="w")
    #     file.write("This is some text data in the file.")
    #     file.flush()
    # except Exception:
    #     print("Exception occurred")
    # finally:
    #     file.close()


    lines = ["first line\n", "second line\n", " third line"]
    with open(new_file, mode="w") as file:
        file.write("This is some text data in the file.")
        file.writelines(lines)
        # file.flush()

    with open(new_file, mode="r") as file:
        text = file.read()
        print(">>>>", text)
        file.seek(5)
        text = file.read(10)
        pos = file.tell()
        print(f"{pos=}")
        print(">>>>", text)
        file.write

    # os.remove(new_file)

    # os.rmdir(new_dir)

# demo_sys()
demo_os()