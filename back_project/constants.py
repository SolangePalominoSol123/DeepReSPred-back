CONFIG_FILENAME="config"
BUCKET_NAME=""
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
CONSTANT_AWS_S3_KEY_JSON="constants_aws.json"                       #Path to json file with aws s3 keys


URL_BACK_END_DEEPRESPRED = "http://localhost:9997/api/"
URL_FRONT_END_DEEPRESPRED="http://frontendDomain/"

EMAIL_TOKEN = ""

#BD config
DB_USER=""
DB_PASS=""
DB_ADDR=""
DB_NAME=""