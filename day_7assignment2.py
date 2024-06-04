# # find the area of circle
# try:
#  class circle:
#     def __init__(self,radius):
#      self.ra_dius=radius
#     def display(self):
#       ra_dius1=3.14*self.ra_dius*self.ra_dius
#       print("the area of circle is :",ra_dius1)
#  radius=int(input("enter the value:"))
#  ob_ject=circle(radius) 
#  print(ob_ject.display())
# except Exception as e:
#     print("Please enter the a numerical value")

#  # 
# try:
#  class discount:
#      def __init__(self,dis,amount):
#       self.dis_c=dis
#       self.amo_unt=amount
#      def discount_counter(self):
#          dis_count_1=(self.dis_c*self.amo_unt)/100
#          final_amo_unt=amount-dis_count_1
#          print("the amount after apply discount",final_amo_unt)
#  amount=int(input("Enter the amount:"))
#  dis=int(input("Enter the discount amount:"))
#  obj=discount(dis,amount)  
#  print(obj.discount_counter())
# except Exception as e:
#   print("enter the numerical value") 



class vowel:
     def __init__(self,vo_wel):
       self.vo_wel1=vo_wel
     def count_vowels(self):
         print(self.vo_wel1.count('aeiouAEIOU'))     
vo_wel=input("enter the srting:") 
obj=vowel(vo_wel) 
print(obj.count_vowels())

    