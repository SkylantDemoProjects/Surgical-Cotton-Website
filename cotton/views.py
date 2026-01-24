from django.shortcuts import render, redirect
from django.http import HttpResponse

# 🏠 Home Page
def home(request):
    return render(request, 'home.html')

# ℹ️ About Page
def about(request):
    return render(request, 'about.html')



# 🧵 Individual Product Pages

# 1️⃣ Absorbent Cotton
def Absorbent_Cotton(request):
    return render(request, 'Absorbent_Cotton.html')

# 2️⃣ Absorbent Gauze Bandage
def Absorbent_Gauze_Bandage(request):
    return render(request, 'Absorbent_Gauze_Bandage.html')

# 3️⃣ Syringe and Needles
def Syringe_and_Needles(request):
    return render(request, 'Syringe_and_Needles.html')

# 4️⃣ Hand Gloves
def Hand_Gloves(request):
    return render(request, 'Hand_Gloves.html')

# 5️⃣ Blood Collection Tubes
def Blood_Collection_Tubes(request):
    return render(request, 'Blood_Collection_Tubes.html')

# zig zag cotton
def zig_zag_cotton(request):
    return render(request, 'zig_zag_cotton.html')

#Gauze_Cloth_Than
def Gauze_Cloth_Than(request):
    return render(request, 'Gauze_Cloth_Than.html')

# 6️⃣ Other Products
def Other_Products(request):
    return render(request, 'Other_Products.html')

# 🩸 Optional Product Detail Page
def product_detail(request, id):
    return render(request, 'product_detail.html', {'id': id})

#Blog page
# def blog(request):
#     return render(request, 'blog.html')


# 📞 Contact Page
def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse

def enquire(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print(f"Enquiry Received: {name}, {email}, {message}")
        return HttpResponse("✅ Thank you! Your enquiry has been submitted.")
    return HttpResponse("Invalid request")
