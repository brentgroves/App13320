# docker run --rm -v /home/brent/srcnode/App13320:/app rp python /app/get_counter.py
# https://github.com/dmroeder/pylogix
# https://realpython.com/python-versions-docker/
'''
the following import is only necessary because eip.py is not in this directory
'''
import sys
sys.path.append('..')

'''
Get the tag list from the PLC

This will fetch all the controller and program
scoped tags from the PLC.  In the case of
Structs (UDT's), it will not give you the makeup
of each  tag, just main tag names.
'''
from pylogix import PLC
with PLC() as comm:
    comm.IPAddress = '10.1.2.161'
    tags = comm.GetTagList()
    
    for t in tags.Value:
        if t.TagName == 'SRP_Seq_Counter':
          print(f'TagName: {t.TagName},DataType: {t.DataType},DataTypeValue: {t.DataTypeValue}')
          break

#        print(t.TagName, t.DataType,t.DataTypeValue)

