# File Transfer Automator with FastAPI

Instructions for usage:

Clone the repository into a local directory, ex: "file_transfer_automator

Navigate to "/file_transfer_automator" directory and run the command "pip install -r requirements.txt" to install the dependencies

update the hostname, password and file paths in the class variables of 'transfer_automator.py' as appropriate. 

Run the command "python -m uvicorn main.app:app --reload" to launch the application

Navigate to the link "http://127.0.0.1:8000" to use the application

The dashboard has a number input field and two buttons. The range of the number input field is from 0 (corresponding to 0:00 hrs) and 23 (corresponding to 23:00 hrs)

One of the two buttons allow the user to start the file transfer automation at scheduled time, indefinitely and the other allow the user to stop the service.

Every detail of download and transfer of each file is logged into the 'transfer_status.log' file.
