import json
import pickle

file=open("Hospital Data.txt", "rb+")
file2=open("Individual Data.txt", "rb+")

d={}
try:
    while True:
        d=pickle.load(file2)
except EOFError:
    pass
for i in d:
    print(i, "=", d[i])