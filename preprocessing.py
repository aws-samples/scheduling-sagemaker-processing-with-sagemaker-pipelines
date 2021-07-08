
import glob
import numpy as np
import os
from sklearn.preprocessing import StandardScaler

if __name__=='__main__':
    
    input_files = glob.glob('{}/*.npy'.format('/opt/ml/processing/input'))
    print('\nINPUT FILE LIST: \n{}\n'.format(input_files))
    scaler = StandardScaler()
    x_train = np.load(os.path.join('/opt/ml/processing/input', 'x_train.npy'))
    scaler.fit(x_train)
    for file in input_files:
        raw = np.load(file)
        # only transform feature columns
        if 'y_' not in file:
            transformed = scaler.transform(raw)
        if 'train' in file:
            if 'y_' in file:
                output_path = os.path.join('/opt/ml/processing/train', 'y_train.npy')
                np.save(output_path, raw)
                print('SAVED LABEL TRAINING DATA FILE\n')
            else:
                output_path = os.path.join('/opt/ml/processing/train', 'x_train.npy')
                np.save(output_path, transformed)
                print('SAVED TRANSFORMED TRAINING DATA FILE\n')
        else:
            if 'y_' in file:
                output_path = os.path.join('/opt/ml/processing/test', 'y_test.npy')
                np.save(output_path, raw)
                print('SAVED LABEL TEST DATA FILE\n')
            else:
                output_path = os.path.join('/opt/ml/processing/test', 'x_test.npy')
                np.save(output_path, transformed)
                print('SAVED TRANSFORMED TEST DATA FILE\n')
