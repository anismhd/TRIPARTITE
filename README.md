# TRIPARTITE

A Python Script for Ploting Velocity Spectra in Tripartite

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Matplotlib
* Numpy

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

## Theory of Tripartite

The time history of degree of freedom can be represented in Fourier domain as,

$$	u = \sum_{i=0}^{N} U_i \exp (i \omega t) $$

The maximum value of displacement/rotation $u$ can and velocity of $\dot{u}$ are related through equation,

$$ \dot{u}_{max} = u_{max} \omega $$ 

Similarly, maximum value of accelaration $\ddot{u}_{max}$ and velocity are,

$$ \ddot{u}_{max} = u_{max} \omega^2 $$

In case of ground motions due to earthquake,

* $u_{max}$ - Peak Ground Displacement, PGD
* $\dot{u}_{max}$ - Peak Ground Velocity, PGV
* $\ddot{u}_{max}$ - Peak Ground Accelaration, PGA

The spectral plot of velocity with frequency/period in logarithemic scale is Tripartite. The spectral displacement and accelration from velocity plot can be established using following equations.

$$ \log_{10}(u_{max}) = \log_{10}(\dot{u}_{max}) - \log_{10}(\omega) $$
$$ \log_{10}(\ddot{u}_{max}) = \log_{10}(\dot{u}_{max}) + \log_{10}(\omega) $$

The above equations indicates acceration axis will be inclinide -45 degree to y-axis and diplacement axis will be 45 degree to y-axis.

## Authors

* **Anis Mohammed Vengasseri** - *Initial work* - (https://github.com/anismhd)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

