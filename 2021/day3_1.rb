#!/usr/bin/ruby
c0=Array.new(32,0)
c1=Array.new(32,0)
while x=gets do
  x.size.times{|i| if x[i]=="0" then c0[i]+=1 elsif x[i]=="1" then c1[i]+=1 end }
end
s1=0
s2=0
i=0
while c0[i]+c1[i]>0 do
  s1*=2
  s2*=2
  if c1[i]>c0[i] then
    s1+=1
  else
    s2+=1
  end
  i+=1
end
p s1*s2
