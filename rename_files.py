import os

def rename_files():
    file_list = os.listdir(r"C:\Users\huanjinzi\Downloads\prank")
    #print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\huanjinzi\Downloads\prank")
    for file_name in file_list:
        new_file = file_name.translate(None,"0123456789")
        print("old file_name:" + file_name + ",new_file:" + new_file)
        os.rename(file_name,new_file)
        
rename_files()
