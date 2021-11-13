CONFIG_FILENAME="config"
keys={
    "ACCESS_KEY_ID": "ASIA6RSSFTG2J3SZEG46",
    "ACCESS_SECRET_KEY": "V57YrtFelnsfo9bGmliGlz5Z/os+bh5xKdsShpKJ",
    "AWS_SESSION_TOKEN": "FwoGZXIvYXdzEJH//////////wEaDCj++x2rzJsUq1wkmCLCAT8TvhNekrpWP/vbUqOputSyS0r/B9R21cGTcq0uJt/vefKVyjMiZ201iD40L5hc9dbX1etse3Yisx3Cr8/6LxrMV8mwnrB2JtsfXHFO0p+9MwYVMBET0qFuJTX6DbRlt7c81WW5S+v1+358aEIm6dHvDKrkVCkpj8qXSmz+qJP9dhPj4JJC5/eumQGmy185Bf+H4mh5mDnTZgzh9rytKXD1oAXq+c9H3JuOjZ1DX7LsV8K2ruvDlIeIJY0wh6oJk4X8KInuu4wGMi3+QjZqbDhtypuzBqd8oS45tbUtM0n9dBCSWVttO/arHT0V2va3gB6FVkJYdj0="
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
