s = 'X-DSPAM_Confidence: 0.875 '

pos1= s.find(':')

print("the position of the colon character is: ",pos1)

pos2 = s[20:]

print('the original data type is: ', type(pos2))

pos3 = float(pos2)

print('Now the data type is: ', type(pos3))