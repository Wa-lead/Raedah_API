import codecs
from fastapi import FastAPI, UploadFile, File
import csv
from func_timeout import func_timeout, FunctionTimedOut
import time


app = FastAPI()

@app.post('/topProduct')
async def topProduct(products: UploadFile = File(...)):  # this is to accept file types
    try:
        # products are wrapped by list because this module takes only 1 argument
        return func_timeout(2, find_top_product, args=([products]))
    except FunctionTimedOut:
        return {'Error': 'Sorry, time allowed excceded'}


# -------- helping method to find top rated product
def find_top_product(products):
    #to simulate timeout uncomment the following line
    # time.sleep(4)
    """
    format:
    id,product_name,average_rating
    """
    try:
        csv_reader = csv_reader = csv.reader(
        codecs.iterdecode(products.file, 'utf-8'))
        next(csv_reader)  # skips the attributes
        items = [row for row in csv_reader]
        # return the max based on the index 2 (the rating) -- also forces exception of type is not a digit
        top_rated = max(items, key=lambda x: float(x[2]))

        # timeout = True
        return {
            "top_product": top_rated[1],
            "product_rating": top_rated[2]
        }
    except:
        return{
            'Format_Error': "Please check the format ( id,product_name,average_rating )"
        }

