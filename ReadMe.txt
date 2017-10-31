						Assignment 3									Pooja Mounika Poluru									ppoluru@uncc.edu									800969916-----------------------------------------------------------------------------------------------------------------------------------------------------------------
  Interface : Python                                        
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Steps to execute on cluster:
1. Log into dsba hadoop cluster using putty
2. put the input files and source code file in dsba hadoop cluster
        scp /home/cloudera/Desktop/linreg.py <username>@dsba-hadoop.uncc.edu: /users/<username>/
    Ex: scp /home/cloudera/Desktop/linreg.py ppoluru@dsba-hadoop.uncc.edu: /users/ppoluru/
3. Put the input files in the HDFS.
	hadoop fs -put /users/<username>/yxlin2.csv <hdfs path where input file is stored>
    Ex: hadoop fs -put /users/ppoluru/yxlin1.csv /user/ppoluru/yxlin1.csv
	hadoop fs -put /users/ppoluru/yxlin2.csv /user/ppoluru/yxlin2.csv
4. Run the following command to generate the output
        spark-submit <source code path in cluster> <HDFS path of input file> > <output file path>  
        spark-submit /users/ppoluru/linreg.py /user/ppoluru > /users/ppoluru/yxlin.out
	spark-submit /users/ppoluru/linreg.py /user/ppoluru > /users/ppoluru/yxlin2.out
5. To view the output file
	Ex: cat <output file path>
        cat /users/ppoluru/yxlin.csv
	cat /users/ppoluru/yxlin2.csv
	