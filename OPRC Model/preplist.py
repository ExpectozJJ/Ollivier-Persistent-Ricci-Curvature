import numpy as np
import math

def listprep(name1, name2):
    f = open(name1, 'r')
    g = open(name2, 'r')
    contents = f.readlines()
    contents1 = g.readlines()

    refined_set = []
    for i in range(6,len(contents)):
        refined_set = np.append(refined_set, contents[i][:4])
    
    core_set = []
    for i in range(6,len(contents1)):
        core_set = np.append(core_set, contents1[i][:4])

    training_set = list(set(refined_set).symmetric_difference(core_set))
    test_set = core_set

    train_BindingAffinity = []
    test_BindingAffinity = []
    for i in range(len(training_set)):
        for j in range(6, len(contents)):
            if contents[j][:4]==training_set[i]:
                #print(training_set[i], contents[j][19:23])
                train_BindingAffinity = np.append(train_BindingAffinity, float(contents[j][18:23]))
                
    for i in range(len(test_set)):
        for j in range(6, len(contents)):
            if contents[j][:4]==test_set[i]:
                #print(training_set[i], contents[j][19:23])
                test_BindingAffinity = np.append(test_BindingAffinity, float(contents[j][18:23]))

    np.save("train_BindingAffinity.npy", train_BindingAffinity)
    np.save("test_BindingAffinity.npy", test_BindingAffinity)
    print("Y_train and Y_test Data have been created.")
    return [training_set, test_set, refined_set]

[training_set, test_set, refined_set] = listprep("INDEX.2007.refined.data", "PDBbind_core_set_v2007.2.lst")

np.savez("train_list.npz", training_set)
np.savez("test_list.npz", test_set)

train_list_2007 = np.load("train_list.npz", allow_pickle=True)
test_list_2007 = np.load("test_list.npz", allow_pickle=True)