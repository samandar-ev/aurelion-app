from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

# main urls for the app, not splitting into many files yet
urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('health/', views.health, name='health'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('associate/', views.SalesAssociateDashboardView.as_view(), name='associate_dashboard'),
    
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/new/luxury/', views.LuxuryProductCreateView.as_view(), name='luxury_product_create'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/archived/', views.ArchivedProductListView.as_view(), name='archived_product_list'),
    path('products/<int:pk>/archive/', views.ArchiveProductView.as_view(), name='archive_product'),
    path('products/<int:pk>/unarchive/', views.UnarchiveProductView.as_view(), name='unarchive_product'),
    
    path('barcodes/', views.BarcodeGeneratorView.as_view(), name='barcode_generator'),
    path('barcodes/generate/', views.BarcodeGeneratePDFView.as_view(), name='barcode_generate_pdf'),
    
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('clients/new/', views.ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('clients/<int:pk>/edit/', views.ClientUpdateView.as_view(), name='client_edit'),
    
    path('pos/', views.POSView.as_view(), name='pos'),
    path('pos/checkout/', views.POSCheckoutView.as_view(), name='pos_checkout'),
    path('pos/preview-discount/', views.POSPreviewDiscountView.as_view(), name='pos_preview_discount'),
    path('pos/return/', views.POSReturnView.as_view(), name='pos_return'),
    path('pos/return/lookup/', views.POSReturnLookupView.as_view(), name='pos_return_lookup'),
    path('pos/return/checkout/', views.POSReturnCheckoutView.as_view(), name='pos_return_checkout'),
    
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    
    path('promotions/', views.PromotionListView.as_view(), name='promotion_list'),
    path('promotions/new/', views.PromotionCreateView.as_view(), name='promotion_create'),
    path('promotions/<int:pk>/edit/', views.PromotionUpdateView.as_view(), name='promotion_edit'),
    path('promotions/<int:pk>/delete/', views.PromotionDeleteView.as_view(), name='promotion_delete'),
    path('promotions/<int:pk>/toggle/', views.PromotionToggleView.as_view(), name='promotion_toggle'),
    
    path('reports/', views.ReportView.as_view(), name='reports'),
    path('reports/export/', views.ReportExportView.as_view(), name='report_export'),
    
    path('personnel/', views.PersonnelListView.as_view(), name='personnel_list'),
    path('personnel/new/', views.PersonnelCreateView.as_view(), name='personnel_create'),
    path('personnel/<int:pk>/delete/', views.PersonnelDeleteView.as_view(), name='personnel_delete'),
]
