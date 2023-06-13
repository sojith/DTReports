import os
import json
import datetime
import re
for filename in os.listdir("./inputFiles"):


        f = open("./inputFiles/"+filename, "rt")
        data = json.load(f)
        f.close()
        for x in data['problems']:
        #        print(x['displayId'] + "," + x['title'] + "," + x['impactLevel'] + "," + x['severityLevel'] + "," + x['status'] + "," + x['affectedEntities'][0]['name'] + "," + re.sub("'(.*)","",re.sub("(.*)mz-az-uk-","",str(x['managementZones']))) + "," + str(datetime.datetime.fromtimestamp(x['startTime']/1000)) + "," + str(datetime.datetime.fromtimestamp(x['endTime']/1000)) )
                print(x['displayId'] + "," + x['title'] + "," + x['impactLevel'] + "," + x['severityLevel'] + "," + x['status'] + "," + x['affectedEntities'][0]['name'] + "," + re.sub("'(.*)","",re.sub("(.*)mz-az-uk-","",str(x['managementZones']))) + "," + str(datetime.datetime.fromtimestamp(x['startTime']/1000)) + "," + str(datetime.datetime.fromtimestamp(x['endTime']/1000)) )#+ str(datetime.datetime.fromtimestamp(x['endTime']/1000))  )                              
        #        print(x)
