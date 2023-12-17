#!/usr/bin/ruby
cmd=[]
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

  x[1]+=1
  y[1]+=1
  z[1]+=1

  xs << x[0]
  xs << x[1]
  ys << y[0]
  ys << y[1]
  zs << z[0]
  zs << z[1]

  cmd << [x,y,z,val]
end

xs=xs.sort.uniq
ys=ys.sort.uniq
zs=zs.sort.uniq
xd={}
yd={}
zd={}
xs.size.times{|i|xd[xs[i]]=i}
ys.size.times{|i|yd[ys[i]]=i}
zss=zs.size
zss.times{|i|zd[zs[i]]=i}

grid=Array.new(xs.size-1) { Array.new(ys.size-1,0) }


def dump(z)
  if z==0 then
    print "-"
    return
  end
  while z>0 do
    print z%2
    z=z>>1
  end
end

cmd.each{|x,y,z,v|
  (xd[x[0]]...xd[x[1]]).each{|xi|
    (yd[y[0]]...yd[y[1]]).each{|yi|
      if v==1 then
        grid[xi][yi]=grid[xi][yi]|((1 << zd[z[1]])-(1 << zd[z[0]]))
      else
        zi0=zd[z[0]]
        zi1=zd[z[1]]
        grid[xi][yi]=grid[xi][yi]&(((((1<<(zss-zi1))-1) << zi1))|((1 << zi0)-1))
      end
    }
  }
}

sol=0
grid.each_with_index{|gx,xi|
  gx.size.times{|yi|
    (zs.size-1).times{|zi|
      if (gx[yi]&(1 << zi))>0 then
        sol+=(xs[xi+1]-xs[xi])*(ys[yi+1]-ys[yi])*(zs[zi+1]-zs[zi])
      end
    }
  }
}
p sol
