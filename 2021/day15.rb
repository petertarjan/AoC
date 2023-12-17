#!/usr/bin/ruby
a=[]
while x=gets do
  a << x.chop.chars.map{|c|c.to_i}
end

def solve(a)
  rs=a.size
  cs=a[0].size
  
  d=Array.new(1,[[0,0]])
  vis=Array.new(rs) { Array.new(cs,false) }
  dist=0
  while dist<d.size
    while d[dist].size==0
      dist+=1
      if dist==d.size then return end
    end
    dkey=d[dist].pop
    if vis[dkey[0]][dkey[1]] then next end
    vis[dkey[0]][dkey[1]]=true
#    print dist," ",dkey,"\n"
    if dkey==[rs-1,cs-1] then
      p dist
      return
    end
    [[-1,0],[0,-1],[1,0],[0,1]].each{|p|
      r=dkey[0]+p[0]
      c=dkey[1]+p[1]
      if r>=0 and r<rs then
        if c>=0 and c<cs then
          if not vis[r][c] then
            nv=a[r][c]+dist
            while d.size<=nv do d << [] end
            d[nv] << [r,c]
          end
        end
      end
    }
  end
end

solve(a)

rs=a.size
cs=a[0].size

4.times{|i|
  rs.times{|r|
    cs.times{|c|
      a[r] << a[r][c]+i+1
      if a[r][-1] > 9 then a[r][-1]-=9 end
    }
  }
}

4.times{|i|
  rs.times{|r|
    a << []
    a[r].size.times{|c|
      a.last << a[r][c]+i+1
      if a[-1][-1]>9 then a[-1][-1]-=9 end
    }
  }
}

solve(a)
