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


def getStateName(stateAbbreviation):
    stateName = stateAbbreviation

    if stateAbbreviation.upper()=='ALL': stateName = "Brasil"
    if stateAbbreviation.upper()=="AC": stateName = "Acre"
    if stateAbbreviation.upper()=="AL": stateName = "Alagoas"
    if stateAbbreviation.upper()=="AM": stateName = "Amapá"
    if stateAbbreviation.upper()=="AM": stateName = "Amazonas"
    if stateAbbreviation.upper()=="BA": stateName = "Bahia"
    if stateAbbreviation.upper()=="CE": stateName = "Ceará"
    if stateAbbreviation.upper()=="DF": stateName = "Distrito Federal"
    if stateAbbreviation.upper()=="ES": stateName = "Espírito Santo"
    if stateAbbreviation.upper()=="GO": stateName = "Goiás"
    if stateAbbreviation.upper()=="MA": stateName = "Maranhão"
    if stateAbbreviation.upper()=="MT": stateName = "Mato Grosso"
    if stateAbbreviation.upper()=="MS": stateName = "Mato Grosso do Sul"
    if stateAbbreviation.upper()=="MG": stateName = "Minas Gerais"
    if stateAbbreviation.upper()=="PA": stateName = "Pará"
    if stateAbbreviation.upper()=="PB": stateName = "Paraíba"
    if stateAbbreviation.upper()=="PR": stateName = "Paraná"
    if stateAbbreviation.upper()=="PE": stateName = "Pernambuco"
    if stateAbbreviation.upper()=="PI": stateName = "Piauí"
    if stateAbbreviation.upper()=="RN": stateName = "Rio Grande do Norte"
    if stateAbbreviation.upper()=="RS": stateName = "Rio Grande do Sul"
    if stateAbbreviation.upper()=="RJ": stateName = "Rio de Janeiro"
    if stateAbbreviation.upper()=="RO": stateName = "Rondônia"
    if stateAbbreviation.upper()=="RR": stateName = "Roraima"
    if stateAbbreviation.upper()=="SC": stateName = "Santa Catarina"
    if stateAbbreviation.upper()=="SP": stateName = "São Paulo"
    if stateAbbreviation.upper()=="SE": stateName = "Sergipe"
    if stateAbbreviation.upper()=="TO": stateName = "Tocantins"

    return(stateName)
