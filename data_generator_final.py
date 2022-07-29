from sklearn.utils import shuffle
import random

# ID thẻ: CardIdGenerator(length)
# Tên chủ thẻ: userNameGenerator(length)
# Hãng xe và loại xe: vehicleCompanyGenerator(length)
# Id hộ gia đình: idHoGenerator(10)
# ID chủ thẻ: userIdGenerator(10)
# Biển số xe :licensePlateArrayGenerator(10)

# Tao ra mang ID card la 1 so random co 5 chu so khong trung lap nhau
cardIdArray = []

def CardIdGenerator(length):
    lengthOfCardId = len(cardIdArray)
    checkCardId = 1
    while lengthOfCardId < length:
        x = random.randint(10000, 99999)
        for i in range(0, lengthOfCardId - 1):
            if x == cardIdArray[i]:
                checkCardId = 0
            else:
                checkCardId = 1
        if checkCardId == 1:
            cardIdArray.append(x)
        lengthOfCardId = len(cardIdArray)
    print(cardIdArray)
    

# Tao random ten nguoi dung tu mot bo du lieu cho truoc, lay ngau nhien FirstName ghep voi LastName
sourceUserFirstName = ['Lucie', 'Nancy', 'Rebekah', 'Maria', 'Jamie', 'Ashley', 'Rhonda', 'Poppy', 'Kye', 'Melanie', 'Lee', 'Fiona', 'Kyra', 'Ann', 'Daisy', 'Meghan', 'Neve', 'Leila', 'Willie', 'Mollie', 'Nannie', 'Kathruyn', 'Lena', 'Kaira', 'Jesse', 'Annabel', 'Pauge', 'Paige', 'Hafsa', 'Elise', 'Robin', 'Franki', 'Frances', 'Alya', 'Rina', 'Irene', 'Rosemary', 'Monica', 'Alicia', 'Lilly', 'Lilian', 'Eleanor', 'Ella', 'Kristina', 'Tiphanie', 'Morgan', 'Natasha', 'Tassa', 'Elena', 'Yasmin', 'Anastashia', 'Asya', 'Francis', 'Rosie', 'Jennifer', 'Jenni', 'Joel', 'Minnie', 'Mina', 'Talia', 'Tiffani', 'Christina', 'Erica', 'Florence', 'Jodie', 'Thea', 'Alannal', 'Edith', 'Frankie', 'Fanni', 'Alice', 'Allie', 'Chelsea', 'Kayla', 'Marine', 'Milicent', 'Millie', 'Amina', 'Nora', 'Anisa', 'Zara', 'Grace', 'Saffon', 'Angela', 'Naomi', 'Elin', 'Bethan', 'Troy', 'Lana', 'Fleur', 'Esther', 'Kian', 'Fannie', 'Hanna', 'Ruth', 'Sharon', 'Elesha', 'Adrina', 'Getrude', 'Laura', 'Hollie', 'Fern', 'Olive', 'Rosa', 'Luccia']
sourceUserLastName = ['Hernandez', 'Lord', 'Robinson', 'Herbert', 'Beck', 'Griffin', 'Paker', 'Hicks', 'Aguilar', 'Smith', 'Hart', 'Edwards', 'Carter', 'Greene', 'Schmidt', 'Gill', 'Adkins', 'Duccan', 'King', 'Hunter', 'Glover', 'Chapman', 'Bird', 'Ayala', 'Alavers', 'Littel', 'Jame', 'Henderson', 'Thornton', 'Horton', 'Matinezs', 'Donaldson', 'Watts', 'Hommond', 'Thompson', 'Green', 'Morton', 'Padilla', 'Bailey', 'Papoy', 'Watson', 'Moore','Liu', 'Ross', 'Phelps', 'Graves', 'Peterson', 'Larson', 'Gughes', 'Marsh', 'Holland', 'Herrera', 'Hopkins', 'Aguirre', 'Copper', 'Simpson', 'Hussain', 'Day', 'Santiago', 'Le', 'Meijia', 'Alvardo', 'Dawson', 'Gregory', 'Saunders', 'Patel', 'Hogan', 'Butler', 'Frazier', 'Baker', 'Carey', 'Hayes', 'Deans', 'Todd', 'Khan', 'Dennis', 'Pearson', 'Poberto', 'Laing', 'Coles', 'Newman', 'Hunt', 'Wright', 'Jordan', 'Baxter', 'Mccoy', 'Humphreys', 'Wheeler', 'Brady', 'Russel', 'Gaedner', 'Harry', 'Emily', 'Canatan', 'Kimmich', 'Ronanldo', 'Messie', 'Debruyer', 'Degear', 'Kin', 'Klau', 'Macerlo', 'Suarez', 'Ramos', 'Zidane', 'Kaka', 'Carlos', 'Colombie']
userNameArray = []
userFirstNameArray = [] #Dung de so sanh lay ra id Ho

