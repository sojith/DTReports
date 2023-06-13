# DTReports

**Server Reports**
Helps create Capacity reports - CPU (min,avg,max) , Memory utilization (min, avg, max) and Disk Space usage (min, max avg) for every server in your DT tenant

- server_utilization/OS.ps1 - Run this PS script first. It will call the Hosts API to get a list of all the hosts and their CPUs. It will run the Metrics API to get CPU (min,mx,avg), Memory (min,max,avg) and Disk space (min, max, avg) for every hst and filesystem in your tenantIt will write this data into seperate files
- 
- server_utilization/server_utilization.py - This python script will read the files which were created n the previous point. It will then output CSV values as follow host Name, min CPU, avg CPU, max CPU, min Mem, avg Mem, Max Mem. And also, host name, file system, min disk %, avg disk %, max disk %

**Alert Reports**
alert/alert_report.py - This puthon script will help create a csv report of all the problems generated, and their respective details. The input data in this case is the out put of the _Problems API_
