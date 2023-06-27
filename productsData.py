samsungA30 = {
    'Name':'Samsung A30',
    'Price':'15000',
    'Category':'Mobiles'
}
samsungA50 = {
    'Name':'Samsung A50',
    'Price':'15000',
    'Category':'Mobiles'
}
iPhone11p = {
    'Name':'iPhone 11 Pro',
    'Price':'15000',
    'Category':'Mobiles'
}
iPhone11 = {
    'Name':'iPhone 11',
    'Price':'15000',
    'Category':'Mobiles'
}
iPhone12 = {
    'Name':'iPhone 12',
    'Price':'15000',
    'Category':'Mobiles'
}
iPhone12p = {
    'Name':'iPhone 12 Pro',
    'Price':'15000',
    'Category':'Mobiles'
}
iPhone13 = {
    'Name':'iPhone 13',
    'Price':'15000',
    'Category':'Mobiles'
}
iPhone13p = {
    'Name':'iPhone 13 Pro',
    'Price':'15000',
    'Category':'Mobiles'
}
iPhone14 = {
    'Name':'iPhone 14',
    'Price':'15000',
    'Category':'Mobiles'
}
mobMain = {
    'mob1' : samsungA30,
    'mob2' : samsungA50,
    'mob3' : iPhone11,
    'mob4' : iPhone11p,
    'mob5' : iPhone12,
    'mob6' : iPhone12p,
    'mob7' : iPhone13,
    'mob8' : iPhone13p,
    'mob9' : iPhone14
}

laptop4 = {
    'Name' : 'Acer Nitro',
    'Price' : '60000 ',
    'Category': 'Laptops'
}
laptop1 = {
    'Name' : 'HP Pavellion',
    'Price' : '75000 ',
    'Category': 'Laptops'
}
laptop2 = {
    'Name' : 'Mac Book Air',
    'Price' : '160000 ',
    'Category': 'Laptops'
}
laptop3 = {
    'Name' : 'Asus Tuf Gaming',
    'Price' : '87500 ',
    'Category': 'Laptops'
}
laptopMain = {
    'lap1' : laptop1,
    'lap2' : laptop2,
    'lap3' : laptop3,
    'lap4' : laptop4,
}

shoe1 = {
    'Name':'Nike Sneaker',
    'Price':'40000 ',
    'Category':'Shoes'
}
shoe2 = {
    'Name':'Adidas Air',
    'Price':'3000 ',
    'Category':'Shoes'
}
shoe3 = {
    'Name':'Puma Back Court',
    'Price':'5000 ',
    'Category':'Shoes'
}
shoe4 = {
    'Name':'Reebok Sprinter',
    'Price':'1300 ',
    'Category':'Shoes'
}
shoeMain = {
    'sh1' : shoe1,
    'sh2' : shoe2,
    'sh3' : shoe3,
    'sh4' : shoe4,
}

cloth1 = {
    'Name':'Gucci Shirt',
    'Price':'3000 ',
    'Category':'Clothes'
}
cloth2 = {
    'Name':'Adidas',
    'Price':'5000 ',
    'Category':'Clothes'
}
cloth3 = {
    'Name':'Louis Vuitton',
    'Price':'1000 ',
    'Category':'Clothes'
}
cloth4 = {
    'Name':'H&M Formals',
    'Price':'9000 ',
    'Category':'Clothes'
}
cloth5 = {
    'Name':'Puma Sporty',
    'Price':'6000 ',
    'Category':'Clothes'
}
clothMain ={
    'cl1' : cloth1,
    'cl2' : cloth2,
    'cl3' : cloth3,
    'cl4' : cloth4,
    'cl5' : cloth5,
}
productsMain = {
    'mobile' : mobMain,
    'laptop' : laptopMain,
    'shoes' : shoeMain,
    'cloth' : clothMain,
}
try:
    def addproduct(NAME, PRICE, CAT):
        name = NAME
        price = PRICE
        productsMain[CAT].update({f'mob{len(productsMain[CAT])+1}':{
            'Name':name,
            'Price':price,
            'Category':CAT
        }})
        return

    def removeProduct(no, CAT):
        list1 = list(productsMain[CAT])[no-1]
        del productsMain[CAT][list1]
        return
except KeyError:
    print("\033[0;31;40mError: Key doesn't exist\033[0;37;40m")
except IndexError:
    print("\033[0;31;40mError: Invalid choice!\033[0;37;40m")