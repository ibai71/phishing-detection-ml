import requests as re
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from bs4 import BeautifulSoup
import pandas as pd
import feature_extraction as fe

disable_warnings(InsecureRequestWarning)

# NOTA: Cambia estas variables para procesar phishing o sitios legítimos.
# Configuración para SITIOS LEGÍTIMOS:
#url_filename = "top-1m.csv"
#output_file = "structured_data_legitimate.csv"
#label_value = 0

# Configuración para SITIOS PHISHING (descomenta para usar):
url_filename = "verified_online.csv"
output_file = "structured_data_phishing.csv"
label_value = 1

df = pd.read_csv(url_filename)
url_list = df['url'].tolist()

# Procesamos una muestra para no demorar la prueba inicial
begin_index = 0
end_index = 100 
collection_list = url_list[begin_index:end_index]

def normalize_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        return url
    return "http://" + url

collection_list = [normalize_url(url) for url in collection_list]

def create_structured_data(url_list):
    data_list = []
    for i in range(0, len(url_list)):
        try:
            response = re.get(url_list[i], verify=False, timeout=4)
            if response.status_code != 200:
                print(i, ". HTTP connection was not successful for the URL: ", url_list[i])
            else:
                soup = BeautifulSoup(response.content, "html.parser")
                vector = fe.create_vector(soup)
                vector.append(str(url_list[i]))
                data_list.append(vector)
        except re.exceptions.RequestException as e:
            print(i, "-->", e)
            continue
    return data_list

data = create_structured_data(collection_list)

columns = [
    "has_title", "has_input", "has_button", "has_image", "has_submit", "has_link",
    "has_password", "has_email_input", "has_hidden_element", "has_audio", "has_video",
    "number_of_inputs", "number_of_buttons", "number_of_images", "number_of_option",
    "number_of_list", "number_of_th", "number_of_tr", "number_of_href",
    "number_of_paragraph", "number_of_script", "length_of_title", "URL"
]

df = pd.DataFrame(data=data, columns=columns)
df['label'] = label_value
df.to_csv(output_file, mode='a', index=False)
print(f"Datos exportados a {output_file}")