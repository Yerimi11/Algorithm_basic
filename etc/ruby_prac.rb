# convert("   tekramngnaad   ") == "DAANGNMARKET"
# convert("   torrak         ") == "KARROT"
# convert("   remmus         ") == "SUMMER"

def convert(input)
	res = input.strip
	res = res.reverse
	res = res.upcase
    puts res
end

convert("   tekramngnaad   ")
convert("   torrak         ")
convert("   remmus         ")