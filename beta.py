import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

# Parameters of the Beta distribution
alpha1 = int(input())
beta_param1 = int(input())

# Generate a range of x values between 0 and 1 (since Beta is defined in this range)
x = np.linspace(0, 1, 100)

# Calculate the PDF and CDF for the Beta distribution
pdf_values = beta.pdf(x, alpha1, beta_param1)
cdf_values = beta.cdf(x, alpha1, beta_param1)

# Print the PDF and CDF values at a specific point (e.g., at x=0.5)

# Plotting the PDF and CDF
plt.figure(figsize=(10, 5))



alpha2 = int(input())
beta_param2 = int(input())

# Generate a range of x values between 0 and 1 (since Beta is defined in this range)
x = np.linspace(0, 1, 100)

# Calculate the PDF and CDF for the Beta distribution
pdf_values2 = beta.pdf(x, alpha2, beta_param2)
cdf_values2 = beta.cdf(x, alpha2, beta_param2)

# Plot PDF
plt.subplot(1, 2, 1)
plt.plot(x, pdf_values, label=f'Beta PDF (α={alpha1}, β={beta_param1})')
plt.plot(x, pdf_values2, label=f'Beta PDF (α={alpha2}, β={beta_param2})')
plt.title('Beta Distribution PDF')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf_values, label=f'Beta CDF (α={alpha1}, β={beta_param1})', color='orange')
plt.plot(x, cdf_values2, label=f'Beta CDF (α={alpha2}, β={beta_param2})', color='red')
plt.title('Beta Distribution CDF')
plt.xlabel('x')
plt.ylabel('Cumulative Probability')
plt.legend()


plt.tight_layout()
plt.show()
