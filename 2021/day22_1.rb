#!/usr/bin/ruby
grid=Array.new(101) {Array.new(101) { Array.new(101,0) } }

xs=[]
ys=[]
zs=[]

while x=gets do
  wut,coords=x.strip.split
  x,y,z=coords.split(",")

  x=x.split("=")
  raise "wtf x" unless x[0]=="x"
  x=x[1].split("..").map{|a|a.to_i+50}

  y=y.split("=")
  raise "wtf y" unless y[0]=="y"
  y=y[1].split("..").map{|a|a.to_i+50}

  z=z.split("=")
  raise "wtf z" unless z[0]=="z"
  z=z[1].split("..").map{|a|a.to_i+50}
  
  if wut=="on" then val=1 else
    raise "wtf dir" unless wut=="off"
    val=0
  end

  ([x[0],0].max..[x[1],100].min).each{|xx|
    ([y[0],0].max..[y[1],100].min).each{|yy|
      ([z[0],0].max..[z[1],100].min).each{|zz|
        grid[xx][yy][zz]=val
      }
    }
  }
end

print "part1: ",(grid.map{|p|p.map{|l|l.inject &:+}.inject &:+}.inject &:+),"\n"
