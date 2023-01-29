import time
import logging

from fastapi import FastAPI, status, HTTPException, Path, Query, Request
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    log.info(f"The time taken to process request is {process_time}")
    return response


class Person(BaseModel):
    name: str
    age: int
    address: Optional[str] = None
    occupation: str


class PersonUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[str] = None
    occupation: Optional[str] = None


PersonData = {}


@app.get('/')
def home():
    return 'Welcome home'


@app.get('/get_name/{name}')
def getName(name: str = Path(None, description="The name of the person to be filtered")):
    for idx in PersonData:
        if PersonData[idx].name == name:
            return PersonData[idx]
    raise HTTPException(status_code=404, detail="The person is not present")


@app.get('/get_by_id/{idx}')
def getNameByQuery(idx: int):
    if idx in PersonData:
        return PersonData[idx]
    raise HTTPException(status_code=404, detail="The person is not present")


@app.get('/get_by_query')
def getNameByQuery(name: str = Query(None, description="The name of the person to be filtered")):
    for idx in PersonData:
        if PersonData[idx].name == name:
            return PersonData[idx]
    raise HTTPException(status_code=404, detail="The person is not present")


@app.get('/get_by_query')
def getNameByQuery(name: str = Query(None, description="The name of the person to be filtered")):
    for idx in PersonData:
        if name in PersonData[idx]:
            return PersonData[idx]
    raise HTTPException(status_code=404, detail="The person is not present")


@app.post('/create_person/{idx}')
def createPerson(idx: int, item: Person):
    if idx in PersonData:
        raise HTTPException(status_code=400, detail="The person is already exists")
    PersonData[idx] = item
    return PersonData[idx]


@app.put('/update_person/{idx}')
def updatePerson(idx: int, item: PersonUpdate):
    if idx not in PersonData:
        raise HTTPException(status_code=404, detail="The person is not present")
    else:
        if item.name is not None:
            PersonData[idx].name = item.name
        if item.age is not None:
            PersonData[idx].age = item.age
        if item.address is not None:
            PersonData[idx].address = item.address
        if item.occupation is not None:
            PersonData[idx].occupation = item.occupation
    return PersonData[idx]


@app.delete('/delete_person/{idx}')
def deletePerson(idx: int, item: Person):
    if idx not in PersonData:
        raise HTTPException(status_code=404, detail="The person not found")
    del PersonData[idx]
    return HTTPException(status_code=410, detail='The person is deleted')
