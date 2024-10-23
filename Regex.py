import re

ProtocoloEncoder = re.compile('.*#P:[0-9]{1,3},[0-9];S:(ON|OFF);L:(ON|OFF).*')
print(ProtocoloEncoder.match(r'#P:257,8;S:ON;L:OFF'))


ProtocoloEncoder2 = re.compile('#P:[0-9]{1,3},[0-9];S:(ON|OFF);L:(ON|OFF)')
print(ProtocoloEncoder2.search(r'#P:257,8;S:ON;L:OFF'))
