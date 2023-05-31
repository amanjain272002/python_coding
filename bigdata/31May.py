import pandas as pd
# sr = pd.Series([12,13,14],name = "marks")
# print(sr)
# print(type(sr))
# print(sr.name)
# print(max(sr))
# print(sr.index)
# sr.index = ['a','b','c']
# print(sr)
# print(sr.index)


# nm = pd.DataFrame({"Name":["A","B"],"product":[1,2]})
#  if element is not given to a particular column than none should be written at that place
# print(nm)
# print(nm.columns)
# nm.index =  [10,20]
# print(nm)
# nm.columns = ["age","name"]
# print(nm)
# print(nm["age"])
# print(nm["age"][10])


nm = pd.Series(["Raj","Jai","baniya"])
pn= pd.Series([1234,2345,5678])
ed = pd.Series(["as@gmail.com","psd@gmail.com","abc@gmail.com"])

sd = pd.DataFrame({"Name":nm,"Phone_No":pn,"email-id":ed})
# print(sd)
sd.columns = ["Student_name","Student_Phone_No","Student_email"]
sd.index = ["S1","S2","S3"]
print(sd)