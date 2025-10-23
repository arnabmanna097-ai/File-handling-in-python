#here i want to perfom CRUD (Create, Read, Update and Delete)
from pathlib import Path
import os
#Step1: to create a function to see the files available in a folder directory
def see_file_and_folder():
    path= Path('') #it give directory where the folder are saved
    items = list(path.rglob('*')) #  rglob() traverses through all subdirectories, making it suitable for finding files deep within a directory structure.
    for i, items in enumerate(items): # i is the index and items are the files name
        print(f'{i+1}:{items}')

#Step2: To take input from user
print('Press 1 for creating a file')
print('press 2 for reading a file')
print('press 3 for updating a file')
print('press 4 for deleting a file')
input_from_user= int(input('tell me the number:-'))

#Step3: To create a function where user can create a file inside the same directory

def create_file():
    see_file_and_folder()
    file_create= input('Tell me the file name you wan to create:-')
    p = Path(file_create) #here i save the input as a file first
    try:
        if not p.exists():
            with open(p,'w') as fs:
                data= input('if you wan to write something you can:-')
                fs.write(data)
            print('FILE CREATED SUCCESSFULLY')
        else:
            print('FILE ALREADY EXISTS')
    except Exception as err:
        print('The error ocuured as',err)


#step3: To create a function for reading a file

def read_file():
    see_file_and_folder()
    name= input('Tell me the file name:-')
    p= Path(name)
    try:
        if p.exists():
            with open(p,'r') as fs:
                print(fs.read())
            print('THE FILE IS SUCCESSFULLY READ')
        else:
            print('FILE DOES NOT EXIST')
    except Exception as err:
        print('The error ocurred as', err)
             




#Step3 To update the file
def Update_file():
    see_file_and_folder()
    update= input('Which file you want to update:-')
    p= Path(update)
    try:
        if p.exists() and p.is_file():
            print('Press 1 for renaming the file')
            print('press 2 for oerwritting the file')
            print('press 3 for appending the file')
        
            res= int(input('Press the number:-'))
            if res==1:
                data= input('Type the new file name:-')
                os.rename(update, data)
                print(f'File {update} is renamed to {data} successfully')
            elif res==2:
                with open(update,'w') as fs:
                    data2= input('what you wan to write?')
                    fs.write(data2)
                print('The File is successfully overwritten')
            elif res==3:
                with open(update,'a') as fs:
                    data3 = input('what you want to append:-')
                    fs.write(data3)
                print('The append is successfully executed')
            else:
                print('FILE DOES NOT EXISTS')

    except Exception as err:
        print('The error occured due to',err)

#step4: To delete a file
def delete_file():
    see_file_and_folder()
    delete= input('which file you want to delete-')
    p = Path(delete)

    try:
        if p.exists() and p.is_file():
            os.remove(delete)
            print(f'File {delete} is successfully deleted')
        else:
            print('File is not found')
    except Exception as err:
        print('The error occured due to', err)



if input_from_user==1:
    create_file()
elif input_from_user==2:
    read_file()
elif input_from_user == 3:
    Update_file()
elif input_from_user == 4:
    delete_file()

