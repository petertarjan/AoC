#!/usr/bin/ruby
a=gets.to_i
b=gets.to_i
c=gets.to_i
last=a+b+c
sol=0
while x=gets do
  d=x.to_i
  x=b+c+d
  if x>last then sol+=1 end
  last=x
  a=b
  b=c
  c=d
end
p sol