def userNameGenerator(length):
    global userNameArray
    lengthOfSourceUserFirstName = len(sourceUserFirstName)
    lengthOfSourceUserLastName = len(sourceUserLastName)
    lengthOfUserNameArray = len(userNameArray)
    while lengthOfUserNameArray < length:
        firstName = sourceUserFirstName[random.randint(0, lengthOfSourceUserFirstName - 1)]
        lastName = sourceUserLastName[random.randint(0, lengthOfSourceUserLastName - 1)]
        userName = firstName + ' ' + lastName
        userNameArray.append(userName)
        userFirstNameArray.append(firstName)
        lengthOfUserNameArray = len(userNameArray)
    print(userNameArray)
        

# Tao ra Hang xe la random trong mot mang du lieu cho truoc
sourceCarsCompany = ['Toyota', 'Volkswagen', 'Nissan', 'Renault', 'Kia', 'Huyndai', 'Chevrolet', 'Cadillac', 'Ford', 'Honda', 'Fiat', 'Chrysler','Citroen', 'Peugeot', 'Suzuki','Mercedes-Benz', 'BMW', 'Geely', 'Mazda', 'Audi', 'Dacia', 'Dewwoo', 'Ferrari', 'Alfa Romeo', 'Great Wall', 'Infiniti', 'Jaguar', 'Lamborghini', 'Lancia', 'Land Rover', 'Lexus', 'BYD', 'MG', 'Mini', 'Mitsubishi', 'Acura', 'Opel', 'Chery', 'Porsche', 'Rover', 'Saab', 'Seat', 'Skoda', 'SsangYoug', 'Subaru' , 'Volvo', 'VAZ', 'GMC' , 'Aston Martin', 'Bugatti', 'Buick', 'Bentley', 'Dodge', 'GAZ' , 'Holden', 'Hummer', 'Jeep', 'Koenigsegg', 'Lincoln', 'Lotus', 'Mahindra', 'Maserati', 'Maybach', 'McLaren', 'Perodua', 'pontiac', 'Proton', 'Ram', 'Polls Royce', 'Tata', 'Tesla', 'Iveco', 'Vauxhall', 'Abarth', 'Baojun', 'Borgward', 'Changan', 'Detroit Electric', 'Donkervoort', 'Elfin', 'Englon', 'FAW', 'Fisker', 'Gonow', 'Gumpert', 'Gafei', 'Haima', 'Hawtai','IKCO', 'Karma', 'Ionini', 'Luxgen', 'Mastretta', 'Pagani','Smart', 'Yulon', 'Zenvo', 'Zotye', 'Carbon Motors', 'Pilley', 'XinKai']
sourceBikeCompany = ['Honda', 'Yamaha', 'Piaggio', 'SYM', 'Suzuki', 'Triumph', 'Harley Davidson', 'Ducati', 'KTM', 'Kawasaki']
sourceBicycleCompany = ['Trinx', 'Merida', 'Trek', 'Specialized', 'Canondale', 'Konna', 'Scott', 'Santa Cruz', 'Martin', 'GT', 'Giant']


#Car
carCompany = []
carType = []

def carCompanyGenerator (length):
    lengthOfSourceCarsCompany = len(sourceCarsCompany)
    lengthOfCarCompany = len(carCompany)
    while lengthOfCarCompany < length:
        car = sourceCarsCompany[random.randint(0, lengthOfSourceCarsCompany -1)]
        carCompany.append(car)
        carType.append('Car')
        lengthOfCarCompany = len(carCompany)


