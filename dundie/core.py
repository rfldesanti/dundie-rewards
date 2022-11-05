"""Core module of dundie"""
import os
from csv import reader
from dundie.utils.log import get_logger
from dundie.database import connect, commit, add_person, add_movement

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database

    >>> len(load("assets/people.csv"))
    2
    >>> load("assets/people.csv")[0][0]
    'J'
    """
    try:

        csv_data = reader(open(filepath))
    except FileNotFoundError as e:
        log.error(str(e))
        raise e

    db = connect()
    people = []
    headers = ["name", "dept", "role", "email"]
    for line in csv_data:
        person_data = dict(zip(headers, [item.strip() for item in line]))
        pk = person_data.pop("email")
        person, created = add_person(db, pk, person_data)
        return_data = person.copy()
        return_data["created"] = created
        return_data["email"] = pk
        people.append(return_data)

    commit(db)
    return people


def read(**query):
    """Reads data from database and filters using query"""
    db = connect()
    return_data = []
    for pk, data in db["people"].items():

        dept = query.get("dept")
        if dept and dept != data["dept"]:
            continue

        # WALRUS / Assignement Expression - since Python 3.8
        if (email := query.get("email")) and email != pk:
            continue

        return_data.append(
            {
                "email": pk,
                "balance": db["balance"][pk],
                "last_movement": db["movement"][pk][-1]["date"],
                **data,
            }
        )
    return return_data


def add(value, **query):
    """Add value to each record on query"""
    people = read(**query)
    if not people:
        raise RuntimeError("Not found")

    db = connect()
    user = os.getenv("USER")
    for person in people:
        add_movement(db, person["email"], value, user)
    commit(db)
