This project is used to create a simple topic connection between three ROS nodes. 
Two of those are publishers, and the last one is a subscriber. 
The two subcribers sent constantly random ints from 1 to 1000 on sepearate. 
The subsriber must recieve(subscribe) from these topics sets of ints and output
  > the larger number if none of the two ints recieved are prim
  > the smaller if only he is a prime
  > the larger if both are primes
