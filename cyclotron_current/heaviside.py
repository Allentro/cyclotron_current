def read_log(filename):
    xdata = []
    ydata = []
    with open(filename, 'r+') as file: 
        for line in file: 
            line = line.split(' ')
            xdata.append(datetime.datetime.strptime(f'{line[0]} {line[1]}', '%Y-%m-%d %H:%M:%S'))
            ydata.append(float(line[2]))
    return xdata, ydata

def output_steps(x_data, y_data, granularity, step_min): 
    ''' 
    Parameters:
    x_data: array_like = Array of time
    y_data: array_like = Array of floats
    Granularity: float = Minumum number of time steps a step must be wide 
    step_min: float = Minimum value change for a new step to be created
    '''
    data = []
    moving_average = np.convolve(y_data, np.ones(granularity), 'valid') / granularity
    average_change = np.diff(moving_average)

    for idx in average_change: 
        if idx > step_min: 
            continue
                # It is this middle step I am currently struggling with.
    step_array = []
    return step_array

filename = f'{directory}/current_output.txt'
xdata, ydata = read_log(filename)

granularity =30
step_min = 25
step_array = output_steps(xdata, ydata, granularity, step_min)