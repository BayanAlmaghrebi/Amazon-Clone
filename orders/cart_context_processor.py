from .models import Cart , CartDetail


def get_cart_data(request):
    if request.user.is_authenticated:   # هل اليوزر مسجل دخول او لاء
        cart , created = Cart.objects.get_or_create(user=request.user , status='Inprogress' ) # user=request.user يعني اليوزر هو اليوزر الحالي اللي مسجل دخول
               # created نوعو بوليان و قيمتو True or Faulse
        cart_detail = CartDetail.objects.filter(cart=cart) #لمعرفة تفاصيل السلة منروح على  cart_detail ومنرجع كلشي موجود بالسلة تبع اليوزر 
        return{'cart_data':cart , 'cart_detail_data':cart_detail}
    

    else:
        return{}