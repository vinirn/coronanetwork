def removeStateName(cityName):
    newCityName = cityName
    newCityName = newCityName.replace(" (município)","")
    newCityName = newCityName.replace(" (Acre)","")
    newCityName = newCityName.replace(" (Alagoas)","")
    newCityName = newCityName.replace(" (Amapá)","")
    newCityName = newCityName.replace(" (Amazonas)","")
    newCityName = newCityName.replace(" (Bahia)","")
    newCityName = newCityName.replace(" (Ceará)","")
    newCityName = newCityName.replace(" (Espírito Santo)","")
    newCityName = newCityName.replace(" (Goiás)","")
    newCityName = newCityName.replace(" (Maranhão)","")
    newCityName = newCityName.replace(" (Mato Grosso)","")
    newCityName = newCityName.replace(" (Mato Grosso do Sul)","")
    newCityName = newCityName.replace(" (Minas Gerais)","")
    newCityName = newCityName.replace(" (Pará)","")
    newCityName = newCityName.replace(" (Paraíba)","")
    newCityName = newCityName.replace(" (Paraná)","")
    newCityName = newCityName.replace(" (Pernambuco)","")
    newCityName = newCityName.replace(" (Piauí)","")
    newCityName = newCityName.replace(" (Rio de Janeiro)","")
    newCityName = newCityName.replace(" (Rio Grande do Norte)","")
    newCityName = newCityName.replace(" (Rio Grande do Sul)","")
    newCityName = newCityName.replace(" (Roraima)","")
    newCityName = newCityName.replace(" (Rondônia)","")
    newCityName = newCityName.replace(" (Santa Catarina)","")
    newCityName = newCityName.replace(" (São Paulo)","")
    newCityName = newCityName.replace(" (Sergipe)","")
    newCityName = newCityName.replace(" (Tocantins)","")
    return(newCityName)

def getStateAbbreviation(stateName):
    stateAbbreviation = stateName
    
    if stateName.upper()=="ACRE": stateAbbreviation = "AC"
    if stateName.upper()=="ALAGOAS": stateAbbreviation = "AL"
    if stateName.upper()=="AMAPÁ": stateAbbreviation = "AP"
    if stateName.upper()=="AMAZONAS": stateAbbreviation = "AM"
    if stateName.upper()=="BAHIA": stateAbbreviation = "BA"
    if stateName.upper()=="CEARÁ": stateAbbreviation = "CE"
    if stateName.upper()=="DISTRITO FEDERAL (BRASIL)": stateAbbreviation = "DF"
    if stateName.upper()=="DISTRITO FEDERAL": stateAbbreviation = "DF"
    if stateName.upper()=="ESPÍRITO SANTO": stateAbbreviation = "ES"
    if stateName.upper()=="GOIÁS": stateAbbreviation = "GO"
    if stateName.upper()=="MARANHÃO": stateAbbreviation = "MA"
    if stateName.upper()=="MATO GROSSO": stateAbbreviation = "MT"
    if stateName.upper()=="MATO GROSSO DO SUL": stateAbbreviation = "MS"
    if stateName.upper()=="MINAS GERAIS": stateAbbreviation = "MG"
    if stateName.upper()=="PARÁ": stateAbbreviation = "PA"
    if stateName.upper()=="PARAÍBA": stateAbbreviation = "PB"
    if stateName.upper()=="PARANÁ": stateAbbreviation = "PR"
    if stateName.upper()=="PERNAMBUCO": stateAbbreviation = "PE"
    if stateName.upper()=="PIAUÍ": stateAbbreviation = "PI"
    if stateName.upper()=="RIO GRANDE DO NORTE": stateAbbreviation = "RN"
    if stateName.upper()=="RIO GRANDE DO SUL": stateAbbreviation = "RS"
    if stateName.upper()=="RIO DE JANEIRO": stateAbbreviation = "RJ"
    if stateName.upper()=="RONDÔNIA": stateAbbreviation = "RO"
    if stateName.upper()=="RORAIMA": stateAbbreviation = "RR"
    if stateName.upper()=="SANTA CATARINA": stateAbbreviation = "SC"
    if stateName.upper()=="SÃO PAULO": stateAbbreviation = "SP"
    if stateName.upper()=="SERGIPE": stateAbbreviation = "SE"
    if stateName.upper()=="TOCANTINS": stateAbbreviation = "TO"

    return(stateAbbreviation)