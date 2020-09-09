import os
import time
import shutil
import smtplib
import zipfile


extension=".sql"

def main():

    deleted_files_count = 0

    path = 'F:/sqql'    # specify the  path
    days=0              # specify days
    seconds = time.time() - (days * 24 * 60 * 60)
    f_zip=zipfile.ZipFile('F:/sqql/archive.zip','w')

    if os.path.exists(path):

        # iterating over each and every folder and file in the path
        for root_folder,folders, files in os.walk(path):

            # checking the current directory files
            for file in files:
            #for make zip file
                if file.endswith('.sql'):
                    f_zip.write(os.join.path(folders,file),os.relpath.join(os.join.path(folders,file),'F:/sqql'),compress_type=zipfile.ZIP_DEFLATED)                # file path
                    print("sucessfully archive files")
                    f_zip.close()

                file_path = os.path.join(root_folder, file)
                file_extension = os.path.splitext(file_path)[1]

                # comparing the days and extension of file
                if seconds >= get_file_age(file_path) and extension== file_extension:
                    # invoking the remove_file function
                    if not os.remove(file_path):
                        print(f"{file_path} deleted successfully")
                    deleted_files_count += 1  # incrementing count

    else:

        # file/folder is not found
        print(f'"{path}" is not found')
        deleted_files_count += 1  # incrementing count

    print(f"Total files deleted: {deleted_files_count}")


#After deleting files send message to client

    li = ["rahulshinde1206148@gmail.com"]# list of email_id to send the mail

    for dest in li:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("rahulshinde1206148@gmail.com", "xxxxxxx") # unable to send mail due to gmail server not allowed to login
        message = "Please confirm, We have run script to delete old sql file from server " \
                  "Thanks and regards " \
                  "rahul shinde"
        s.sendmail("rahulshinde1206148@gmail.com", dest, message)
        s.quit()

def get_file_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()