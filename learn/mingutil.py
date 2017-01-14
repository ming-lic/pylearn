

# import sys;
# 
# 
# if not "/pylearn/learn/" in sys.path:
#     sys.path.append("/pylearn/learn/") 
# if not 'mingutil' in sys.modules:
#     mingutil = __import__('mingutil')
# else:
#     eval('import mingutil')
#     b = eval('reload(mingutil)')
    

    
def compline(name): 
    if name is not None:
        print "****************************************** "+name+" complete **********************************************"
    else:
        print "***************************************************************************************************"