
import numpy as np
from scipy.io import loadmat


PATH = 'C://Users//DongHwi//Desktop//intern//'
file = 'dataset_1.mat'


mat_file = loadmat(PATH + file)


dataset_dict = { 0 : 'S_left',
                 1 : 'S_left_phase',
                 2 : 'S_right',
                 3 : 'S_right_phase',
                 4 : 'clean_left',
                 5 : 'clean_left_phase',
                 6 : 'clean_right',
                 7 : 'clean_right_phase',
                 8 : 'idx_drone_end',
                 9 : 'idx_voice_end',
                 10: 'idx_voice_start' }




'''x_data'''
for n in range(len(dataset_dict)):
    mat_data_name = dataset_dict[n]
    npy_from_mat  = mat_file[ mat_data_name ]

    np.save( PATH + mat_data_name + '.npy', npy_from_mat )
    print('saved as '+mat_data_name+'.npy')


'''y_data'''
y_data = loadmat( PATH+'angle.mat' )
np.save( PATH+'angle.npy', y_data['phi'][:1000] )
print('done.')
