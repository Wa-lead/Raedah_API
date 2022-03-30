from fastapi.testclient import TestClient
from Raedah_API import app



client = TestClient(app)

def test_normal():
    with open('dummy.csv') as f:
        response = client.post("/topProduct", files={'products': ('dummy.csv', f, 'text/csv', {'Expires': '0'})})
        print (response.json())
        assert response.status_code == 200
        assert response.json() == {
            "top_product": "Massoub gift card",
            "product_rating": " 5.0"
        }

def test_badformat():
    with open('faultyFile.csv') as f:
        response = client.post("/topProduct", files={'products': ('dummy.csv', f, 'text/csv', {'Expires': '0'})})
        print (response.json())
        assert response.status_code == 200
        assert response.json() == {
            'Format_Error': "Please check the format ( id,product_name,average_rating )"
        }
