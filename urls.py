from django.conf.urls import url
from theonly import views

urlpatterns = [
    url(r'^$', views.theonlyView, name="theonlyHome"),
    url(r'^menu/$', views.theonlyMenuView, name="theonlyMenu"),
    url(r'^ajax/$', views.ajax_request, name="theonlyajax"),
    url(r'^update_taps/$', views.MenuUpdateTaps, name='updateTaps'),
    url(r'^add/Brewery_Graphic/$', views.AddBrewery_GraphicView, name="AddBrewery_Graphic"),
    url(r'^add/Brewery/$', views.AddBreweryView, name="AddBrewery"),
    url(r'^add/Beverage_Style/$', views.AddBeverage_StyleView, name="AddBeverage_Style"),
    url(r'^add/Beverage_Serving_Size/$', views.AddBeverage_Serving_SizeView, name="AddBeverage_Serving_Size"),
    url(r'^add/Beverage_Serving_Graphic/$', views.AddBeverage_Serving_GraphicView, name="AddBeverage_Serving_Graphic"),
    url(r'^add/Beverage/$', views.AddBeverageView, name="AddBeverage"),
    url(r'^loadBasicData/$', views.loadBasicData, name="loadBasicData"),
]
