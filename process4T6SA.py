# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

"""directories should be modified according to your directory """
File=['C:\\Users\\Chen\\Desktop\\subtask_A.txt',]

Result_File=['C:\\Users\\Chen\\Desktop\\T6SA_stance.neg',
			'C:\\Users\\Chen\\Desktop\\T6SA_stance.pos',
			'C:\\Users\\Chen\\Desktop\\T6SA_stance.none',
			]

RES=[]
			
def process_str(topic,msg):
	msg=msg.replace("#SemST","")
	msg=msg.replace("\r\n","\n")
	msg=msg.lower()
	msg=msg+"\n"

	return msg
	
if __name__=="__main__":
    for i in range(1):

        j=0

        with open(File[i],encoding="utf8") as f:
            for line in f:
                if j==0 :
                    j+=1
                    continue
                print(j)
                j+=1
                tmp=line.split("\t")
                id=int(tmp[0])
                topic=''.join(tmp[1])
                msg=''.join(tmp[2])
                stance=''.join(tmp[3])
                if stance=="AGAINST\n":
                    stance=0
                if stance=="FAVOR\n":
                    stance=1
                if stance=="NONE\n":
                    stance=2
                msg=process_str(topic,msg)
                datum = {"topic":topic,
						"stance":stance,
						"message":msg
						}
                if msg!="not available\n":
                    RES.append(datum)

    len_RES=len(RES)
    f_neg=open((Result_File[0]),"w",encoding="utf-8")
    f_pos=open((Result_File[1]),"w",encoding="utf-8")
    f_none=open((Result_File[2]),"w",encoding="utf-8")
    for i in range (len_RES):
        if RES[i]["stance"]==0:
            f_neg.write(RES[i]["message"])
        if RES[i]["stance"]==1:
            f_pos.write(RES[i]["message"])
        if RES[i]["stance"]==2:
            f_none.write(RES[i]["message"])

    f.close()
    f_neg.close()
    f_pos.close()
    f_none.close()




	
