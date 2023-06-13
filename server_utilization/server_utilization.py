import os
import json
import datetime
import re

host_ID = []
host_name = []
host_cpu_min = []
host_cpu_max = []
host_cpu_avg = []
host_mem_min = []
host_mem_avg = []
host_mem_max = []
host_os = []

disk_host_ID = []
disk_host_name = []
disk_ID = []
disk_name = []
disk_min = []
disk_avg = []
disk_max = []
disk_host_os = []

for filename in os.listdir("./inputFiles/metrics"):

        f = open("./inputFiles/metrics/"+filename, "rt")
        data1 = json.load(f)
        f.close()

        #Map of all hostnames and diskname
        for x in data1['result']:
                for y in x['data']:
                        if (x['metricId'] == 'builtin:host.cpu.usage:min:names'):
                                host_ID.append(y['dimensionMap']['dt.entity.host'])
                                host_name.append(y['dimensionMap']['dt.entity.host.name'])
                                host_cpu_min.append(0)
                                host_cpu_max.append(0)
                                host_cpu_avg.append(0)
                                host_mem_min.append(0)
                                host_mem_avg.append(0)
                                host_mem_max.append(0)
                                host_os.append("")
                        if (x['metricId'] == 'builtin:host.disk.usedPct:min:names'):
                                disk_host_ID.append(y['dimensionMap']['dt.entity.host'])
                                disk_host_name.append(y['dimensionMap']['dt.entity.host.name'])
                                disk_ID.append(y['dimensionMap']['dt.entity.disk'])
                                disk_name.append(y['dimensionMap']['dt.entity.disk.name'])
                                disk_min.append(0)
                                disk_avg.append(0)
                                disk_max.append(0)
                                disk_host_os.append("")

        #Map min CPU to hostnames                                


        for x in data1['result']:
                for y in x['data']:

                        #Map min CPU to hostnames
                        if (x['metricId'] == 'builtin:host.cpu.usage:min:names'):
                                for z in range(len(host_ID)):
                                        if( y['dimensionMap']['dt.entity.host'] == host_ID[z] ):
                                                host_cpu_min[z] = y['values'][0]
               

                        #Map max CPU to hostnames
                        if (x['metricId'] == 'builtin:host.cpu.usage:max:names'):
                                for z in range(len(host_ID)):
                                        if( y['dimensionMap']['dt.entity.host'] == host_ID[z] ):
                                                host_cpu_max[z] = y['values'][0]
                

                        #Map avg CPU to hostnames
                        if (x['metricId'] == 'builtin:host.cpu.usage:avg:names'):
                                for z in range(len(host_ID)):
                                        if( y['dimensionMap']['dt.entity.host'] == host_ID[z] ):
                                                host_cpu_avg[z] = y['values'][0]


                        #Map min Mem to hostnames
                        if (x['metricId'] == 'builtin:host.mem.usage:min:names'):
                                for z in range(len(host_ID)):
                                        if( y['dimensionMap']['dt.entity.host'] == host_ID[z] ):
                                                host_mem_min[z] = y['values'][0]
                                                

                        #Map max Mem to hostnames
                        if (x['metricId'] == 'builtin:host.mem.usage:max:names'):
                                for z in range(len(host_ID)):
                                        if( y['dimensionMap']['dt.entity.host'] == host_ID[z] ):
                                                host_mem_max[z] = y['values'][0]
                                

                        #Map avg Mem to hostnames
                        if (x['metricId'] == 'builtin:host.mem.usage:avg:names'):
                                for z in range(len(host_ID)):
                                        if( y['dimensionMap']['dt.entity.host'] == host_ID[z] ):
                                                host_mem_avg[z] = y['values'][0]


                        #Map min Disk to hostnames
                        if (x['metricId'] == 'builtin:host.disk.usedPct:min:names'):
                                for z in range(len(disk_ID)):
                                        if( y['dimensionMap']['dt.entity.disk'] == disk_ID[z] ):
                                                disk_min[z] = y['values'][0]

                        #Map max Disk to hostnames
                        if (x['metricId'] == 'builtin:host.disk.usedPct:max:names'):
                                for z in range(len(disk_ID)):
                                        if( y['dimensionMap']['dt.entity.disk'] == disk_ID[z] ):
                                                disk_max[z] = y['values'][0]

                        #Map avg Disk to hostnames
                        if (x['metricId'] == 'builtin:host.disk.usedPct:avg:names'):
                                for z in range(len(disk_ID)):
                                        if( y['dimensionMap']['dt.entity.disk'] == disk_ID[z] ):
                                                disk_avg[z] = y['values'][0]
                                                
#Map OS Name
for filename2 in os.listdir("./inputFiles/os"):


        f2 = open("./inputFiles/os/"+filename2, "rt")
        data2 = json.load(f2)
        f2.close()
        for x2 in data2['entities']:
#                print(x2['properties']['osVersion'])

                for z in range(len(host_ID)):
                        if( x2['entityId'] == host_ID[z] ):
                                host_os[z] = x2['properties'].replace("@{osType=","").replace("}","")

                for z in range(len(disk_ID)):
                        if( x2['entityId'] == disk_host_ID[z] ):
                                disk_host_os[z] = x2['properties'].replace("@{osType=","").replace("}","")
                                

print("HostName" + "," + "OS" + "," + "Min CPU" + "," + "Avg CPU" + "," + "Max CPU" + "," + "Min Mem" + "," + "Avg Mem" + "," + "Max Mem")

for x in range(len(host_ID)):
        print(host_name[x] + "," + host_os[x] + "," + str(host_cpu_min[x]) + "," + str(host_cpu_avg[x]) + "," + str(host_cpu_max[x]) + "," + str(host_mem_min[x]) + "," + str(host_mem_avg[x]) + "," + str(host_mem_max[x]))

print("HostName" + "," + "OS" + "," + "FileSystem" + "," + "Min Disk" + "," + "Avg Disk" + "," + "Max Disk")

for x in range(len(disk_host_ID)):
        print(disk_host_name[x] + "," + disk_host_os[x] + "," + disk_name[x] + "," + str(disk_min[x]) + "," + str(disk_avg[x]) + "," + str(disk_max[x]))
