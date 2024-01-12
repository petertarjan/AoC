#!/usr/bin/ruby

require 'fc'

cmd=[]
xs=[]
ys=[]
zs=[]
while x=gets do
  wut,coords=x.strip.split
  x,y,z=coords.split(",")

  x=x.split("=")
  raise "wtf x" unless x[0]=="x"
  x=x[1].split("..").map &:to_i

  y=y.split("=")
  raise "wtf y" unless y[0]=="y"
  y=y[1].split("..").map &:to_i

  z=z.split("=")
  raise "wtf z" unless z[0]=="z"
  z=z[1].split("..").map &:to_i
  
  if wut=="on" then val=1 else
    raise "wtf dir" unless wut=="off"
    val=0
  end

  x[1]+=1
  y[1]+=1
  z[1]+=1

  xs << x[0]
  xs << x[1]
  ys << y[0]
  ys << y[1]

  cmd << [x,y,z,val]
end

xs=xs.sort.uniq
ys=ys.sort.uniq
xd={}
yd={}
xs.size.times{|i|xd[xs[i]]=i}
ys.size.times{|i|yd[ys[i]]=i}

grid=Array.new(xs.size-1) { Array.new(ys.size-1,nil) }

cmd.each{|x,y,z,v|
  (xd[x[0]]...xd[x[1]]).each{|xi|
    (yd[y[0]]...yd[y[1]]).each{|yi|
      if grid[xi][yi]==nil then
        grid[xi][yi]=FastContainers::PriorityQueue.new(:min)
      end
      grid[xi][yi].push([z[1], grid[xi][yi].size, v],z[0])
    }
  }
}

sol=0
grid.each_with_index{|gx,xi|
  xa=xs[xi+1]-xs[xi]
  gx.size.times{|yi|
    if grid[xi][yi]!=nil and grid[xi][yi].size>0 then
      xya=xa*(ys[yi+1]-ys[yi])
      t=grid[xi][yi].top_key.to_i
      curr=FastContainers::PriorityQueue.new(:max)
      while 1 do
        while grid[xi][yi]!=nil and grid[xi][yi].size>0 and grid[xi][yi].top_key.to_i==t do
          curr.push([grid[xi][yi].top[0], grid[xi][yi].top[2]], grid[xi][yi].top[1])
          grid[xi][yi].pop
        end
        if curr.size>0 then
          tt=curr.top[0]
          if grid[xi][yi]!=nil and grid[xi][yi].size>0 and grid[xi][yi].top_key.to_i<tt then
            tt=grid[xi][yi].top_key.to_i
          end
        elsif grid[xi][yi]!=nil and grid[xi][yi].size>0 then
          tt=grid[xi][yi].top_key.to_i
        else
          break
        end
        if curr.size>0 and curr.top[1]>0 then
          sol+=xya*(tt-t)
        end
        while curr.size>0 and curr.top[0]<=tt do
          curr.pop
        end
        t=tt
      end
    end
  }
}
p sol
