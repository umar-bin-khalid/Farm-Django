from dataclasses import dataclass, asdict, field
import json
import traceback
from dataclasses_json import dataclass_json,LetterCase
from typing import List
import uuid
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet,ViewSet
from rest_framework_dataclasses.serializers import DataclassSerializer
from rest_framework import status
from api.flows import FlowTacRegister,FlowTacRegisterResult
from api.flows import FlowTacRegisterInitObjWF,FlowTacRegisterInitObjWFResult 
from api.flows import FlowValidationError
from api.models import Tac
from dacite import from_dict
import marshmallow_dataclass
import logging
import marshmallow.exceptions 

### response
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidationError:
    property:str = ""
    message:str  = ""

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PostResponse:
    success:bool = False
    message:str = ""
    validation_errors:List[ValidationError] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TacRegisterPostResponse(PostResponse):
    customer_code:uuid = uuid.UUID(int=0)
    email:str = ""
    user_code_value:uuid = uuid.UUID(int=0)
    utc_offset_in_minutes:int = 0
    role_name_csv_list:str = ""
    api_key:str = ""

    def load_flow_response(self,data:FlowTacRegisterResult):
        self.customer_code = data.customer_code
        self.email = data.email
        self.user_code_value = data.user_code_value
        self.utc_offset_in_minutes = data.utc_offset_in_minutes
        self.role_name_csv_list = data.role_name_csv_list
        self.api_key = data.api_key

### request. expect camel case. use marshmallow to validate.
@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class TacRegisterPostModel:
    email:str = ""
    password:str = ""
    confirmPassword:str = ""
    firstName:str = ""
    lastName:str = ""


### init response
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetInitResponse:
    success:bool = False
    message:str = ""
    validation_errors:List[ValidationError] = field(default_factory=list)

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TacRegisterGetInitResponse(GetInitResponse):
    email:str = ""
    password:str = ""

    def load_flow_response(self,data:FlowTacRegisterInitObjWFResult):
        self.email = data.email
        self.password = data.password
 
  


class TacRegisterViewSet(ViewSet): 

    @action(detail=False, methods=['post'],url_path=r'(?P<tacCode>[0-9a-f-]{36})')
    def submit(self, request, tacCode=None, *args, **kwargs): 
        logging.debug('TacRegisterViewSet.submit post start. tacCode:' + tacCode)

        response = TacRegisterPostResponse()
         
        try:
            logging.debug("Request:" + json.dumps(request.data))

            logging.debug("get schema")
            schema = marshmallow_dataclass.class_schema(TacRegisterPostModel)()
             
            logging.debug("validating request...")
            request = schema.load(request.data)  

            logging.debug("loading model...")
            tac = Tac.objects.get(code=tacCode)
            
            logging.debug("process flow...")
            flow = FlowTacRegister()
            flowResponse = flow.process(
                tac,
                request.email,
                request.password,
                request.confirmPassword,
                request.firstName,
                request.lastName,
            ) 

            response.load_flow_response(flowResponse);
            response.success = True
            response.message = "Success."

        except marshmallow.exceptions.ValidationError as se:
            response.success = False
            response.message = "Schema validation error. Invalid Request" 
             
        except TypeError as te: 
            response.success = False
            response.message = "Invalid Request" 
            
        except FlowValidationError as ve:
            response.success = False 
            response.validation_errors = list()
            for key in ve.error_dict:
                response.validation_errors.append(ValidationError(key,ve.error_dict[key]))

        except Exception as e:
            response.success = False
            traceback_string = "".join(traceback.format_tb(e.__traceback__))
            response.message = str(e) + " traceback:" + traceback_string
 
        logging.debug('TacRegisterViewSet.submit get result:' + response.to_json())

        responseDict = json.loads(response.to_json())
        
        return Response(responseDict,status=status.HTTP_200_OK) 
    
    
    @action(detail=False, methods=['get'],url_path=r'(?P<tacCode>[0-9a-f-]{36})/init')
    def init(self, request, tacCode=None, *args, **kwargs):
        logging.debug('TacRegisterViewSet.init get start. tacCode:' + tacCode)
        
        response = TacRegisterGetInitResponse() 
         
        try: 
 
            logging.debug("loading model...")
            tac = Tac.objects.get(code=tacCode)
            
            logging.debug("process flow...")
            flow = FlowTacRegisterInitObjWF()
            flowResponse = flow.process(
                tac, 
            ) 
 
            response.load_flow_response(flowResponse);
            response.success = True
            response.message = "Success."
            
        except TypeError as te: 
            response.success = False
            traceback_string = "Invalid Request" 
            
        except FlowValidationError as ve:
            response.success = False 
            response.validation_errors = list()
            for key in ve.error_dict:
                response.validation_errors.append(ValidationError(key,ve.error_dict[key]))

        except Exception as e:
            response.success = False
            traceback_string = "".join(traceback.format_tb(e.__traceback__))
            response.message = str(e) + " traceback:" + traceback_string
 
        logging.debug('TacRegisterViewSet.init get result:' + response.to_json())

        responseDict = json.loads(response.to_json())
        
        return Response(responseDict,status=status.HTTP_200_OK) 