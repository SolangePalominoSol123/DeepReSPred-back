CONFIG_FILENAME="config"
keys={
    "ACCESS_KEY_ID": "",
    "ACCESS_SECRET_KEY": "",
    "AWS_SESSION_TOKEN": ""
}
BUCKET_NAME="deeprespred.pucp.edu.pe"
IP_INFO_TOKEN=""

BASE_DIR_REPO="/home/ladmin/DeepReSPred-back"

BASE_PATH=BASE_DIR_REPO+"/back_project"
ALGORITHM_FOLDER=BASE_PATH+"/deepReSPred"                           #Directory with run_repeat_prediction.sh and MappingFasta.py
DAEMON_FOLDER=BASE_PATH + "/autProcess"                             #Directory where daemon proccesing will work
UPLOAD_FOLDER=DAEMON_FOLDER + "/filesInFolder"                      #Directory where input data from front-end will be saved to upload it to S3
DAEMON_QUEUE_FOLDER=DAEMON_FOLDER + "/queueReq"                     #Directory where a file with ID request will be created as a flag to daemon queue
ALGORITHM_PROCESSING=DAEMON_FOLDER + "/processingPred"              #Directory where the prediction algorithm will work
FILES_DOWNLOADED=DAEMON_FOLDER + "/filesDownloaded"                 #Directory as support to saved files downloaded from S3, this files will be deleted after their use
S3_UPLOAD_DIR=DAEMON_FOLDER + "/s3UploadDir"                 #Directory where some files could be in order to upload them to S3 from local

URL_BACK_END_DEEPRESPRED = "http://backend:9997/api/"
URL_FRONT_END_DEEPRESPRED="http://deeprespred.duckdns.org/"

EMAIL_TOKEN = ""