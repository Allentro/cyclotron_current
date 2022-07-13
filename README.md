## Cyclotron Current logger 
This is a python module developed at the University of Birmingham cyclotron. 
Data are parsed from an arduino data logger and converted into a .csv of amps against time. 
```
logger_to_csv()
```
A second function offers the ability to convert a logged data-set into a discrete number of Heaviside step-functions. 
```
create_step_fn()
```
The plot below shows the logged data in blue with the Heaviside functions overlaid in red. 
