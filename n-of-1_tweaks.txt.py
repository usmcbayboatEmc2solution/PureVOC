import sympy as sp  
import numpy as np  

phi = (1 + sp.sqrt(5))/2  
golden_pi = phi * sp.pi  # ≈5.083  

ber = 0.4  
boost = 0.3  
new_ber = ber * (1 - boost * (golden_pi / 12).evalf())  

print(f"Golden Pi: {golden_pi.evalf()}")  
print(f"New BER: {new_ber.evalf()}")  
print(f"Reduction: {1 - new_ber / ber:.1%}")  