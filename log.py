import requests
keyFile = open('/home/pi/Config/ifttt', 'r')
key = keyFile.readline().rstrip()
keyFile.close()
requests.post('https://maker.ifttt.com/trigger/foxberry/with/key/' + key, data = {'value1':'All systems operational.'})
