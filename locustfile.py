import Excelfile as ef
from locust import HttpUser, task,between
import jsonBuilder as builder
import functions as func

file_path = 'assets/test.xlsx'
assigned_variables = ef.assign_excel_columns_to_variables(file_path)
# Server ip or url to which the tests will be directed
www = 'http://localhost:29456'
# Timeout for every request
timeout_set = 60


class Myuser(HttpUser):
    def on_start(self):
        self.login()
    wait_time = between(2,10)

    # @task
    # def PanelPrincipal(self):
    #     url ="/ProdeskNet.html"
    #     self.client.get(url)

    #iniciar sesion
    def login(self):
        username = "admintelepro"
        password = "Generico.101"

        # request and set state variables for next request
        self.view_st, self.view_st_gen = func.get_hidden_elements(
            self.client.request("GET", "", name="1 Ini Get: /"))
        
        # initial login
        url_main = "/login.aspx"
        # payload raw text
        p_main = "__LASTFOCUS=&__EVENTTARGET=&__EVENTARGUMENT=&"
        p_main = p_main + "__VIEWSTATE=" + self.view_st + "&__VIEWSTATEGENERATOR=" + self.view_st_gen
        p_main = p_main + "%2FwEdAAjtrfc9bFlycPRNvd9GpAk4QUnBeTmJnrNhxmPOJ04KLLXwdJFqioFGQdCtVz1hJa0z0pbtemMeEG4g1PnXXStT1O%2F2WkqbDud7RMyNsu3snL7gUW5RdHnCkit5S48%2F25KHg6q%2FhgwvZ%2BXsyHR25sWJxIKTJ3pG1f%2FYoIrbO%2F2ZOR9sxDmPtN2zrGIyTBh9GJ%2BqACo%2F64K6tJ5UstwGY7Y0&txtUsu="+username+"&txtPwd="+password+"&btnAceptar=Ingresar&usuAcceso=&intentosAcceso=0"
        response = self.client.post(url_main, data=p_main, timeout=timeout_set)
        # response = self.client.post(url_main,headers=func.get_headers(www,url_main),data=p_main)
        if response.status_code == 200:
            print("Todo ok")
        else:
            print("Algo salio mal")

    
    

if __name__ == "__main__":
    Myuser()




    # @task
    # def my_task(self):
    #     endpoint_url = "/Classification.svc/V2/List"
    #     json = {
    #         "idBrand" : assigned_variables['IdBrand'],
    #         "idDealer" : assigned_variables['IdDealer'],
    #         "idSubBrand" : assigned_variables['IdSubBrand']
    #     }
    #     self.client.get(endpoint_url,data=json)