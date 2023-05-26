import Excelfile as ef
from locust import HttpUser, task,between
import jsonBuilder as builder

file_path = 'assets/test.xlsx'
assigned_variables = ef.assign_excel_columns_to_variables(file_path)
endpoint_url = "/"
class Myuser(HttpUser):
    wait_time = between(5,10)
    @task
    def my_task(self):
        json = {
            "idBrand" : assigned_variables['IdBrand'],
            "idDealer" : assigned_variables['IdDealer'],
            "idSubBrand" : assigned_variables['IdSubbrand']
        }
        self.client.get("{endpoint_url}",data=json)

def main():
    file_path = 'assets/test.xlsx'
    assigned_variables = ef.assign_excel_columns_to_variables(file_path)
    print(assigned_variables['IdBrand'])
    print(assigned_variables['IdCategory'])
    print(assigned_variables['Amount'])
    print(assigned_variables['IdClassification'])
    print(assigned_variables['IdDealer'])
    print(assigned_variables['IdSubBrand'])
    print(assigned_variables['Year'])

if __name__ == "__main__":
    Myuser()