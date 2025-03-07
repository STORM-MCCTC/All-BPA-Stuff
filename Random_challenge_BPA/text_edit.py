import os
def main_menu():
    print("TXT Editor")
    print("")
    print("1 - Write File")
    print("2 - Append file")
    print("3 - read file")
    print("4 - delete file")

    choice = input("")
    if choice == "1":
        write_file()
    elif choice == "2":
        append_file()
    elif choice == "3":
        read_file()
    elif choice == "4":
        delete_file()
    else:
        main_menu()

def write_file():
    file_name = input("File name(include file extenison): ")
    file_text = input("text content: ")

    f = open(f"{file_name}", "w")
    f.write(file_text)
    f.close()
    main_menu()

def append_file():
    file_name = input("File name(include file extenison): ")
    file_text = input("text content: ")

    f = open(f"{file_name}", "a")
    f.write(f"\n{file_text}")
    f.close()
    main_menu()

def read_file():
    file_name = input("File name(include file extenison): ")

    f = open(f"{file_name}", "r")
    print(f.read())
    input("enter continue: ")
    main_menu()

def delete_file():
    file_name = input("File name(include file extenison): ")
    
    os.remove(file_name)
    main_menu()

main_menu()