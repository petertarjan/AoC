#!/usr/bin/ruby
A=[]
while x=gets do
  A << (x.chop.split("").map &:to_i)
end
R=A.size
C=A[0].size

s=0
(0...R).each{|r|
  (0...C).each{|c|
    ok=true
    if r>0 then
      if A[r][c]>=A[r-1][c] then ok=false end
    end
    if c>0 then
      if A[r][c]>=A[r][c-1] then ok=false end
    end
    if r<R-1 then
      if A[r][c]>=A[r+1][c] then ok=false end
    end
    if c<C-1 then
      if A[r][c]>=A[r][c+1] then ok=false end
    end
    if ok then
#      p [r,c,A[r][c]]
      s+=A[r][c]+1
    end
  }
}
p s
