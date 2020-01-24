#!/usr/bin/python

import docker

try:
   server = docker.from_env()
   server_health = server.ping()
   list_containers = server.containers.list()
   info = server.info()
   status_containers = server.api.containers()
   print 'Images:',info['Images'],'|','Containers:',info['Containers'],'|','ContainersRunning:',info['ContainersRunning'],'|','ContainersPaused:',info['ContainersPaused'],'|','ContainersStopped:',info['ContainersStopped']
   print info['Warnings'][0]
   print status_containers[0]['Status']
#   container_id = server.containers.get(server.containers.list)
#   container_name = server.attrs['Name']
#   container_status = server.container.attrs['State']['Status']
#   container_ports = container.attrs['NetworkSettings']['Ports']
#   print(container_id + container_name + container_status + container_ports)
except Exception, p:
   print('%s' %repr(p))    

