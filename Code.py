g=dict()
input_file=open('Input.txt','r')
for line in input_file:
    if line !='\n':
        a=line.split(":")
        a[1]=a[1][1:]
        if a[1] != "":
            if a[1][-1] == "\n":
                a[1] = a[1][:-1]
            g[a[0]] = int(a[1])
input_file.close()

m=g["Number of employees"]
del g["Number of employees"]
s_v=sorted(g.values())
l=len(s_v)
min = s_v[-1] - s_v[0]
f=0
for i in range((l-m)+1):
    k=s_v[i + (m-1)] - s_v[i]
    if k<min:
        min=k
        f=1
output_file=open('output.txt','w')
output_file.write("The goodies selected for distribution are:\n")
output_file.write("\n")
for i in range(f, f+m):
    for j in g.keys():
        if g[j] == s_v[i]:
            output_file.write(j + ": ")
            output_file.write(str(g[j]))
            output_file.write("\n")
            break
output_file.write("\n")
output_file.write("And the difference between the chosen goodie with highest price and the lowest price is ")
output_file.write(str(min))
output_file.close()


