fp = open('sample.txt','w')
fp.write('Hello . this is a file created using python\n')
fp.write('Bye . see you next time')
fp.close()

fr = open('sample.txt','r')
text = fr.read()
fr.close()
print(text)