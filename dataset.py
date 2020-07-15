
import numpy as np

#PATH = 'C://Users//DongHwi//Desktop//intern//'
PATH = 'C://Projects//keras_talk//keras//intern//dataset//'

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



numpy_dict = dict()
for n in range(4):
    numpy_name    = dataset_dict[n]
    numpy_dict[n] = np.load( PATH + numpy_name + '.npy' )
    



''' x_data, y_data '''
x_data = []
for idx in range(1000):
    x_element = []

    for n in range(4):
        x_element.append( numpy_dict[n][:,:,idx] )

    x_element = np.asarray( x_element )
    x_data.append(x_element)


x_data = np.asarray(x_data)
y_data = np.load(PATH + 'angle.npy')
print('done..')
