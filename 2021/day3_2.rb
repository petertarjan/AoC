#!/usr/bin/ruby
c0=Array.new(32,0)
c1=Array.new(32,0)
nums=[]
while x=gets do
  nums << x.chop
end
live=Array.new(nums.size,true)
liven=nums.size
nums[0].size.times do |i|
  c0=0
  c1=0
  nums.size.times{|j| if live[j] then if nums[j][i]=="0" then c0+=1 elsif nums[j][i]=="1" then c1+=1 end end }
  if c1>=c0 then
    live.size.times{|j| if live[j] and nums[j][i]=="0" then liven-=1; live[j]=false end}
    if liven==1 then
      break
    end
  else
    live.size.times{|j| if live[j] and nums[j][i]=="1" then liven-=1; live[j]=false end}
    if liven==1 then
      break
    end
  end
end

s=0
live.size.times{|j| if live[j] then s=nums[j].to_i(2) end}

live=Array.new(nums.size,true)
liven=nums.size
nums[0].size.times do |i|
  c0=0
  c1=0
  nums.size.times{|j| if live[j] then if nums[j][i]=="0" then c0+=1 elsif nums[j][i]=="1" then c1+=1 end end }
  if c1<c0 then
    live.size.times{|j| if live[j] and nums[j][i]=="0" then liven-=1; live[j]=false end}
    if liven==1 then
      break
    end
  else
    live.size.times{|j| if live[j] and nums[j][i]=="1" then liven-=1; live[j]=false end}
    if liven==1 then
      break
    end
  end
end

live.size.times{|j| if live[j] then p s*nums[j].to_i(2) end}
