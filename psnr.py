
import matplotlib.pyplot as plt
import numpy as np
from skimage.metrics import peak_signal_noise_ratio
from tabulate import tabulate

# black and white ramp [0,256]
uint8_ramp = np.linspace(0, 255, num=256*256).reshape(256, 256).astype(np.uint8)


noisy_ramp8 = uint8_ramp.copy()
noisy_ramp8[0, 0] = 1
fig0 = plt.figure()
plt.imshow(uint8_ramp, cmap='gray', vmin=0, vmax=255)
fig0.suptitle('uint8 image', fontsize=20)
plt.show()

compute_psnr = peak_signal_noise_ratio(uint8_ramp, noisy_ramp8)
print(f'8 bit image: min:{np.amin(uint8_ramp)}, max:{np.amax(uint8_ramp)}, mean:{np.mean(uint8_ramp)}')
print(f'8 bit image PSNR : {compute_psnr:.2f} dB')

# normalized black & white image [0,1] float32
float32_ramp = (uint8_ramp / 255.).astype(np.float32)
noisy_float32 = float32_ramp.copy()
noisy_float32[0, 0] = 1 / 255.


fig1 = plt.figure()
plt.imshow(float32_ramp, cmap='gray', vmin=0, vmax=1)
fig1.suptitle('float32 image', fontsize=20)
plt.show()

compute_psnr = peak_signal_noise_ratio(float32_ramp, noisy_float32)
print(f'im min value:{np.amin(float32_ramp)}, im max value:{np.amax(float32_ramp)}, im mean value:{np.mean(float32_ramp)}')
print(f'float32 image PSNR : {compute_psnr:.2f} dB')

# black and white ramp [0,256]
uint16_ramp = np.linspace(0, 65535, num=256*256).reshape(256, 256).astype(np.uint16)
noisy_ramp16 = uint16_ramp.copy()
noisy_ramp16[0, 0] = 1
fig2 = plt.figure()
plt.imshow(uint16_ramp, cmap='gray', vmin=0, vmax=65535)
fig2.suptitle('uint16 image', fontsize=20)
plt.show()

compute_psnr = peak_signal_noise_ratio(uint16_ramp, noisy_ramp16)


print(f'im min value:{np.amin(uint16_ramp)}, im max value:{np.amax(uint16_ramp)}, im mean value:{np.mean(uint16_ramp)}')
print(f'16 bit images PSNR : {compute_psnr:.2f} dB')
