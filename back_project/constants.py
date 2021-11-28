CONFIG_FILENAME="config"
keys={
    "ACCESS_KEY_ID": "ASIA6RSSFTG2C3C3L5VT",
    "ACCESS_SECRET_KEY": "e56t9h5VIu2ee2cFcWbaCC/Zke38l9IvKSnUE8ND",
    "AWS_SESSION_TOKEN": "FwoGZXIvYXdzEKX//////////wEaDOtriqlX09KetOGgayLCAR6yg4HWMQyX1FeAHpxDl/v8DQ7JT3s7RD650xeVKXGllSzoMq7C+MSc6o2nJrOhGASER+dF57sHS6KSis0gzsRMIudbxEwnEKIBD+DgY4JZHquyMQ8Yr9nzHCdHdgNj0JG+YYTrkFfnyDICHv0iYP/UURWzgkXKO0DppKylrJjjZY/WxP98q6XYNi2a7Erqe5ThmdXKvMP5k3CTg0TboNDhflqIxuj/XQ6uWL7LsBqavJ0skxcIn+wtkQ4WthHMHwHnKN2gwIwGMi0TWdowvB63Wqc6h0Aaimy3L7ZvV6f99EdquU6C/+tMUWVtXZxYZH9djTldJ58="
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
