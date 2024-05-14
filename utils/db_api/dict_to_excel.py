import pandas as pd
import requests

response = requests.get("https://crm.sifatdev.uz/sertificates/").json()
print(response[0])
key_list =["T/r","F.I.Sh","Lavozim","Hudud","Tuman","JShShIR","Telefon raqami","Sertifikat nomi","Sertifikatga havola"]
data={}
data = data.fromkeys(key_list)
data.update({"T/r":[i for i in range(1,len(response)+1)]})
data.update({"F.I.Sh":[i["last_name"]+" "+i["first_name"]+" "+i["middle_name"] for i in response]})
data.update({"JShShIR":[i["JSHSHR"] for i in response]})
data.update({"Sertifikatga havola":[i["sertificate_link"] for i in response]})
data.update({"Sertifikat nomi":[i["course"] for i in response]})

df = pd.DataFrame(data)

df.to_excel('data.xlsx', index=False)
