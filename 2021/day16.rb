#!/usr/bin/ruby
$sv=0

def cmb(t,val,v)
#  print t," ",val," ",v,"\n"
  if t==0 then
    val+v
  elsif t==1 then
    val*v
  elsif t==2 then
    [val,v].min
  elsif t==3 then
    [val,v].max
  elsif t==5 then
    val==$z ? v : ((val>v) ? 1 : 0)
  elsif t==6 then
    val==$z ? v : ((val<v) ? 1 : 0)
  else
    raise "!" unless t==7
    val==$z ? v : ((val==v) ? 1 : 0)
  end
end

def parse(s)
  v=s[0..2].to_i(2)
  t=s[3..5].to_i(2)
  $sv+=v
#  puts "V="+v.to_s+" T="+t.to_s
  if t==4 then
    pos=6
    x=""
    while s[pos]=="1" do
      x+=s[pos+1..pos+4]
      pos+=5
    end
    x+=s[pos+1..pos+4]
    pos+=5
    val=x.to_i(2)
#    p x,val
  else
    l=s[6]
    $z=999999999999999999
    val=[0,1,$z,-$z,-1,$z,$z,$z][t]
    if l=="0" then
      len=s[7..21].to_i(2)
      pos=22
      while pos<22+len do
        p,v=parse(s[pos..-1])
        pos+=p
        val=cmb(t,val,v)
      end
    else
      pos=18
      s[7..17].to_i(2).times{
        p,v=parse(s[pos..-1])
        pos+=p
        val=cmb(t,val,v)
      }
    end
  end
  [pos,val]
end

x=gets.strip.chars.map{|c|a=c.to_i(16).to_s(2).rjust(4,"0")}.join("")
p,v=parse(x)
puts "Part1: "+$sv.to_s
puts "Part2: "+v.to_s
