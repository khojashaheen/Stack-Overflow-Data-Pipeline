import azure.functions as func
import logging
import requests, re
from bs4 import BeautifulSoup
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

func.HttpResponse.mimetype = 'application/json'
func.HttpResponse.charset = 'utf-8'

def scrapeWikiTableFromHTML(html_page):
    soup = BeautifulSoup(html_page.content, "html.parser")
    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    data = []
    index = 0
    for row in rows:
        cols = row.find_all('td')
        for col in cols:
            if (index==0):
                data_dict={}
                element = col.text.strip()
                element_clean = re.sub('((\[|\()[a-zA-Z0-9\s]*(\]|\)))', '', element)
                data_dict["Country"]=element_clean

            if (index==4):
                element = col.text.strip()
                element_clean = element.replace(",", "")
                if (element_clean.isnumeric()):
                    element_clean = int(element_clean)
                data_dict["Population"]=element_clean
                data.append(data_dict)
            index=(index+1)%6
    return data

@app.route(route="get_world_population")
def get_world_population(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = req.params.get('url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')

    if url:
        page = requests.get(url)
        table = scrapeWikiTableFromHTML(page)
        return func.HttpResponse(json.dumps(table))
    else:
        return func.HttpResponse("",
            status_code=200
        )
