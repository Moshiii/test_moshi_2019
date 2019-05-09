 
 
def version_compare(v1,v2):
#assuming the version is in the format  major.minor
#assuming version is all digital
#assuming the maximum decimal is 5. i.e. 00000.00000
#assuming all version number are positive

    v1 = int(''.join(['{0:05d}'.format(int(x)) for x in v1.split('.')]))
    v2 = int(''.join(['{0:05d}'.format(int(x)) for x in v2.split('.')]))
    # return 1 if v1>v2
    # return 0 if v1==v2
    # return -1 if v1<v2
    if v1==v2:  return 0
    elif v1>v2: return 1
    else :      return -1


print(version_compare('0.1','0.4'))
print(version_compare('0.41','0.4'))
print(version_compare('3.1','3.0'))
print(version_compare('3.14','3.41'))
print(version_compare('4.1','0.2344'))
print(version_compare('3.1','9.455'))
print(version_compare('452.1','3.1'))