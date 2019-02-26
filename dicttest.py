# import sys
# String=sys.argv[1:]
# dict={}

# for i in String:
# 	l=i.split(':')
# 	dict[l[0]]=l[1]
# for key,value in dict.items():
# 	print('ID:'+key ,'Name:'+value)
import sys
output_dict = {}

def handle_data(str):
    return str.split(":")

def print_data(key,value):
    print('ID:'+key,'Name:'+value)

if __name__ == '__main__':

    for arg in sys.argv[1:]:
        l=handle_data(arg)
        output_dict[l[0]]=l[1]
    for key in output_dict:
        print_data(key, output_dict[key])
        