#!/usr/bin/ruby
A=[]
while x=gets do
  A << (x.chop.chars.map &:to_i)
end
fl=0
100.times{
  xfl=[]
  A.size.times{|r|
    A[r].size.times{|c|
      A[r][c]+=1
      if A[r][c]==10 then
        fl+=1
        ([0,r-1].max..[A.size-1,r+1].min).each {|rn|
          ([0,c-1].max..[A[r].size-1,c+1].min).each {|cn|
            if r!=rn or c!=cn then
              xfl << [rn,cn]
            end
          }
        }
      end
    }
  }
  while xfl.size>0 do
    r,c=xfl.pop
    A[r][c]+=1
    if A[r][c]==10 then
      fl+=1
      ([0,r-1].max..[A.size-1,r+1].min).each {|rn|
        ([0,c-1].max..[A[r].size-1,c+1].min).each {|cn|
          if r!=rn or c!=cn then
            xfl << [rn,cn]
          end
        }
      }
    end
  end
  A.size.times{|r|
    A[r].size.times{|c|
      if A[r][c]>9 then A[r][c]=0 end
    }
  }
}
p fl
