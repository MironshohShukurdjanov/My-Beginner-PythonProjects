# Format Specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many space
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 30000000.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:}")
print(f"Price 3 is ${price3:+}")