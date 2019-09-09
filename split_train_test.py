import numpy as np
import pandas as pd



def split_train_test(data, target=None, test_ratio=0.2, random_state=42):
    np.random.seed(random_state)
    
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)

    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]


    if type(data) == pd.core.frame.DataFrame:
        train_data = data.iloc[train_indices]
        test_data = data.iloc[test_indices]

        if target:
            train_target = target.iloc[train_indices]
            test_target = target.iloc[test_indices]

            return train_data, test_data, train_target, test_target
    
        else:
            return train_data, test_data
    
    else:
        train_data = []
        test_data = []

        for index in train_indices:
            train_data.append(data[index])
        
        for index in test_indices:
            test_data.append(data[index])
        
        if target:
            train_target = []
            test_target = []

            for index in train_indices:
                train_target.append(target[index])
        
            for index in test_indices:
                test_target.append(target[index])

            return train_data, test_data, train_target, test_target
        
        else:
            return train_data, test_data




