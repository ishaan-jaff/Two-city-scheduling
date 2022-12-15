"""

[[10,20],[30,40],[400,50],[30,200]]
0,0,1,1 => 40 + 50 + 200 => 290
0,1,1,0 => 50 + 80 => 130 

[10, 10, 350, 170]
{
0: 10
1: 10
2: 350
3: 170
}
[[400,50],[30,200],[10,20],[30,40],]
# in order to minmize cost, prioritse giving lowest to passengers with highest differences 

# 
"""

def two_city_scheduling(costs):
  # Write your code
  # sort based on diff bw costs
  # at each point make best decision

  #sorted_costs = sorted(costs)
  # print(costs)
  costs.sort(key=lambda x: abs(x[1]-x[0]))
  num_each = len(costs)/2
  num_0 = 0
  num_1 = 0
  total = 0
  for elem in costs[::-1]:
    # print(elem)
    if elem[1] < elem[0]:
      if num_1 < num_each:
        num_1 +=1
        total += elem[1]
      else: # send to city 0, since no place in city 1 
        total += elem[0]
        num_0 +=1 
    else: # send to city 0, since cheaper
      if num_0 < num_each:
        num_0 +=1
        total+= elem[0]
      else:
        # send to city 1 since 0 has no place
        total+= elem[1]
        num_1 +=1 
  return total
print(two_city_scheduling([[400,50],[30,200],[10,20],[30,40]]))



