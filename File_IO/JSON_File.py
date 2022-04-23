#Storing JSON values in text file

import json

MyList =['Hello','Rahul',233,1234.78787]
MyDictionary = {'food':'eggs','job':'Engineer'}

print(json.dumps(MyList))

FileObj = open('Myfile_JSON.txt','w') #open file in read mode

json.dump(MyList,FileObj)# dump JSON data to file
json.dump(MyDictionary,FileObj)

json.dump(MyList,FileObj)
json.dump(MyDictionary,FileObj)

FileObj.close() #Close the file 