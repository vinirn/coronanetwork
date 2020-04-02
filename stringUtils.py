def replaceURLEncoding(content):
    newcontent = content
    newcontent = newcontent.replace(r'&#39;',"'")
    newcontent = newcontent.replace(r'\xc3\x81',r'Á')
    newcontent = newcontent.replace(r'\xc3\x8d',r'Í')
    newcontent = newcontent.replace(r'\xc3\xa1',r'á')
    newcontent = newcontent.replace(r'\xc3\xa2',r'â')
    newcontent = newcontent.replace(r'\xc3\xa3',r'ã')
    newcontent = newcontent.replace(r'\xc3\xa7',r'ç')
    newcontent = newcontent.replace(r'\xc3\xa9',r'é')
    newcontent = newcontent.replace(r'\xc3\xaa',r'ê')
    newcontent = newcontent.replace(r'\xc3\xad',r'í')
    newcontent = newcontent.replace(r'\xc3\xb3',r'ó')
    newcontent = newcontent.replace(r'\xc3\xb4',r'ô')
    newcontent = newcontent.replace(r'\xc3\xb5',r'õ')
    newcontent = newcontent.replace(r'\xc3\xba',r'ú')
    newcontent = newcontent.replace(r'\xc3\xbc',r'ü')
    return(newcontent)

def getQuotesParam(content,param,startpos):
    paramStart = content.find(param+r'="',startpos)
    paramEnd = content.find(r'"',paramStart+len(param)+2)
    paramValue = content[(paramStart+len(param)+2):(paramEnd)]
    paramValue = replaceURLEncoding(paramValue)
    return(paramValue, paramEnd)