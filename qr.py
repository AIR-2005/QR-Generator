import qrcode
import sys

#QR Class
class QR:
    #Initialize object
    def __init__(self,data):
        #Data and it's qr code
        self.data = data
        self.qr = qrcode.make(self.data)

    #Function to save the qr code to given path as given file name(default name is qr.png) 
    def save_qr(self,path,name="qr.png"):
        self.qr.save(path+"/"+name)

#Main Function
def main():
    #Take first command line argument as data
    qr_code = QR(sys.argv[1])
    #Take second command line argument as path and optionally take third command line argument as file name
    qr_code.save_qr(*sys.argv[2:])

#If this file is directly running run main function
if __name__ == "__main__":
    main()