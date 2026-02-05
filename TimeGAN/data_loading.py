

## Necessary Packages
import numpy as np
import pandas as pd
import os

def sine_data_generation (no, seq_len, dim):

  # Initialize the output
  data = list()

  # Generate sine data
  for i in range(no):      
    # Initialize each time-series
    temp = list()
    # For each feature
    for k in range(dim):
      # Randomly drawn frequency and phase
      freq = np.random.uniform(0, 0.1)            
      phase = np.random.uniform(0, 0.1)
          
      # Generate sine signal based on the drawn frequency and phase
      temp_data = [np.sin(freq * j + phase) for j in range(seq_len)] 
      temp.append(temp_data)
        
    # Align row/column
    temp = np.transpose(np.asarray(temp))        
    # Normalize to [0,1]
    temp = (temp + 1)*0.5
    # Stack the generated data
    data.append(temp)
                
  return data

### Custom-modified code to process all patient Excel files in a folder
import os

def patient_data_loading(folder_path, seq_len):

  temp_data = []

  for file in os.listdir(folder_path):
    if file.endswith(".xlsx") or file.endswith(".xls"):
      df = pd.read_excel(os.path.join(folder_path, file))

      # Ensure that only the 4 required columns are selected in the correct order
      df = df[['Time', 'Brachial Data', 'Carotid Diameter', 'blood velocity']]
      
      df = df.values  
      # If MinMaxScaler is used, remove this line and restore the step below

      # Split the data into consecutive sequences of length seq_len
      for i in range(0, len(df) - seq_len):
        _x = df[i:i+seq_len]
        temp_data.append(_x)

  # Shuffle the data to approximate i.i.d. samples
  idx = np.random.permutation(len(temp_data))
  data = [temp_data[i] for i in idx]

  return data
