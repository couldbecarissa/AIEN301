import pandas as pd
import numpy as np
import random
np.random.seed(47)

classes = ['Class 1', 'Class 2', 'Class 3']
confusion_matrix = [[100,20,5],[15,80,10],[10,5,5]]


df_confusion = pd.DataFrame(
    confusion_matrix,
    index=['Actual ' + _ for _ in classes],
    columns=['Predicted ' + _ for _ in classes]
)

def conf_positions(df,i):
    for i in range(3):
        tp=df[i,i]
        fp=np.sum(df[:,i])-tp
        fn=np.sum(df[i,:])-tp
        tn=np.sum(df)-tp-fp-fn

    return tp,fp,fn,tn
    
def metric_scores(df,type='micro'):
    if type=='micro':
        precision=[]
    

# Display the generated confusion matrix
print(df_confusion)