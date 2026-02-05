# Waveform-based Deep Learning Analysis of Carotid Dynamics for Cardiovascular Risk Classification using Physiology-Preserving Data Augmentation (WCD-CRC):
This study proposes a neural network–based framework for cardiovascular disease (CVD) risk classification using nonconventional arterial waveforms derived from carotid ultrasound imaging with physiology-preserving data augmentation. Dynamic arterial signals, including vessel diameter, flow velocity, and pressure, were obtained from carotid duplex ultrasonography and brachial pressure measurements and analyzed using a hybrid convolutional neural network–long short-term memory (CNN–LSTM) model. To address limited sample size and class imbalance, three data augmentation strategies—time shifting, jittering, and TimeGAN—were evaluated, with augmentation scales selected based on empirical performance analysis. The dataset was expanded from 75 to 6,060 samples, and time-shift augmentation achieved the best performance, yielding a test accuracy of 0.813, an AUC of 0.848, and a low loss value (0.234) while preserving physiological waveform integrity. These results demonstrate the feasibility of CVD risk classification from carotid dynamic waveforms that are not routinely used in clinical practice and support duplex sonography–based waveform analysis as a promising data-driven approach for CVD risk assessment.

# Dataset:
All the data used by WCD-CRC can be found in the "Training and testing code" folder.

# Dependency:
numpy==1.23.5

pandas==2.3.1

scikit-learn==1.7.1

tensorflow==2.12.0

keras==2.12.0

matplotlib==3.10.5

seaborn==0.13.2

openpyxl==3.1.5

xlsxwriter==3.2.5

# Usage:
jupyter notebook

