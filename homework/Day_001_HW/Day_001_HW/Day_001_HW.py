
import numpy as np
import matplotlib.pyplot as plt

w=3
b=0.5

x_line=np.linspace(0,100,101)
y=(x_line+np.random.randn(101)*5)*w+b

plt.plot(x_line,y,'b.',label='data points')
plt.title("Assume we havve data points")
plt.legend(loc='upper left')
plt.show()

y.hat=x_line*w+b
plt.plot(x_line,y,'b.',label='data points')
plt.plot(x_line,y,'r-',label='prediction')
plt.title("Assume we have data points(And the prediction")
plt.legend(loc='upper left')
plt.show()

def mean_absolute_error(y,yp):
    mae=sum(abs(y-yp))/len(y)
    return mae
MAE=mean_absolute_error(y,y_hat)
print("The mean absolute error is %.3f" %(MAE))

def mean_square_error(y,yp):
    mse=sum((y-yp)**2)/len(y)
    return mse
MSE=mean_square_error(y,y_hat)
print("The mean square error is %.3f " %(MSE))
