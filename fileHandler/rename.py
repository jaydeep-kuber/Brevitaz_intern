import os
path = input("Enter full path where image located: ")
path= path.replace('\\','/')
back_slash = "\\"
if path[-1] != back_slash:
    path = path + '/'

print("Your Path: ",path)
# print(os.listdir(path))
def main():
    i=1
    for file in os.listdir(path):
        new_mane= path+'SS_'+str(i)+'.jpg'
        old_name_= path+file
        os.rename(old_name_,new_mane)
        i+=1
    print("renameing done, you can do check in folder")
main()