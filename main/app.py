from fastapi import FastAPI, Request, Form
from main.transfer_automator import FileTransfer
from fastapi.templating import Jinja2Templates
import schedule
import time


app = FastAPI()    #Creating a FastAPI instance
templates = Jinja2Templates(directory="templates/") #Creating a template object with the .html file in templates directory

@app.get("/")
def form_post(request: Request):
    
    return templates.TemplateResponse('first_page.html', context ={'request':request}) # Returning the template response on application launch

@app.post("/")
def form_post(request: Request, status : str = Form(None), timer : int = Form(None) ): #If the user clicks on any of the buttons with the same name 'status', recieve the value of the button and the schedule
    print(timer)

    if status == 'Start File Transfer':
        if isinstance(timer,int) and int(timer) in range(1,24):    #If the user clicks on the 'Start File Transfer' button and if the value entered for scheduling file transfer is valid, starting the file transfer automation.

            automator = FileTransfer()    #Creating an instance of the FileTransfer class
            
            f_timer = '0'+str(timer)+':'+'00' if len(str(timer)) < 2 else str(timer)+':'+'00'    #The user enters an integer value between 0 and 23. Convert it to '00:00' format to be able to pass it as an argument to the scheduler
            schedule.every().day.at(f_timer).do(automator.file_transfer)    #Automate daily file transfer event at the input time by the user, using the 'schedule' library

            #schedule.every(int(timer)).minutes.do(automator.file_transfer)    #Schedule file transfer event every minute. #Uncomment for testing purposes

            while True:
                schedule.run_pending()    #Run the pending jobs in an infinite loop until the user presses the stop file transfer button
                time.sleep(1)
        else:
            #If the user input for scheduling the file transfer is invalid, notifying the user
            return templates.TemplateResponse('first_page.html', context={'request': request, 'message': "Please enter a valid hour in 24 hours format."})    

    else:
        print("stopped")
        automator = FileTransfer()
        schedule.cancel_job(automator.file_transfer)    #If the user clicks on 'Stop file Transfer', stopping the file transfer automation service.
        return templates.TemplateResponse('first_page.html', context={'request': request, 'message': "The automatic file transfer service has been stopped"})    