#Bike
bikeCompany = []
bikeType = []

def bikeCompanyGenerator (length):
    lengthOfSourceBikeCompany = len(sourceBikeCompany)
    lengthOfBikeCompany = len(bikeCompany)
    while lengthOfBikeCompany < length:
        bike = sourceBikeCompany[random.randint(0, lengthOfSourceBikeCompany -1)]
        bikeCompany.append(bike)
        bikeType.append('Bike')
        lengthOfBikeCompany = len(bikeCompany)


#bicycle
bicycleCompany = []
bicycleType = []

def bicycleCompanyGenerator (length):
    lengthOfSourceBicycleCompany = len(sourceBicycleCompany)
    lengthOfBicycleCompany = len(bicycleCompany)
    while lengthOfBicycleCompany < length:
        bicycle = sourceBicycleCompany[random.randint(0, lengthOfSourceBicycleCompany -1)]
        bicycleCompany.append(bicycle)
        bicycleType.append('Bicycle')
        lengthOfBicycleCompany = len(bicycleCompany)


# Tao ham tạo ra tên các hãng xe
vehicleCompanyArray = []
vehicleTypeArray = []



def vehicleCompanyGenerator(length):
    SumCars = int(2*length/5)
    SumBike = int(2*length/5)
    SumBicycle = length - SumBike - SumCars
    carCompanyGenerator(SumCars)
    bikeCompanyGenerator(SumBike)
    bicycleCompanyGenerator(SumBicycle)
    global vehicleCompanyArray
    vehicleCompanyArray = carCompany + bikeCompany + bicycleCompany
    global vehicleTypeArray 
    vehicleTypeArray = carType + bikeType + bicycleType
    print(vehicleCompanyArray)
    print(vehicleTypeArray)


# Tao mang chua ID các hộ gia đình, những người cùng FirstName sẽ có cùng 1 ID hộ gia đình, những người không cùng FirstName sẽ 
# có ID Hộ khác nhau

#Tao ra các ID Hộ mẫu
sourceIdHoNumeber = []
sourceIdHo = []
userOfIdHo = []

def sourceIdHoNumberGenerator(length):
    lengthOfSourceIdHoNumber = len(sourceIdHoNumeber)
    check = 1
    while lengthOfSourceIdHoNumber < length:
        x = random.randint(10000, 99999)
        for i in range(0, lengthOfSourceIdHoNumber - 1):
            if x == sourceIdHoNumeber[i]:
                check = 0
            else:
                check = 1
        if check == 1:
            sourceIdHoNumeber.append(x)
            lengthOfSourceIdHoNumber = len(sourceIdHoNumeber)
    
def sourceIdHoGenerator(length):
    sourceIdHoNumberGenerator(length)
    for i in range (0, length):
        string = "HO{}"
        string = string.format(sourceIdHoNumeber[i])
        sourceIdHo.append(string)
    

def idHoGenerator(length):
    sourceIdHoGenerator(length)
    for i in range(0, len(userFirstNameArray)):
        IdHo = sourceIdHo[i]
        userOfIdHo.append(IdHo)
    for j in range(0, len(userFirstNameArray) - 1):
        for k in range (j, len(userFirstNameArray)):
            if userFirstNameArray[k] == userFirstNameArray[j]:
                userOfIdHo[k] = userOfIdHo[j]
    print(userOfIdHo)






# Ham tao id chủ xe: Định dạng: User + 5 chữ số
userId = []

def userIdGenerator(length):
    check = 1
    sourceUserIdNumber = []
    lengthOfUserId = len(userId)
    lengthOfSourceUserIdNumber = len(sourceUserIdNumber)
    while lengthOfSourceUserIdNumber < length:
        x = random.randint(10000, 99999)
        for i in range(0, lengthOfSourceUserIdNumber):
            if x == sourceUserIdNumber[i]:
                check = 0
            else:
                check = 1
        if check == 1:
            sourceUserIdNumber.append(x)
            lengthOfSourceUserIdNumber = len(sourceUserIdNumber)
    for j in range(0, lengthOfSourceUserIdNumber):
        string = "User{}"
        string = string.format(sourceUserIdNumber[j])
        userId.append(string)
    print(userId)
        


