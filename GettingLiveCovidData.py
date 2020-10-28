#get live covid data
#basicaly use in client server module
#pip insatll covid
from covid import Covid
I=Covid()

I.get_data()
I.get_status_by_country_name("India")
I.get_status_by_country_id(18)
