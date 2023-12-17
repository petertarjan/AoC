#!/usr/bin/ruby
A=[]
while x=gets do
  A << (x.chop.split("").map &:to_i)
end
R=A.size
C=A[0].size

vis=[]
R.times{|r|
  vis << Array.new(C,false)
  C.times{|c| if A[r][c]==9 then vis[r][c]=true end}
}
sol=1
basins=[]
(0...R).each{|r|
  (0...C).each{|c|
    if vis[r][c] then next end
    prc = []
    prc << [r,c]
    vis[r][c]=true
    cnt=1
    while prc.size > 0 do
      p=prc.pop
      if p[0]>0 then
        if not vis[p[0]-1][p[1]] then
          vis[p[0]-1][p[1]]=true
          cnt+=1
          prc << [p[0]-1, p[1]]
        end
      end
      if p[1]>0 then
        if not vis[p[0]][p[1]-1] then
          vis[p[0]][p[1]-1]=true
          cnt+=1
          prc << [p[0], p[1]-1]
        end
      end
      if p[0]<R-1 then
        if not vis[p[0]+1][p[1]] then
          vis[p[0]+1][p[1]]=true
          cnt+=1
          prc << [p[0]+1, p[1]]
        end
      end
      if p[1]<C-1 then
        if not vis[p[0]][p[1]+1] then
          vis[p[0]][p[1]+1]=true
          cnt+=1
          prc << [p[0], p[1]+1]
        end
      end
    end
#    p cnt
    basins << cnt
  }
}
b=basins.sort
puts b[b.size-1]*b[b.size-2]*b[b.size-3]
