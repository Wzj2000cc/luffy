from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    # page_query_param = 'pp' 默认使用page参数进行页码设置
    page_size = 5   # 默认每页显示5条数据
    page_size_query_param = 'size'  # 可以根据size参数调整每页显示的数据条数
    max_page_size = 20  # 最大显示