FAKE_AVAILABILITY={ 
    "2025-11-11": "Available FROM 4:00 pm TO 5:00 pm",
    "2025-11-12": "Available FROM 10:00 am TO 11:00 am",
    "2025-11-13": "Busy all day",
}
def get_availability(date_str:str)->dict[str, str]:
    """
    Simulates checking Jeff's availability on a specific date.
    Args:
        date_str (str): A date in ' YYYY-MM-DD' format.
    Returns:
        dict: a SALL json-LIKE DITIONARY WITH AVAILABILITY INFO.
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