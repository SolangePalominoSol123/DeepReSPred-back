CONFIG_FILENAME="config"
keys={
    "ACCESS_KEY_ID": "ASIA6RSSFTG2NFJFOVL5",
    "ACCESS_SECRET_KEY": "QKyU3/3xvhh1ul6PYVfYg+xz9PQkciPA2TV+QV6l",
    "AWS_SESSION_TOKEN": "FwoGZXIvYXdzEAIaDM3C8jf+p7pds+m4BSLCAXS8i8qQJZz21aSj6plgsE7g7F8aczfTAzIOFha08KITqy+2XeS+6KovFzDYfOIUbYnFw8PBl1MY4T3zzjxzEWiH9Tsu9/7KzqTbr21XiVKWZOtARta6YD+87YqNpVuXlFs54SzNs66cvctpgjS579wliBFMxfS8Db+IADc1hvs7l7G9qYXVhsrClaZ60+RRYv4a1iLvKsOK9x5ooguSkHm41quq5RDPOUOuffelDAYOUlh+dQcfwfJjYzG5v6HwD6JMKKL5jI0GMi2padFbLWRaqk1qbUEA5pbv9pXqOUg7SF5lGk+zSKuRupm/qB5e4BHZZ1XUzJQ="
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
