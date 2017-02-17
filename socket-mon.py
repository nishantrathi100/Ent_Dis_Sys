import psutil

connections = psutil.net_connections()

validConnections = []

#Considering connections with non null, not empty laddr & raddr
for conn in connections:
	if (conn.laddr and conn.raddr) :
		validConnections.append(conn)


#get number of connections each PID is making
pidConnectionsCountDict = {};
for conn in validConnections:
	if (conn.pid in pidConnectionsCountDict) :
		pidConnectionsCountDict[conn.pid] = pidConnectionsCountDict[conn.pid] + 1;
	else:
		pidConnectionsCountDict[conn.pid] = 1;

#sort the list with max number of connections on top
pidConnectionsCountList = pidConnectionsCountDict.items()
pidConnectionsCountList.sort(key=lambda con: con[1], reverse=True)

#print pidConnectionsCountList
print "\"" + "pid" + "\",\"" + "laddr" + "\",\"" + "raddr" + "\",\"" + "status" + "\""
for attr, values in pidConnectionsCountList:
	for conn in validConnections:
		if (conn.pid==attr) :
			print "\"" + str(conn.pid) + "\",\"" + str(conn.laddr) + "\",\"" + str(conn.raddr) + "\",\"" + str(conn.status) + "\""
