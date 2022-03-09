CONFIG_FILENAME="config"
keys={
    "ACCESS_KEY_ID": "ASIA6RSSFTG2FL7Z7DRT",
    "ACCESS_SECRET_KEY": "VOSMDoWGtdKq/rK6UlAzaxHLdp1MW9Qdjh+Nx2Na",
    "AWS_SESSION_TOKEN": "FwoGZXIvYXdzECAaDOplmZBHFDy+mMstqiLCAcCwHd6TG7ckR7baH5ZPKYaA0OdyGLKhQcKqhu/vVUouuxVGQGHv36f/YdgRs5U+MtYRyUQ7X6Uy4XTrUqflg6jrh1pPl0DWZVdJzY1I+VLDn1z4v3j5fJ8dQN1ZUiVKAP2r1QO+rCi8I5slIrpIUFkNxBF36S+gJchUbngIYS3cQ0Fu9TH70U5CJ/EEF4z6dIde5J6nMtU5TXOI27DBCBOAYZwDQ6jzkV2Ay8SMvesZiy7nf7cteMqBKs+5XTAEVEybKNq7k40GMi2YAKhlMBorPebJNwUFFdkn7NBol3ji7+ihXLeAlmk30/F8MbjkZ/BQieNbhAI="
}
BUCKET_NAME="deeprespred.pucp.edu.pe"
IP_INFO_TOKEN="61df6841805a0f"

BASE_DIR_REPO="/home/ladmin/DeepReSPred-back"

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

URL_BACK_END_DEEPRESPRED = "http://54.156.135.177:9997/api/"
URL_FRONT_END_DEEPRESPRED="http://deeprespred.duckdns.org/"

EMAIL_TOKEN = "lmteuddclebbtssj"