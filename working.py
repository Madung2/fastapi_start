from pdb import post_mortem
from pickle import GET
from shutil import get_unpack_formats
from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
##일종의 api 오브젝트를 생성

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


# @app.get('/')
# def home():
#     return {'Data':'아무말'}

# @app.get('/about')
# def about():
#     return {'Data': 'About'}



inventory = {}
    # 1:{
    #     'name':'milk',
    #     'price':3.99,
    #     'brand': 'Regular'
    # }


#패스 사용법
@app.get('/get-item/{item_id}/')
def get_item(item_id:int = Path(None, description="The ID of the item youd like to view", gt=0)): #첫번째 None 디폴트값
    return inventory[item_id]


#쿼리파라미터 http://127.0.0.1:8000/get-by-name?name=milk
@app.get('/get-by-name/{item_id}')
def get_item(*, item_id:int, name:Optional[str] = None, test:int): 

    #=None을 붙여주면 optional이 된다 
    # Optional을 붙여주면 그냥 읽기 쉬워짐\
    # 파이썬에서 필수변수를 옵션변수 뒤에 붙여주면 에러를 뱉는데 이때 *을 앞에 달면 해결!
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {'Data':'Not found'}


#post api!
@app.post('/create-item/{item_id}')
def create_item(item_id:int, item:Item):
    if item_id in inventory:
        return {'Error': 'Item Id already exists'}
    inventory[item_id] = item #아이템 오브젝트를 넣어주는 것
    return inventory[item_id]



# put api

@app.put('/update-item/{item_id}')
def update_item(item_id:int, item:Item):
    if item_id not in inventory:
        return {'Error': 'Item ID does not exist'}
    inventory[item_id].update(item)
    return inventory[item_id]