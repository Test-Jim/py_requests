

def appendMs(response,ms,passls,fels):
    try:
        if response.json()['code'] == '100':
            passls.append(ms)
        else:
            fels.append(ms)
    except:
        fels.append(ms)
