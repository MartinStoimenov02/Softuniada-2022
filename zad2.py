n = int(input());
text=input();

for i in range (0, n):
    print((n*(" "))+("~ ~ ~"));
print(((3 * n + 6)-1)*"=");
for i in range(1, n-1):
    if(i==int(n/2)):
        print("|"+(n*"~")+text.upper()+(n*"~")+"|"+((n-1)*" ")+"|");
    else:
        print("|"+(((3*n+6)-(n-1)-3)*"~")+"|"+((n-1)*" ")+"|");
print(((3 * n + 6)-1)*"=");
max = 6+(n-1)*2;
for i in range (0, n):
    print((i*" ")+"\\"+(max*"@")+"/");
    max-=2;
print(((3 * n + 6)-1)*"-");
