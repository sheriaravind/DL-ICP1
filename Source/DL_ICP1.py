import tensorflow as tf
#define the matrixes for a , b and c
a = tf.constant([1,2,2,1], name="matrix_a",shape=[2,2])
b = tf.constant([3,4,4,3], name="matrix_b",shape=[2,2])
c = tf.constant([5,6,6,5], name="matrix_c",shape=[2,2])
#Using pow function to get the square of the elements of the matrix
sq_a = tf.pow(a,2)
#define the addition operation for sq_a + b
y=tf.add(sq_a,b)
#define the multiply operation for y * c
z=tf.matmul(y,c)

#create the session for evaluating tensor objects
with tf.Session() as s:

    #print a*a
    print(s.run(sq_a))
    #print (a*a+b)
    print(s.run(y))
    #print (a*a+b)*c
    print(s.run(z))