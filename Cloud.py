import dropbox

class TransferData:
    def _init_(self,access_token):
        self.access_token =access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token ='sl.Ak5uIodo-nc4T-Vo4WnD21fSF-KN0_q2Nu-EwAhu78ZPbyK4e7-6p0Rfetl_1OMvx48jE1JbOGkw-0O5R8mf09ykG-mmKKAwPmZPmqKrtr3iAHGjFdW4N_OopwbmLpxZm5ccF1Y'
    transferData =TransferData(access_token)

    file_from = input("enter file to transfer :")
    file_to = input("enter the path to upload to dropbox :")
    transferData.upload_file(file_from, file_to)
    print("file transferred succesfully")


main()


        