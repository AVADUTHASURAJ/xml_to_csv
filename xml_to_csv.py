
import csv
import xml.etree.ElementTree as ET

# PARSE XML
xml = ET.parse('DLTINS_20210117_01of01.xml')
root = xml.getroot()

# CREATE CSV FILE
csvfile = open('DATA.csv','w',encoding='utf-8',newline='')
csv_writer = csv.writer(csvfile)

# ADD THE HEADER TO CSV FILE
csv_writer.writerow(['ID','Full Name','ClssfctnTp','CmmdtyDerivInd','NtnlCcy','Issr'])

# FOR EACH DATA
for i in root.findall("./{urn:iso:std:iso:20022:tech:xsd:head.003.001.01}Pyld/{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Document/{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FinInstrmRptgRefDataDltaRpt/{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FinInstrm/{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}TermntdRcrd"):
    # EXTRACT DATA 
    Issr = i.find("{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Issr").text
    for x in i.findall("./{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FinInstrmGnlAttrbts"):
    
        ID= x.find("{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Id").text
        Full_Name = x.find("{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FullNm").text
        ClssfctnTp = x.find("{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}ClssfctnTp").text
        CmmdtyDerivInd = x.find("{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}CmmdtyDerivInd").text
        NtnlCcy = x.find("{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}NtnlCcy").text
    csv_line = [ID,Full_Name,ClssfctnTp,CmmdtyDerivInd,NtnlCcy,Issr]
    
    # ADD A NEW ROW TO CSV FILE
    csv_writer.writerow(csv_line)

# CLOSE THE CSV FILE
csvfile.close()