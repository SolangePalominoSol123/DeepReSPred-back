CONFIG_FILENAME="config"
keys={
    "ACCESS_KEY_ID": "ASIA6RSSFTG2GESXLLB6",
    "ACCESS_SECRET_KEY": "7AUo81bmgmpyOXHTVXFr5Tav3NJ3Ub6FduWHOgAH",
    "AWS_SESSION_TOKEN": "FwoGZXIvYXdzEBUaDAAFg6LgVW/07218kyLCAesqNRrOcmQ1ghI9LN1vlI76GvOlUvwR1D9zai0YR5xEMybFIAVipA+dGCrL2/i9V4Txsgrn+IauarRDPkZjXO8QzIrF3ntrVNgts3+ci+Pcz0AN9gzd7C18qnEqvQUEfT5eKHiNnn7rkqyEUqAQ1Dovqrhq056zVnC4PGTyktb6lNQYWABrifEOdFQr7/RPYbJdh4x+MMQQ47baRzYY0J2gS/s0BS0lU8PVyDdEwi4FEjYory/sbib/ZPM8Z90I4HfOKMGWkY0GMi04uE1ksG/5mEGOTCFvunT28N/aHXEKg8N0TscWO4UFEIBYjodoCHTVIsxZeB4="
}
BUCKET_NAME="deeprespred-bucket-files"
IP_INFO_TOKEN="61df6841805a0f"

BASE_DIR_REPO="/home/ubuntu/DeepReSPred-back"

BASE_PATH=BASE_DIR_REPO+"/back_project"
ALGORITHM_FOLDER=BASE_PATH+"/deepReSPred"                           #Directory with run_repeat_prediction.sh and MappingFasta.py
DAEMON_FOLDER=BASE_PATH + "/autProcess"                             #Directory where daemon proccesing will work
UPLOAD_FOLDER=DAEMON_FOLDER + "/filesInFolder"                      #Directory where input data from front-end will be saved to upload it to S3
DAEMON_QUEUE_FOLDER=DAEMON_FOLDER + "/queueReq"                     #Directory where a file with ID request will be created as a flag to daemon queue
ALGORITHM_PROCESSING=DAEMON_FOLDER + "/processingPred"              #Directory where the prediction algorithm will work
FILES_DOWNLOADED=DAEMON_FOLDER + "/filesDownloaded"                 #Directory as support to saved files downloaded from S3, this files will be deleted after their use
S3_UPLOAD_DIR=DAEMON_FOLDER + "/s3UploadDir"                 #Directory where some files could be in order to upload them to S3 from local

#URL_BACK_END_DEEPRESPRED = "http://localhost:9997/api/"
#URL_FRONT_END_DEEPRESPRED="http://192.168.1.13:8080/"

URL_BACK_END_DEEPRESPRED = "http://ec2-52-7-202-195.compute-1.amazonaws.com:9997/api/"
URL_FRONT_END_DEEPRESPRED="http://ec2-44-199-91-203.compute-1.amazonaws.com/"
