from dataclasses import dataclass
from dataclasses_json import dataclass_json,LetterCase 
import uuid
from api.flows.base.BaseFlowTacRegister import BaseFlowTacRegister
from api.models import Tac 
from api.flows.base.LogSeverity import LogSeverity

@dataclass_json
@dataclass
class FlowTacRegisterResult():
    context_tac_code:uuid = uuid.UUID(int=0)
    customer_code:uuid = uuid.UUID(int=0)
    email:str = ""
    user_code_value:uuid = uuid.UUID(int=0)
    utc_offset_in_minutes:int = 0
    role_name_csv_list:str = ""
    api_key:str = ""

    def __init__(self): 
        pass

class FlowTacRegister(BaseFlowTacRegister):
    def __init__(self): 
        super(FlowTacRegister, self).__init__() 
    
    def process(self,
        tac: Tac,
        email:str,
        password:str,
        confirm_password:str,
        first_name:str,
        last_name:str
        ) -> FlowTacRegisterResult:

        super()._log_message_and_severity(LogSeverity.information_high_detail, "Start")
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Code::" + str(tac.code))

        super()._process_validation_rules(
            tac,
            email,
            password,
            confirm_password,
            first_name,
            last_name,
        )

        super()._throw_queued_validation_errors()

        customer_code_output = uuid.UUID(int=0)
        email_output = ""
        user_code_value_output = uuid.UUID(int=0)
        utc_offset_in_minutes_output = 0
        role_name_csv_list_output = ""
        api_key_output = ""

        super()._log_message_and_severity(LogSeverity.information_high_detail, "Building result")
        result = FlowTacRegisterResult() 
        result.customer_code = customer_code_output
        result.email = email_output
        result.user_code_value = user_code_value_output
        result.utc_offset_in_minutes = utc_offset_in_minutes_output
        result.role_name_csv_list = role_name_csv_list_output
        result.api_key = api_key_output
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Result:" + result.to_json())

        super()._log_message_and_severity(LogSeverity.information_high_detail, "End")


        return result


    