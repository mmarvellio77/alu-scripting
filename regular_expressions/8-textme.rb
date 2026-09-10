#!/usr/bin/env ruby
line = ARGV[0]

if line =~ /\[from:([^\]]*)\]\s*\[to:([^\]]*)\]\s*\[flags:([^\]]*)\]/
  puts "#{$1},#{$2},#{$3}"
end
