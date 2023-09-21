import requests
import datetime
import smtplib


def get_sheet_data():
    print("getting sheet data")

    sheety_get_url = "https://api.sheety.co/c4fe58003bb93f830d9482e9170f309a/flightdeals/sheet1"
    response = requests.get(url=sheety_get_url)

    sheet_data = response.json()

    return sheet_data


def edit_sheet_data(row_to_be_edited_id: int, data: dict):

    # PUT URL NEEDS OBJECT ID
    sheety_put_url = f"https://api.sheety.co/c4fe58003bb93f830d9482e9170f309a/flightdeals/sheet1/{row_to_be_edited_id}"

    sheety_put_headers = {
        'Content-type': 'application/json'
    }

    put_response = requests.put(url=sheety_put_url, json=data, headers=sheety_put_headers)

    return put_response.status_code, put_response.text


def get_city_iata(name):
    api_key = "e2OvF4upUl2ZsBJ5Dnm2IqYMM86G1xMs"

    endpoint = "https://api.tequila.kiwi.com/locations/query"

    params = {
        "term": name,
        "locale": "en - US",
        "location_types": "city",
        "limit": 1,
        "active_only": True
    }

    headers = {
        'accept': 'application/json',
        "apikey": "e2OvF4upUl2ZsBJ5Dnm2IqYMM86G1xMs"
    }

    response = requests.get(url=endpoint, params=params, headers=headers)

    iata = response.json()["locations"][0]["code"]

    return iata


def fill_iata_based_on_name():

    sheet_data_template = {
        "sheet1": {
            "city": "",
            "iataCode": "",
            "lowestPrice": 99999,
        }
    }
    sheet_rows = get_sheet_data()["sheet1"]

    for row in sheet_rows:
        city_name = row["city"]
        row_id = row["id"]
        city_iata = get_city_iata(city_name)

        data = sheet_data_template
        data["sheet1"]["city"] = city_name
        data["sheet1"]["iataCode"] = city_iata

        print(edit_sheet_data(row_id, data))


def get_flights_to(destination_city_iata: str, departure_city_iata: str = "Belgrade", min_stay: int = None, max_stay: int = None):

    endpoint = "https://api.tequila.kiwi.com/v2/search"

    api_key = "e2OvF4upUl2ZsBJ5Dnm2IqYMM86G1xMs"

    headers = {
        'accept': 'application/json',
        "apikey": "e2OvF4upUl2ZsBJ5Dnm2IqYMM86G1xMs"
    }

    from_iata = get_city_iata(departure_city_iata)
    to_iata = get_city_iata(destination_city_iata)

    dt = datetime.datetime.now()

    tomorrow = dt + datetime.timedelta(days=1)
    tomorrow = tomorrow.strftime("%d/%m/%Y")
    six_mo = dt + datetime.timedelta(days=6 * 30)
    six_mo = six_mo.strftime("%d/%m/%Y")

    from_date = tomorrow
    to_date = six_mo

    params = {
        "fly_from": from_iata,
        "fly_to": to_iata,
        "date_from": from_date,
        "date_to": to_date,
        "nights_in_dst_from": min_stay,
        "nights_in_dst_to": max_stay,
    }

    response = requests.get(url=endpoint, headers=headers, params=params)

    flights_list = response.json()["data"]

    return flights_list


def get_cheap_flights(lowest_price: int, departure_city_iata="Belgrade", destination_city_iata="BER", min_stay=5, max_stay=7):
    flights_list = get_flights_to(departure_city_iata=departure_city_iata,
                                  destination_city_iata=destination_city_iata,
                                  min_stay=min_stay,
                                  max_stay=max_stay)

    for flight in flights_list:
        if flight["price"] < lowest_price:
            print(f"{flight}")


def check_destinations_in_sheet():
    sheet_data = get_sheet_data()

    for row in sheet_data:
        get_cheap_flights(lowest_price=row["lowestPrice"], destination_city_iata=row["iataCode"])

    print(sheet_data)

check_destinations_in_sheet()
