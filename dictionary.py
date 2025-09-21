#program of dictionary

market={'maths':45,'science':50,'gk':90}
print(market)

print("\n adding data in dictionary")
market['shopname']='big bazaar'
print(market)

print("\n deletion in dictionary")
del market['maths']
print(market)

print("\n Membership test")

print("gk in market=",'gk' in market)
print("history in market=",'history' not in market)
print("english in market=",'english' in market)

#dictionary=a collection of{key:value}pairs

capitals={"USA":"washington D.C",
          "India":"New Delhi",
          "China":"Beijing",
          "Russia":"Moscow"}

keys=capitals.keys()
print(keys)
for key in capitals.keys():
    print(key)


#program of list within dictionary

student={
    "Name":"Alice",
    "Subjects":["Math","Science","English","History"]
}

print(f"Student's Name:{student['Name']}")
print("Subjects enrolled:")
count=0
for subject in student["Subjects"]:
    count+=1
    print(f"{count}:{subject}")