# Tao ham random bien so xe: Dinh dang BKS- 5 chữ số
licensePlatesArray = []

def licensePlateArrayGenerator (length):
    check = 1
    sourceLicensePlatesNumber = []
    lengthOfLicensePlatesArray = len(licensePlatesArray)
    lengthOfSourceLicensePlatesNumber = len(sourceLicensePlatesNumber)
    while lengthOfSourceLicensePlatesNumber < length:
        x = random.randint(10000, 99999)
        for i in range(0, lengthOfSourceLicensePlatesNumber):
            if x == sourceLicensePlatesNumber[i]:
                check = 0
            else:
                check = 1
        if check == 1:
            sourceLicensePlatesNumber.append(x)
            lengthOfSourceLicensePlatesNumber = len(sourceLicensePlatesNumber)
    for j in range(0, lengthOfSourceLicensePlatesNumber):
        string = "BKS-{}"
        string = string.format(sourceLicensePlatesNumber[j])
        licensePlatesArray.append(string)
    print(licensePlatesArray)
    



# Hàm random số điện thoại
SourcePhoneNumberArray = []
phoneNumberArray = []

def phoneNumberGenerator(length):
    check = 1
    lengthOfSourcePhoneNumberArray = len(SourcePhoneNumberArray)
    while lengthOfSourcePhoneNumberArray < length:
        x = random.randint(100000000, 999999999)
        for i in range(0, lengthOfSourcePhoneNumberArray - 1):
            if x == SourcePhoneNumberArray[i]:
                check = 0
            else:
                check = 1
        if check == 1:
            SourcePhoneNumberArray.append(x)
            lengthOfSourcePhoneNumberArray = len(SourcePhoneNumberArray)
    for j in range(0, lengthOfSourcePhoneNumberArray ):
        string = "0{}"
        string = string.format(SourcePhoneNumberArray[j])
        phoneNumberArray.append(string)
        
    print(phoneNumberArray)
    
# Tao ID xe: Dinh dang: XE + 5 chu so
vehicleId = []
sourceVehicleIdNumber = []

def vehicleIdGenerator(length):
    check = 1
    lengthOfSourceVehicleIdNumber = len(sourceVehicleIdNumber)
    while lengthOfSourceVehicleIdNumber < length:
        x = random.randint(10000, 99999)
        for i in range(0, lengthOfSourceVehicleIdNumber):
            if x == sourceVehicleIdNumber[i]:
                check = 0
            else:
                check = 1
        if check == 1:
            sourceVehicleIdNumber.append(x)
            lengthOfSourceVehicleIdNumber = len(sourceVehicleIdNumber)
    for j in range(0, lengthOfSourceVehicleIdNumber):
        string = "XE{}"
        string = string.format(sourceVehicleIdNumber[j])
        vehicleId.append(string)
    print(vehicleId)
            




def createvaluessArray(length): 
    CardIdGenerator(length)                 # cardIdArray[]
    userNameGenerator(length)               # userNameArray[]
    vehicleCompanyGenerator(length)         # vehicleTypeArray[], vehicleCompanyArray[]
    idHoGenerator(length)                   # userOfIdHo[]
    userIdGenerator(length)                 # userId[]
    licensePlateArrayGenerator(length)      # licensePlatesArray[]
    phoneNumberGenerator(length)            # phoneNumberArray[]
    vehicleIdGenerator(length)              # vehicleId[]


def insertDataIntoThongTinXe(length):
    f = open("test.txt", "w")
    for i in range(0, length):
        string = "insert into Thong_tin_xe values ('{IdXe}', '{IdChuXe}', '{BienSoXe}', '{HangXe}', '{LoaiXe}');\n" 
        string = string.format(
            IdXe = vehicleId[i],
            IdChuXe = userId[i],
            BienSoXe = licensePlatesArray[i],
            HangXe = vehicleCompanyArray[i],
            LoaiXe = vehicleTypeArray[i]
        )
        f.write(string)
    f.close()
        

def insertDataIntoChuXe(length):
    f = open("test.txt", "a")
    for i in range(0, length):
        string = "insert into Chu_xe values ('{IdChuXe}', '{IdHo}', '{TenChuXe}', '{SDT}');\n" 
        string = string.format(
            IdChuXe = userId[i],
            IdHo = userOfIdHo[i],
            TenChuXe = userNameArray[i],
            SDT = phoneNumberArray[i]
        )
        f.write(string)
    f.close()
    
