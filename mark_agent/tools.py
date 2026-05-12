FAKE_AVAILABILITY={ 
    "2025-11-09": "Available FROM 4:00 pm TO 5:00 pm",
    "2025-11-08": "Available FROM 10:00 am TO 11:00 am",
    "2025-11-10": "Busy all day",
}
def get_availability(date_str:str)->dict[str, str]:
    """
    Simulates checking Mark's availability on a specific date.
    Args:
        date_str (str): A date in ' YYYY-MM-DD' format.
    Returns:
        dict: a SMALL json-LIKE DICTIONARY WITH AVAILABILITY INFO.
    """
    if not date_str:
        return {"status": "error", "message": "No date provided"}
    availability=FAKE_AVAILABILITY.get(date_str)
    if availability:
        return{
            "status": "completed",
            "message":f"On {date_str}, Jeff is {availability}"
        }
    return {
        "status":"input_required",
        "message":f"He is busy on {date_str}. Please try another date.",
    }
from crewai.tools import BaseTool
class AvailabilityTool(BaseTool):
    name: str = "Calendar Availability Checker"
    description: str = "Checks Mark's availability for a given date."
    def _run(self,date: str) -> str:
        return get_availability(date)["message"]