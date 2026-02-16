# from ecommerce.customer import contact  #intra packages refrence
# from ..customer import contact
# contact.customer_contact()

# print("sales module initialize",__name__)
def cal_tax():
    print("tax")

def cal_shipping():
    print("shipping")

if __name__ == "__main__":
    print("sales is started ")
    cal_tax()