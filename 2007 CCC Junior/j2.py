# I Speak TXTMSG

txtmsg = {'CU'   :  'see you',
          ':-)'  :  'I\'m happy',
          ':-('  :  'I\'m unhappy',
          ';-)'  :  'wink',
          ':-P'  :  'stick out my tongue',
          '(~.~)':  'sleepy',
          'TA'   :  'totally awesome',
          'CCC'  :  'Canadian Computing Competition',
          'CUZ'  :  'because',
          'TY'   :  'thank-you',
          'YW'   :  'you\'re welcome',
          'TTYL' :  'talk to you later'}

while True:
    line = input()
    if txtmsg.get(line) != None:
        print(txtmsg[line])
    else:
        print(line)
    if line == 'TTYL':
        break