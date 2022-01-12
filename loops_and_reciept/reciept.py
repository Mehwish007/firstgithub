#create a company name
company_name="coding temple, inc."
company_adress="283 Franklin St."
company_city="Boston, MA"
#declare ending message
message="Thanks for shopping with us today!"
#create a top boarder
print("*" * 50)
#print company information first
print("\t\t{}".format(company_name.title( )))
print("\t\t{}".format(company_adress))
print("\t\t{}".format(company_city))
#print a line between sections
print("=" * 50)
#print out header for section of items
print("\tProduvt Name\tproduct Price")
#products
p1_name="Books"
p2_name="computer"
p3_name="monitor"
p1_price="49.95"
p2_price="579.99"
p3_price="124.89"
#create print statement for each product
print("\t{}\t\t${}".format(p1_name.title(), p1_price))
print("\t{}\t\t${}".format(p2_name.title(),p2_price))
print("\t{}\t\t${}".format(p3_name.title(),p3_price))
#print a line between sections
print('=' * 50)
#print out header for section of total
print("\t\tTotal")
#calculate total price and print out
total=p1_price+p2_price+p3_price
print("\t\t\t${}".format(total))
#print a line between sections
print("=" * 50)
#output thankyou message
print("\n\t{}\n".format(message))
#create a bottom boarder
print("*" * 50)

          
          
