import Excelfile as ef
from locust import HttpUser, task,between
import jsonBuilder as builder

file_path = 'assets/test.xlsx'
assigned_variables = ef.assign_excel_columns_to_variables(file_path)
class Myuser(HttpUser):
    @task
    def my_task(self):
        endpoint_url = "/Classification.svc/V2/List"
        json = {
            "idBrand" : assigned_variables['IdBrand'],
            "idDealer" : assigned_variables['IdDealer'],
            "idSubBrand" : assigned_variables['IdSubBrand']
        }
        self.client.get(endpoint_url,data=json)

    @task
    def ProductInfo(self):
        endpoint_url = "/ProductInfo.svc/V2/List/"
        json = {
            "idBrand" : assigned_variables['IdBrand'],
            "idSubBrand" : assigned_variables['IdSubBrand'],
            "idClassification" : assigned_variables['IdClassification'],
            "idYear" : assigned_variables['Year'],
            "idVersion" : assigned_variables['IdVersion'],
            "idDealer" : assigned_variables['IdDealer'],
        }
        self.client.get(endpoint_url,data=json)


if __name__ == "__main__":
    Myuser()