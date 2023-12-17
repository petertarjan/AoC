#!/usr/bin/ruby
last=gets.to_i
sol=0
while x=gets do
  x=x.to_i
  if x>last then sol+=1 end
  last=x
end
p sol
