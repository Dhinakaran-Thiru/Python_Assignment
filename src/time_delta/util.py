from datetime import datetime
def time_delta(s):
    string=s.split("\n")
    print(len(string))
    n=int(string[0])
    new_list=[]
    for i in range(1,len(string),2):
        t1=string[i]
        t2=string[i+1]
        format_str="%a %d %b %Y %H:%M:%S %z"
        t1=datetime.strptime(t1,format_str)
        t2=datetime.strptime(t2,format_str)
        diff=int(abs(t1-t2).total_seconds())
        new_list.append(str(diff))
    return '\n'.join(new_list)