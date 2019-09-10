import subprocess

process = subprocess.Popen('python try.py', shell = True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
pin = process.stdin
pout = process.stdout
flag = 0
pin.write('flag = ' + str(flag))

##SALOME_ROOT='/INSTALLABLES/salome_meca-2017/appli_V2017.0.2' #root folder for salome
##ASTER_ROOT='/INSTALLABLES/aster' #root folder for asterstudy
##WORKING_DIR='/home/u1449908/Salome_files/AUTO_FIBER' #Working directory

### Make a subprocess call to the salome executable and store the used port in a text file:
##subprocess.call(SALOME_ROOT + '/salome -t try.py --ns-port-log=' + WORKING_DIR + '/salomePort.txt', shell=True)

### Read in the port number from the text file:
##port_file = open(WORKING_DIR + '/salomePort.txt','r')
##killPort = int(port_file.readline())
##port_file.close()

### Kill the session with the specified port:
##subprocess.call(SALOME_ROOT + '/bin/salome/killSalomeWithPort.py %s' % killPort,shell=True)
