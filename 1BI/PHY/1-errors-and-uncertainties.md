`2017-09-07 Thursday`
# Errors and uncertainties

- Absolute error
	- raw uncertainty of measurement or estimate
- Fractional error
	- $\frac{\text{Absolute error}}{\text{Value of estimate / measurement}}$

The symbol $\Delta$ is used to describe error.

## Example
Guess the number of Dragibus.

- Absolute value of sweets: $150$
- Absolute error: $\pm 70$
- Fractional error: $\frac{70}{150} \sim 50 \text{%}$ (more precisely 47%)

### Adding measurements
$(15 \pm 70) + (85 \pm 25) = 235 \pm \bf{95}$

#### RULE: when adding physical quantities, I add _absolute_ uncertainties.

#### Prove that adding fractional uncertainties does _not_ give the same result

- 1st pot $\frac{\Delta_{pot1}}{pot1} = \frac{70}{150}$
- 2nd pot $\frac{\Delta_{pot2}}{pot2} = \frac{25}{85}$
- 3rd pot $\frac{\Delta_{pot3}}{pot3} = \frac{70 + 25}{150 + 85} = \frac{95}{235}$

$\frac{\Delta_{pot1}}{pot1} + \frac{\Delta_{pot2}}{pot2} = 0.76 \neq \frac{95}{235}$


### Subtracting measurements
- $I_1 = 0.5A \pm 0.2A$
- $I_2 = 0.3A \pm 0.2A$
- $I_1 = I_2 = I_3 \Leftrightarrow I_3 = I_1 - I_2$
- Find $I_3$

$I_3 = I_1 - I_2 = 0.5 - 0.3 = 0.2A$  

- NO: $\Delta_{I_3} = \Delta_{I_1} - \Delta_{I_2} = 0.2 - 0.2 = \mathbf{0}A$
- YES: $\Delta_{I_3} = \Delta_{I_1} + \Delta_{I_2} = 0.2 + 0.2 = 0.4A$

#### RULE: when subtracting measurements or estimates -> add _absolute_ uncertainties

### Example - continued
- Mass of beaker
- Mass of 1 sweet
- $\text{#}sweets = \frac{\text{Total Mass}}{\text{Mass of sweets}}$

Mass of sweet 1: 4.4g  
$\Delta_{sweet 1}$: ± 0.2g  
Mass of empty beaker: 225g ± 5g  
Mass of full beaker: 870 ± 5g  
Mass of sweets: 645 g  
$\Delta_{sweets}$ = 10g  
-> 645g ± 10g

$\frac{\text{#}\Delta_{sweets}}{\text{#}sweets} = \frac{\Delta_{\text{mass sweets}}}{\text{mass sweets}} + \frac{\Delta_{\text{mass of 1 sweet}}}{\text{mass of 1 sweet}}$

- $\text{#}sweets = \frac{\text{Total mass}}{Individual mass} = \frac{625}{44} = 147$
- $\Delta_{\text{#}sweets} = (\frac{\Delta_\text{mass 1}}{\text{mass 1}} + \frac{\Delta_\text{mass total}}{\text{mass total}}) \cdot \text{#}sweets = (\frac{0.2}{4.4} + \frac{10}{645}) \cdot 147 = 9$
- Answer = 147 ± 9

`2017-09-08 Friday`
### Estimating number of sweets using volumes
- $V_{sphere} = \frac{4}{3} \pi r^3$
	- r = 0.8 ± 0.1cm
- $V_{cylinder} = A \cdot h = \pi r^2 h$
	- h = 10.8 ± 0.2cm
	- r = 5.2 ± 0.4cm

1. Calculate volume of sweet and fractional error
	- $V = \frac{4}{3} \pi \cdot 0.8^3 = 2.1$ 
	- $\frac{\Delta V}{V} = \frac{0.1}{0.8} + \frac{0.1}{0.8} + \frac{0.1}{0.8} = \frac{3}{8}$
	- $\Delta V = \frac{\Delta V}{V} \cdot V = 0.8$
	- $V = 2.1 \pm 0.8 cm^3$
2. Calculate volume of cylinder
	- $V = \pi r^2 h = 917.4$
	- $\frac{\Delta V}{V}=\frac{0.4}{5.2} + \frac{0.4}{5.2} + \frac{0.2}{10.8} = 0.2$
	- $\Delta V = \frac{\Delta V}{V} \cdot V = 158.1$
	- $V = 917.4 \pm 158.1 cm^3$
3. Divide volume of cylinder by volume of sweet
	- $\text{#sweets} = \frac{V_{cylinder}}{V_{sweet}} = 428$
	- $\frac{\Delta\text{#sweets}}{\text{#sweets}} = \frac{0.8}{2.1} + \frac{158.1}{917.4} = 0.5$
	- $\Delta\text{#sweets} = \frac{\Delta\text{#sweets}}{\text{#sweets}} \cdot \text{#sweets} = 234$
	- $\text{#sweets} = 428 \pm 234$
4. Suppose 25% of the beaker is filled with air. Calculate the new number of candies.
	- 107 ± 59

### Actual number (obtained by counting)
171

## Random and systematic errors
- **Random error** is error due to the recorder, rather than the instrument used for the measurement
- **Systematic error** is error due to the instrument being "out of adjustment".

## Precision and accuracy
- precision (grouped)
- accuracy (average)

## Standard deviation
$\sqrt{\sum_{i=1}^{n}\frac{(x_i - \bar{x})^2}{n-1}}$

## Orders of magnitude
If you take 10 and 100, there are separated by one order of magnitude.

Use $\log_{10}(X)$ to find the magnitude of X.

e.g. $$\log_{10}(84000) = \log_{10}(8.4) + \log_{10}(10000) = 4.92 \simeq 5$$

Comparing numbers: A = 1 000 000, B = 1 000
$\frac{A}{B} = 1 000 \text{ and } \log_{10}(1000) = 3$

## Significant figures

| number | sf    |
|:------:|:-----:|
| 405    |3 s.f. |
| 100    |1 s.f. |
| 100.24 |5 s.f. |
| 1.24   |3 s.f. |
| 1.240  |4 s.f. |

- 0 after decimal is _always_ significant

## SI prefixes
|Power of 10|Prefix Name|Symbol|
|:---------:|:---------:|:----:|
|$10^{-12}$   |pico       |p|
|$10^{-9}$|nano|n|
|$10^{-6}$|micro|$\mu$|
|$10^{-3}$|milli|m|
|$10^{-2}$|centi|c|
|$10^3$|kilo|k|
|$10^6$|mega|M|
|$10^9$|giga|G|
|$10^{12}$|tera|T|
