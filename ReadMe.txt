				 Implementing MLR using SPARK in the UNCC cluster
				 
------------------------------------------------------------------------------------------------------------------------------------------
  Interface : Python                                        
------------------------------------------------------------------------------------------------------------------------------------------
Here yxlin1.csv and yxlin2.csv are the input files.
 And the output files are named and yxlin.out and yxlin2.out

Steps to execute on cluster:
1. Log into dsba hadoop cluster using putty

2. put the input files and source code file in dsba hadoop cluster
        scp /home/cloudera/Desktop/linreg.py <username>@dsba-hadoop.uncc.edu: /users/<username>/
    Ex: scp /home/cloudera/Desktop/linreg.py ppoluru@dsba-hadoop.uncc.edu: /users/xyz/
    
3. Put the input files in the HDFS.
	hadoop fs -put /users/<username>/yxlin2.csv <hdfs path where input file is stored>
    Ex: hadoop fs -put /users/xyz/yxlin1.csv /user/xyz/yxlin1.csv
	hadoop fs -put /users/xyz/yxlin2.csv /user/xyz/yxlin2.csv
	
4. Run the following command to generate the output
        spark-submit <source code path in cluster> <HDFS path of input file> > <output file path>  
        spark-submit /users/xyz/linreg.py /user/xyz > /users/xyz/yxlin.out
	spark-submit /users/xyz/linreg.py /user/xyz > /users/xyz/yxlin2.out
	
5. To view the output file
	Ex: cat <output file path>
        cat /users/xyz/yxlin.csv
	cat /users/xyz/yxlin2.csv
	
