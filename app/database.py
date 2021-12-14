"""Defines all the functions related to the database"""
from app import db

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("Select * from Cities order by Cities.City_ID desc LIMIT 30;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "id": result[0],
            "city": result[1],
            "country": result[5],
            "latitute": result[3],
            "longitude": result[4],
            "population": result[10],
            "valid_or_not": result[11]
        }
        todo_list.append(item)

    return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update Cities set population = "{}" where City_ID = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()


def insert_new_task(text: str) ->  int:
    conn = db.connect()
    query = 'Insert Into Cities(city) VALUES ("{}");'.format(text)
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id


def remove_task_by_id(task_id: int) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From Cities where City_ID={};'.format(task_id)
    conn.execute(query)
    conn.close()

def get_tropical_city() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select distinct Temp.city, Temp.country, Temp.population, Temp.lat, Temp.lng "
                                 "from (Select * from Attractions NATURAL JOIN City_Attraction JOIN Cities USING(City_ID) "
                                 "WHERE Attractions.Having_Animals = 'TRUE') AS Temp NATURAL JOIN City_Environment "
                                 "WHERE City_Environment.Climate_Type = 'tropical' LIMIT 15;").fetchall()
    conn.close()
    item_list = []
    for result in query_results:
        item = {
            "city": result[0],
            "country": result[1],
            "population": result[2],
            "latitute": str(result[3]),
            "longitude": str(result[4])
        }
        item_list.append(item)

    return item_list

def get_culture_city() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select Country, MuseumNumber from (Select Country, Count(City_ID) AS MuseumNumber from City_Attraction LEFT JOIN Cities USING(City_ID) NATURAL JOIN Attractions WHERE Attractions.Attraction_Type = 'museum' GROUP BY Country) AS temp WHERE temp.MuseumNumber >= 3 LIMIT 15;").fetchall()
    conn.close()
    item_list = []
    for result in query_results:
        item = {
            "country": result[0],
            "numberofmuseums": result[1]
        }
        item_list.append(item)

    return item_list

def get_good_accommodation() -> dict:
    conn = db.connect()
    query_results = conn.execute('Call Result3();')
    conn.close()
    item_list = []
    for result in query_results:
        item = {
            "city": result[0],
            "averageTemperature": result[1],
            "possibilityToFindAAccommodationWithFreeWifi": result[2],
            "averageRatingOfAccommodations":result[3],
            "rankingOfaccommodations":result[4]
        }
        item_list.append(item)
    return item_list


def search_city(city: str) -> dict:
    conn = db.connect()
    query = 'Select * from Cities WHERE city = "{}";'.format(city)
    query_results = conn.execute(query).fetchall()
    conn.close()
    item_list = []
    for result in query_results:
        item = {
            "city": result[1],
            "country": result[5],
            "population": result[10]
        }
        item_list.append(item)
    return item_list
