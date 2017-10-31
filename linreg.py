# linreg.py
#
# Standalone Python/Spark program to perform linear regression.
# Performs linear regression by computing the summation form of the
# closed form expression for the ordinary least squares estimate of beta.
# 
# TODO: Write this.
# 
# Takes the yx file as input, where on each line y is the first element 
# and the remaining elements constitute the x.
#
# Usage: spark-submit linreg.py <inputdatafile>
# Example usage: spark-submit linreg.py yxlin.csv
#
#

import sys
import numpy as np

from pyspark import SparkContext
from numpy.linalg import inv


if __name__ == "__main__":
  if len(sys.argv) !=2:
    print >> sys.stderr, "Usage: linreg <datafile>"
    exit(-1)

  sc = SparkContext(appName="LinearRegression")

  # Input yx file has y_i as the first element of each line 
  # and the remaining elements constitute x_i
  yxinputFile = sc.textFile(sys.argv[1])
  
  
  xlines = yxinputFile.map(lambda line: line.split(',')[1:])  #getting the values of the x
  x =np.array(xlines.collect()).astype('float')               #putting values of x into an array

  ylines = yxinputFile.map(lambda line: line.split(',')[0])   #getting the values of y
  y = np.array(ylines.collect()).astype('float')              #putting the values of y into an array

  
 #
  # Add your code here to compute the array of 
  # linear regression coefficients beta.
  # You may also modify the above code.
  #

  new_x=np.c_[np.ones((len(x),1)),x]                          #adding an extra term with ones as values to the x array.this increases the dimensions of the array for multiplication
  
  next_x=sc.parallelize(new_x)                               #parallelizing the data for mapreduce x*xtranspose
  next_y=sc.parallelize(np.c_[y,new_x])                      #parallelizing the data for mapreduce x*y
  
    
  
  A_map = next_x.map(lambda m:("KeyA",(np.array(m).reshape(len(m),1) * np.transpose(np.array(m).astype('float')).reshape(1,len(m)))))   
  A_reduce=A_map.reduceByKey(lambda x,y : x+y).values()                                                             #value of x*xtranspose
  B_map = next_y.map(lambda n:("KeyB",(np.array(n)[1:len(n)].reshape(len(n)-1,1) * np.array(n)[0].reshape(1,1))))
  B_reduce=B_map.reduceByKey(lambda x,y : x+y).values()                                                             #value of x*y      
  X= inv(np.array(A_reduce.collect())).squeeze()                                                                    #computing the inverse of x*xtranspose ans squeezzing it to fit the dimensions       

  Y= np.array(B_reduce.collect())                      

  result = np.dot(X,Y)                                                                                              #computing the value of the beta coefficient
  
  


 
  
  # print the linear regression coefficients in desired output format`
  print "beta: "
  for coeff in result:
       print coeff

  sc.stop()
