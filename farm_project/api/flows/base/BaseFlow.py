import uuid
from api.models import Tac 
from .FlowValidationError import FlowValidationError 
from .LogSeverity import LogSeverity
import logging

class BaseFlow():
    __flow_name = ""
    queued_validation_errors:dict

    def __init__(self, flow_name:str): 
        self.__flow_name = flow_name
        self.queued_validation_errors = dict()

    def _add_validation_error(self, message:str):
        self._add_field_validation_error("", message)

    def _add_field_validation_error(self, field_name:str = "", message:str = ""):
        if field_name in self.queued_validation_errors:
            current_val = self.queued_validation_errors[field_name]
            self.queued_validation_errors[field_name] = current_val + ',' + message
        else:
            self.queued_validation_errors[field_name] = message
             

    def _throw_validation_error(self, message:str):
        self._throw_field_validation_error("", message)

    def _throw_field_validation_error(self, field_name:str, message:str):
        raise FlowValidationError(field_name,message,None)


    def _throw_queued_validation_errors(self):
        if len(self.queued_validation_errors) > 0:
            raise FlowValidationError(None,None,self.queued_validation_errors)
 
    def _log_exception(self, ex:Exception):   
        self._log_message_and_severity(LogSeverity.error_occurred,str(ex))

    def _log_message_and_severity(self, log_severity:int, message:str):    

        log_message = self.__flow_name + " " + message

        match log_severity:
            case LogSeverity.error_occurred:
                logging.error(log_message) 
            case LogSeverity.warning:
                logging.critical(log_message)
            case LogSeverity.information_low_detail:
                logging.warning(log_message)
            case LogSeverity.information_mid_detail:
                logging.info(log_message)
            case LogSeverity.information_high_detail:
                logging.debug(log_message)

    def _log_message(self, message:str):   
        self._log_message_and_severity(LogSeverity.information_high_detail,message)

 