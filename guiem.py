- import datetime

def birthday_wish_marri():
    today = datetime.date.today()
    marri_birthday = datetime.date(today.year, 10, 26)
    age = today.year - 2007  # Marri sinh năm 2007

    if today == marri_birthday:
        message = f"Chào mừng vk đến với thế giới 17 năm trước 🎉🎂 Sinh nhật vui vẻ nhé nàng công chúa của anh! Chúc vk sẽ tìm được một người tốt hơn anh 😋"
    else:
        days_left = (marri_birthday - today).days
        if days_left < 0:
            # Nếu hôm nay đã qua ngày 26/10 thì tính số ngày cho năm sau
            marri_birthday = datetime.date(today.year + 1, 10, 26)
            days_left = (marri_birthday - today).days
        message = f"Hi Marri! Chỉ còn {days_left} ngày nữa là đến sinh nhật bạn vào ngày 26/10! 🎁🎈 Sẵn sàng cho một ngày đầy niềm vui và bánh sinh nhật rồi chứ? 🌸🐱"

    return message

# Chạy hàm
print(birthday_wish_marri())
