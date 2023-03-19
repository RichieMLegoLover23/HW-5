#question 1
#Get the actual value of the property from the user
actual_value = float(input("Enter the actual value of the property: "))

#Calculate the assessment value and property tax
assessment_value = 0.6 * actual_value
property_tax = 0.007 * assessment_value

#Display the results to the user
print("Assessment value: $", format(assessment_value, ",.2f"), sep="")
print("Property tax: $", format(property_tax, ",.2f"), sep="")




























#question 2
classA = 20
classB = 15
classC = 10

ticketA_sold = int(input('Number of class A tickets sold: '))
ticketB_sold = int(input('Number of class B tickets sold: '))

ticketC_sold = int(input('Number of class C tickets sold: '))

revA = ticketA_sold * classA

revB = ticketB_sold * classB

revC = ticketC_sold * classC

totalincome_fromsales = revA + revB + revC

print('Total income from ticket sales is:', totalincome_fromsales )
















#question 3
# Get the total sales for the month from the user
total_sales = float(input("Enter the total sales for the month: "))

# Calculate the county sales tax, state sales tax, and total sales tax
county_sales_tax = 0.025 * total_sales
state_sales_tax = 0.05 * total_sales
total_sales_tax = county_sales_tax + state_sales_tax

# Display the results to the user
print("County sales tax: $", format(county_sales_tax, ",.2f"), sep="")
print("State sales tax: $", format(state_sales_tax, ",.2f"), sep="")
print("Total sales tax: $", format(total_sales_tax, ",.2f"), sep="")
