

def appendMs(response,ms,passls,fels):
    try:
        if response.json()['code'] == '100':
            passls.append(ms)
        else:
            fels.append(ms)
    except:
        fels.append(ms)

def appendMs_dubbo(response,ms,passls,fels):
    try:
        if response.json['success'] == 'True':
            passls.append(ms)
        else:
            fels.append(ms)
    except:
        fels.append(ms)