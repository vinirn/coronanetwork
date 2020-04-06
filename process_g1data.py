import csv
from City import City

def process_g1_data(day):

    txtfilename = "./data/corona/" + day + ".txt"
    csvfilename = "./data/corona/" + day + ".csv"

    with open(txtfilename, "r") as txtfile:
        with open(csvfilename, "w") as csvfile:
            for line in txtfile:
                line = line.strip()
                line = line.replace(".","")
                line = line.replace(", ",";")
                line = line.replace(",",";")
                line = line.replace("\t",";")
                print(line)
                if line.upper().find("NÃO INFORMADO")==-1:
                    csvfile.write(line+"\n")
