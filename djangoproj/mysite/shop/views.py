from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.db.models import F
from django.views import generic
from .models import Product, Image



def index(request):
    product_list=Product.objects.all()
    cart_sum = 0
    for product in product_list:
        cart_sum = cart_sum+product.in_cart_number
    context = {'product_list': product_list, 'cart_sum': cart_sum}
    return render(request, 'shop/index.html', context)


# question_id variable name must be the same as defined in the regex
# ?P<question_id>


# class IndexView(generic.ListView):
#     template_name = 'shop/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]
#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'shop/cart.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'shop/results.html'
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'shop/cart.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         # using F finction to avoid race condition in database
#         selected_choice.votes=F('votes')+1
#         # selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('shop:results', args=(question.id,)))
#
#
def bought(request):
    product_list=Product.objects.filter(in_cart_number__gte=1)
    total_price_dict={}
    for item in product_list:
        total_price_dict[item.id]=item.in_cart_number*item.official_price
    context = {'product_list': product_list, 'total_price_dict': total_price_dict}
    return render(request, 'shop/cart.html', context)


def add_to_cart(request):
    selected_prod = get_object_or_404(Product, pk=request.POST['product_bought'])

    product = get_object_or_404(Product, pk=selected_prod.id)
    product.in_cart_number=F('in_cart_number')+1
    product.save()
    return HttpResponseRedirect(reverse('shop:index'))
