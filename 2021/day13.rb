#!/usr/bin/ruby
pt=[]
first=true
while s=gets.chop do
  if s=="" then break end
  x,y=s.split(",").map &:to_i
  pt << [x,y]
end
fl=[]
while s=gets do
  w=s.chop.split
  raise "bad input" unless w[0]=="fold" and w[1]=="along"
  axis,coord=w[2].split("=")
  coord=coord.to_i
  fl << [axis, coord]
end
fl.each{|fo|
  if fo[0]=="x" then
    pt.size.times{|i|
      if pt[i][0]>fo[1] then
        pt[i][0]=2*fo[1]-pt[i][0]
      end
    }
  else
    raise "bad in" unless fo[0]=="y"
    pt.size.times{|i|
      if pt[i][1]>fo[1] then
        pt[i][1]=2*fo[1]-pt[i][1]
      end
    }
  end
  if first then
    print "part1: ",pt.uniq.size,"\n"
    first=false
  end
}

sol=[]
pt.each{|p|
  while p[1]>=sol.size do sol << [] end
  while p[0]>=sol[p[1]].size do sol[p[1]] << " " end
  sol[p[1]][p[0]]="#"
}
puts "part2:",sol.map{|ln|ln.join ""}

