from constants import BASE_PATH
from constants import URL_FRONT_END_DEEPRESPRED
import yagmail
import keyring

img = BASE_PATH + '/DeepReSPred_Logo2.png'

def getEmailConfig():
    emailSender = yagmail.SMTP("deeprespred@gmail.com")
    return emailSender

def sendEmail(receiver, files, type, idRequest):
    yag = getEmailConfig()

    if type==1:
        subject="[DeepReSPred] Confirmation of registered prediction request"
        body="DeepReSPred has received successfully your prediction request. \n\n" + \
                "You will be able to know the status of the processing or the results of your prediction request by entering the following identifier in the search section of the web service: " + \
                str(idRequest)
        files=[]
    else:
        subject="[DeepReSPred] Results of prediction request"

        if len(files)>0:
            body="DeepReSPred has processed successfully your prediction request with ID " + str(idRequest) + ". \n\n" + \
                "You will be able to know the status of the processing and the results of your prediction request by entering the request identifier in the search section of the web service.\n\n"  + \
                "Additionally, in this email you are sent the results obtained. Find them in the attachments section.\n\nThanks!"
        else:
            body="DeepReSPred has processed your prediction request with ID " + str(idRequest) + ". \n\n" + \
                "You will be able to know the status of the processing of your prediction request by entering the request identifier in the search section of the web service.\n\n"  + \
                "Unfortunately, the algorithm was unable to obtain any predictions from the data provided in the request. However, we trust that we can give you predictions with other families of repeat proteins.\n\nThanks!"
    
    html=   '<h2>Hello!</h2>' + \
            '<h4 style="font-weight:300">'+ body +'</h4>' + \
            '<h4 style="font-weight: bold;"> Prediction Request ID: ' + str(idRequest) + '</h4>' + \
            '<a href="'+URL_FRONT_END_DEEPRESPRED+str(idRequest)+'">Go to DeepReSPred Web!</a>'+ \
            '<h3>.....</h3>' + \
            '<h3>DeepReSPred Team</h3>' 

    yag.send(
        to = receiver,
        subject = subject,
        contents = [yagmail.inline(img), html], 
        attachments = files
    )

#yagmail.register('deeprespred@gmail.com', '')

#sendEmail("correoprueba@dominio.com", [],1,"ASDOW")