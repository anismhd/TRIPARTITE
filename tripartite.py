import numpy as np
import matplotlib.pyplot as plt
def tripartite_axis(axis):
	axis.set_xscale('log')
	axis.set_yscale('log')
	xlim = axis.get_xlim()
	axis.set_xlim(xlim)
	ylim = axis.get_ylim()
	axis.set_ylim(ylim)
	axis.grid(b=True, which='both', color='k', linestyle='-', alpha=.3, lw=.3)
	axis.set_xlabel('Period (sec.)')
	axis.set_ylabel('Spectral Velocity')
	# Finding the middle point of the graph
	xcenter = 10**(0.5*sum(np.log10(xlim)))
	ycenter = 10**(0.5*sum(np.log10(ylim)))
	# Finding minimum and maximum value of displacement and accelaration
	log10DISP_min = np.floor(np.log10(ylim[0]*xlim[0]/(2*np.pi)))
	log10DISP_max = min(np.ceil(np.log10(ylim[1]*xlim[1]/(2*np.pi))),1)
	log10ACCL_min = np.floor(np.log10(ylim[0]*2*np.pi/xlim[1]))
	log10ACCL_max = min(np.ceil(np.log10(ylim[1]*2*np.pi/xlim[0])),2)
	C1 = 0.5*(sum(np.log10(ylim)) - sum(np.log10(xlim)))
	C2 = 0.5*(sum(np.log10(ylim)) + sum(np.log10(xlim)))
	bbox = {'fc': '0.8', 'pad': 0}
	for accl in range(int(log10ACCL_min),int(log10ACCL_max)+1):
		axis.plot(xlim,10**accl*np.array(xlim)/(2*np.pi), c='b', lw=.5, alpha=.3)
		loc_x = -0.5*(accl-np.log10(2*np.pi)-C2)
		loc_y = -loc_x + C2
		axis.text(10**loc_x,10**loc_y, '{0:f} $m/s^2$'.format(10**accl),\
					ha='center', va='center', rotation=45, color='b')
		for i in range(1,10):
			axis.plot(xlim,10**accl*i*np.array(xlim)/(2*np.pi), c='b', lw=.5, alpha=.3)
	for disp in range(int(log10DISP_min),int(log10DISP_max)+1):
		axis.plot(xlim,10**disp*2*np.pi/np.array(xlim), c='r', lw=.5, alpha=.3)
		loc_x = 0.5*(disp+np.log10(2*np.pi)-C1)
		loc_y = loc_x + C1
		axis.text(10**loc_x,10**loc_y, '{0:f} $m$'.format(10**disp),\
					horizontalalignment='center', rotation=-45,\
					verticalalignment='center', color='r')
		for i in range(1,10):
			axis.plot(xlim,10**(disp)*i*2*np.pi/np.array(xlim), c='r', lw=.5, alpha=.3)
	return axis
def tripartite_plot(periods,PGV, g=9.81):
	fig = plt.figure()
	ax = plt.gca()
	ax.plot(periods,PGV, c='k')
	ax = tripartite_axis(ax)
	'''
	ax.set_xscale('log')
	ax.set_yscale('log')
	xlim = ax.get_xlim()
	ax.set_xlim(xlim)
	ylim = ax.get_ylim()
	ax.set_ylim(ylim)
	ax.grid(b=True, which='both', color='k', linestyle='-', alpha=.3, lw=.3)
	ax.set_xlabel('Period (sec.)')
	ax.set_ylabel('Spectral Velocity')
	DISP_lim10 = [np.floor(np.log10(ylim[0]*xlim[0]/(2*np.pi))), \
				min(np.ceil(np.log10(ylim[1]*xlim[1]/(2*np.pi))),1)]
	ACCL_lim10 = [np.floor(np.log10(ylim[0]*2*np.pi/xlim[1])), \
				min(np.ceil(np.log10(ylim[1]*2*np.pi/xlim[0])),2)]
	print(DISP_lim10)
	print(ACCL_lim10)
	print(xlim)
	print(ylim)
	ax.scatter([10**(0.5*sum(np.log10(xlim)))],[10**(0.5*sum(np.log10(ylim)))])
	## Trials
	c = 0.5*(sum(np.log10(ylim)) - sum(np.log10(xlim)))
	c1 = 0.5*(sum(np.log10(ylim)) + sum(np.log10(xlim)))
	ax.plot(xlim, 10**(np.log10(xlim)+c), c='r')
	ax.plot(xlim, 10**(-np.log10(xlim)+c1), c='g')
	for accl in range(int(ACCL_lim10[0]),int(ACCL_lim10[1])+1):
		y1 = 10**accl*np.array(xlim)/(2*np.pi)
		ax.plot(xlim,y1, c='b', lw=.5, alpha=.3)
	for disp in range(int(DISP_lim10[0]),int(DISP_lim10[1])+1):
		y1 = 10**disp*2*np.pi/np.array(xlim)
		ax.plot(xlim,y1, c='r', lw=.5, alpha=.3)  
'''
periods = 10**(np.linspace(-3,1,31))
PGV = np.zeros(31)
for i,period in enumerate(periods):
	if period <= 0.1:
		PGV[i] = (1+15*period)*9.81*period/(2*np.pi)
	elif period <= 0.4:
		PGV[i] = 2.5*9.81*period/(2*np.pi)
	else:
		PGV[i] = 9.81/(2*np.pi)
fig = tripartite_plot(periods,PGV)
plt.savefig('bis_spectra.pdf')
plt.show()

'''
ax = plt.subplot(1,1,1)
ax.set_xlim([0.001,10])
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_ylim([0.001,10])
PGA = 10**(np.linspace(-6,3,10))
PGD = 10**(np.linspace(-6,3,10))
ax.plot(periods, PGV, c='k')
ax.grid(b=True, which='both', color='k', linestyle='-', alpha=.3, lw=.3)
ax.plot([0,10],[0,10], c='b', lw=1)
ax.plot(periods,0.001*2*np.pi/periods, c='r', lw=1)
for value in PGA:
	y1 = value*2*np.pi/periods
	y2 = value*periods/(2*np.pi)
	ax.plot(periods,y1, c='b', lw=.5, alpha=.3) 
	ax.plot(periods,y2, c='r', lw=.5, alpha=.3) 
	for i in range(1,10):
		y1 = np.exp( np.log(i*value) + np.log(2*np.pi/periods) )
		y2 = np.exp( np.log(i*value) - np.log(2*np.pi/periods) )
		ax.plot(periods,y1, c='b', lw=.5, alpha=.3)
		ax.plot(periods,y2, c='r', lw=.5, alpha=.3) 

ax.set_xlabel('Period (sec.)')
ax.set_ylabel('Spectral Velocity')
plt.show()
'''
