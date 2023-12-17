#!/usr/bin/ruby
nums=gets.split(",").map &:to_i
boards=[]
rows=[]
cols=[]
sums=[]
while x=gets do
  x=x.chop
  raise "wrong input" unless x==""
  b=[]
  sum=0
  5.times do
    x=gets
    b << x.split.map{|x|x.to_i}
    b.last.each{|a| sum+=a}
  end
  boards << b
  rows << Array.new(5,0)
  cols << Array.new(5,0)
  sums << sum
end

nums.each do |x|
  boards.size.times do |b_i|
    5.times do |r|
      5.times do |c|
        if boards[b_i][r][c]==x then
          rows[b_i][r] += 1
          cols[b_i][c] += 1
          sums[b_i] -= x
          if rows[b_i][r]==5 or cols[b_i][c]==5 then
            print sums[b_i]*x
            exit
          end
        end
      end
    end
  end
end