def insertDataIntoThongTinGui(length):
    f = open("test.txt", "a")
    for i in range(0, length):
        string = "insert into Thong_tin_gui values ({Id}, 'M{IdThe}', '{IdXe}');\n" 
        string = string.format(
            Id = i+1,
            IdThe = cardIdArray[i],
            IdXe = vehicleId[i]
        )
        f.write(string)
    f.close()
    
def insertDataIntoThe(length):
    f = open("test.txt", "a")
    for i in range(0, length):
        string = "insert into The values ('M{IdThe}', '{IdChuXe}', '{IdXe}');\n" 
        string = string.format(
            IdThe = cardIdArray[i],
            IdChuXe = userId[i],
            IdXe = vehicleId[i],
        )
        f.write(string)
    f.close() 
    
def insertDataIntoThoiGianGuiLayXe(length):
    f = open("test.txt", "a")
    for i in range(0, length):
        string = "insert into Thoi_gian_gui_lay_xe values ({Id}, 'M{IdThe}');\n" 
        string = string.format(
            Id = i + 1,
            IdThe = cardIdArray[i])
        f.write(string)
    f.close() 


def insertDataIntoHoGiaDinh():
    IdHoGiaDinh = set(userOfIdHo)
    IdHoGiaDinh = list(IdHoGiaDinh)
    print(IdHoGiaDinh)
    f = open("test.txt", "a")
    for i in range(0, len(IdHoGiaDinh)):
        string = "insert into Ho_gia_dinh values ('{IdHo}');\n" 
        string = string.format(
            IdHo = IdHoGiaDinh[i]
        )
        f.write(string)
    f.close()
    
    
# Tạo data cho khách (người không phải người trong chung cư,) sẽ dùng 3 bảng:
# Thông tin xe
# Thông tin gửi
# Thẻ
# Để thể hiện cho khách, ta để thông tin ID chủ thẻ là null (thể hiện người này không có thẻ tháng, chỉ dùng vé ngày)

def insertDataIntoThongTinXeKhach(length):
    f = open("test.txt", "a")
    i = length + 1
    for i in range(i, 2*length):
        string = "insert into Thong_tin_xe values ('{IdXe}', null, '{BienSoXe}', '{HangXe}', '{LoaiXe}');\n" 
        string = string.format(
            IdXe = vehicleId[i],
            IdChuXe = userId[i],
            BienSoXe = licensePlatesArray[i],
            HangXe = vehicleCompanyArray[i],
            LoaiXe = vehicleTypeArray[i]
        )
        f.write(string)
    f.close()
    
def insertDataIntoThongTinGuiKhach(length):
    f = open("test.txt", "a")
    i = length + 1
    for i in range(i, 2*length):
        string = "insert into Thong_tin_gui values ({Id}, 'D{IdThe}', '{IdXe}');\n" 
        string = string.format(
            Id = i,
            IdThe = cardIdArray[i],
            IdXe = vehicleId[i]
        )
        f.write(string)
    f.close()
    
def insertDataIntoTheKhach(length):
    f = open("test.txt", "a")
    i = length + 1
    for i in range(i, 2*length):
        string = "insert into The values ('D{IdThe}', null, '{IdXe}');\n" 
        string = string.format(
            IdThe = cardIdArray[i],
            IdChuXe = userId[i],
            IdXe = vehicleId[i],
        )
        f.write(string)
    f.close() 

createvaluessArray(2*100)
vehicleCompanyArray, vehicleTypeArray = shuffle(vehicleCompanyArray, vehicleTypeArray, random_state=0)

def createInsertData(length):
    
    insertDataIntoThongTinXe(length)
    insertDataIntoChuXe(length)
    insertDataIntoThongTinGui(length)
    insertDataIntoThe(length)
    insertDataIntoThoiGianGuiLayXe(length)
    insertDataIntoHoGiaDinh()
    
    insertDataIntoThongTinXeKhach(length)
    insertDataIntoThongTinGuiKhach(length)
    insertDataIntoTheKhach(length)
createInsertData(100)