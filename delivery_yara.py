def delivery_cost(postcode):
  postcode1=postcode[0].upper()
  postcode2=postcode[0:2].upper()
  if postcode1=='E':
    delivery_cost=0.89
  elif postcode1== 'N':
    delivery_cost=1.99
  elif postcode1== 'W':
    delivery_cost=3.59
  elif postcode2== 'NW':
    delivery_cost=3.99
  elif postcode2== 'SW':
    delivery_cost=1.29
  elif postcode2== 'SE':
    delivery_cost=2.09
  elif postcode2== 'EC':
    delivery_cost=4.89
  elif postcode2== 'WC':
    delivery_cost=9.99
  return delivery_cost
