'''
This will read the averaged intensities from the final output file and plots them.
'''

import matplotlib.pyplot as plt

wavelength_range = (695, 800)

# Define the input file
# input_file = r"G:\.shortcut-targets-by-id\0B8-gGFa6hkR4XzJJMDlqZXVKRk0\ansom\Data\THz 1\Qdots spectra\Position Test\Pos6_14\processed\Pos10\aa_final.txt"
input_file = r"G:\.shortcut-targets-by-id\0B8-gGFa6hkR4XzJJMDlqZXVKRk0\ansom\Data\THz 1\Qdots spectra\Position Test\around 10\run5\..\processed\run5\aa_final.txt"

def plot_averaged_intensities(input_file):
    wavelengths = []
    intensities = []

    # Read the averaged intensities file
    with open(input_file, 'r') as f:
        for line in f:
            wavelength, intensity = line.strip().split(',')
            if float(wavelength) >= wavelength_range[0] and float(wavelength) <= wavelength_range[1]:
                wavelengths.append(float(wavelength))
                intensities.append(float(intensity))

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(wavelengths, intensities, label='Averaged Intensity')
    plt.xlabel('Wavelength')
    plt.ylabel('Averaged Intensity')
    plt.title('Averaged Intensity vs. Wavelength')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the plotting function
plot_averaged_intensities(input_file)
