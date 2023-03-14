import ftplib
import os
import shutil
import logging
import datetime
import logging
import time


class FileTransfer:

    HOSTNAME = "ftp.dlptest.com"  #Host name of the ftp server used int he program to connect to
    USERNAME = "dlpuser"    #User name of the ftp server
    PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"    #Password to connect to the server is variable and can be accessesd by visiting the link --> https://dlptest.com/ftp-test/
    local_path = "D:\\File_transfer_automator\\downloaded_files"    #Absolute path to local directory where the files from client server are temporarily downloaded before transferring to internal netwrok
    internal_server_path = "D:\\transferred_files_internal"    #Absolute path to the internal network

    def __init__(self):
        pass


    #Metod to download the files from client server    
    def file_downloader(self):

        logging.basicConfig(filename='transfer_status.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')    #This line of code sets up a basic configuration for logging in Python. It creates a log file named "transfer_status.log"

        ftp_server = ftplib.FTP(FileTransfer.HOSTNAME, FileTransfer.USERNAME, FileTransfer.PASSWORD)    #Establishing a connection to the FTP server using the ftplib library, passing in the hostname, username, and password for authentication.
        files = ftp_server.nlst()    #Creating a list of the files found in the server

        if not os.path.exists(FileTransfer.local_path):   #If the local path for downloading the files doesn't exist, create the path according to local path class variable declared above
            os.makedirs(FileTransfer.local_path)

        #Iterating over the files found in the server
        for file in files:
            if (file not in os.listdir(FileTransfer.internal_server_path)):    # Checking and if the files already do not exist in the internal network try to download the file
                try:
                    
                    with open(os.path.join(FileTransfer.local_path, file), "wb") as f:
                        ftp_server.retrbinary(f"RETR {file}", f.write)    #Opening and downloading the file by passing the RETR command to ftp_server.retrbinary

                    logging.info('File "{0}" downloaded sucessfully'.format(file))    #logging the success message for each file that is downloaded to the log file
                    
                except Exception as e:
                    logging.error('Error downloading or opening file: {0}. Name of file: {1}'.format(str(e), file))    #if there has been an error in downloading or opening the file, logging the error to log file
            else:
                continue


    # Method to transfer the file to internal network from local directory
    def file_transfer(self):

        self.file_downloader()    #First call the downloader method to download the files
        for file in os.listdir(FileTransfer.local_path):    #Iterate over all the files in the download folder
            try: 
                source_path = os.path.join(FileTransfer.local_path, file)    #Creating the source path by joining the file name to the file download path
                destination_path = os.path.join(FileTransfer.internal_server_path, file)    #Creating the destination path by joining the file name to the internal network path
                shutil.move(source_path, destination_path)    #using shutil library to transfer the files from local directory to internal network

            except Exception as e:
                    logging.error('Error transferring file: {0}. File name: {1}.  #Please check the source and destination PATHS'.format(str(e),file))  #Logging the error message if an exception was raised while transferring
        
        logging.info("All files transferred successfully to internal server...")    #Logging success message if all the files have been transferred without any issue
        

    




        