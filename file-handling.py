# file handling program

def write_fn(filename,content):

    file=open(filename,'w')
    file.write(content)
    file.close()
    print(f"Data has been written to {filename}")

def read_fn(filename):
    file=open(filename,'r')
    content=file.read()
    file.close()
    return content

filename='example.txt'
#filename='E:\example.txt'

content="Hello,this is an example file handling program in Python!"
write_fn(filename,content)

read_content=read_fn(filename)
print("Content read from file:")
print(read_content)
