from flask import Blueprint
from flask_restful import Api


from resources.parameter import ParameterResource
from resources.statusrequest import StatusrequestResource
from resources.idRequest import IdRequestResource
from resources.request import RequestResource
from resources.endpoint import EndpointResource
from resources.file import FileResource
from resources.access import AccessResource
from resources.searchPred import SearchPredResource
from resources.s3file import S3FileResource
from resources.filexReqInfo import FilexReqInfoResource
from resources.existsPFAMreq import ExistsPFAMreqResource
from resources.resultsFilesxReq import ResultsFilesxReq
from resources.allFilesxReq import AllFilesxReq
from resources.sendEmail import SendEmailResource

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

api.add_resource(ParameterResource, "/parameter/")
api.add_resource(StatusrequestResource, "/statusrequest/")
api.add_resource(IdRequestResource, "/idrequest/")
api.add_resource(RequestResource, "/request/")
api.add_resource(EndpointResource, "/endpoint/")
api.add_resource(FileResource, "/file/")
api.add_resource(AccessResource, "/access/")
api.add_resource(SearchPredResource, "/searchpred/")
api.add_resource(S3FileResource, "/s3file/")
api.add_resource(FilexReqInfoResource, "/filexreqInfo/")
api.add_resource(ExistsPFAMreqResource, "/existsPFAMreq/")
api.add_resource(ResultsFilesxReq,"/resultsFilesxReq/")
api.add_resource(AllFilesxReq, "/allFilesxReq/")
api.add_resource(SendEmailResource, "/sendEmail/")