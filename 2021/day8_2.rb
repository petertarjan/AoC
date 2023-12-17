#!/usr/bin/ruby
sol=0
while x=gets do
  s=x.split
  raise "wrong input" unless s.size==15
  occ=Array.new(7,0)
  c1=c4=-1
  s[0..9].each{|x|
    x.split("").each{|c|occ[c.ord-'a'.ord]+=1}
    if x.size==4 then c4=x
    elsif x.size==2 then c1=x end
  }
  dc=Array.new(7,0)
  occ.each_with_index{|o,i|
    if o==8 then
      if c1.chars.include? (i+'a'.ord).chr then dc[i]='c'.ord-'a'.ord
      else dc[i]='a'.ord-'a'.ord end
    elsif o===6 then dc[i]='b'.ord-'a'.ord
    elsif o==7 then
      if c4.chars.include? (i+'a'.ord).chr then dc[i]='d'.ord-'a'.ord
      else dc[i]='g'.ord-'a'.ord end
    elsif o==4 then dc[i]='e'.ord-'a'.ord
    elsif o==9 then dc[i]='f'.ord-'a'.ord
    elsif o==7 then dc[i]='g'.ord-'a'.ord
    else raise "watt?" end
  }
#  (11..14).each{|i| if [2,3,4,7].include? s[i].size  then sol+=1 end }
  v=0
  (11..14).each{|i|d=s[i].chars.map{|c|dc[c.ord-'a'.ord]}.sort.map{|j|(j+'a'.ord).chr}.join
    if d=="abcefg" then v=10*v+0
    elsif d=="cf" then v=10*v+1
    elsif d=="acdeg" then v=10*v+2
    elsif d=="acdfg" then v=10*v+3
    elsif d=="bcdf" then v=10*v+4
    elsif d=="abdfg" then v=10*v+5
    elsif d=="abdefg" then v=10*v+6
    elsif d=="acf" then v=10*v+7
    elsif d=="abcdefg" then v=10*v+8
    elsif d=="abcdfg" then v=10*v+9
    else raise d end
  }
  sol+=v
end
print sol

