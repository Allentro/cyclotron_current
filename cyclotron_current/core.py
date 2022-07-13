def import_current_logger(directory, file, current_scale_na): 
    ''' 
    Function to extract the data from the logger format. Itterating through the file, the data are converted. 
    The values in the file are taken every second on a scale 0-2. (negative numbers = 0). Where the scale is multiplied by the 'current_scale' parameter
    The first loop takes the first line from the file and extracts the start date and time. 
    Data are extracted into a nested data list. [x_data, y_data]. x_data = time, y_data = current.
    '''
    log_file = f'{directory}/{file}'
    current_scale = 3e-7 # Amps 
    current_scale = current_scale* 3e9 # converting A->nA 
    with open(log_file, 'r+') as file: # 'r' in the open statement allows you to read but not write to the file
        y_data = []
        x_data = []
        counter = 0
        for line in file:
            if counter == 0: 
                date_time_str = line.split('log')[1].split('=')[0].strip(' ')
                date_time = datetime.datetime.strptime(date_time_str, '%Y.%m.%d %H:%M:%S') 
                date = date_time.date()
                time = date_time.time()
            counter += 1 
            if ',' in line:
                number = float(line.split(',')[0])
                if number < 0: 
                    number = 0 
                else: 
                    error = 0.025 * (current_scale)
                    number *= current_scale/2 # The divide by two is due to the scale on the current logger being between 0-2. This normalised the data
                date_time = date_time + datetime.timedelta(0,1) # this command adds 1 second for each 
                y_data.append(number) 
                x_data.append(date_time)
    data = [x_data, y_data]
    return data#, error


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

