from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Company, Book


class CompanyList(generic.ListView):
    """登録企業の一覧ビュー。確認しやすいように作っただけ."""

    model = Company


class CompanyCreate(generic.CreateView):
    """企業登録."""

    model = Company
    fields = '__all__'
    success_url = reverse_lazy('app:company_list')  # ダミーURL。これがないとエラー

    def form_valid(self, form):
        """登録後、URLのお知らせページに遷移させる.
        
        お知らせページのビューに今登録した企業を教えないとURLを表示できないので
        このような書き方に

        """
        super().form_valid(form)
        return redirect('app:company_create_after', pk=self.object.pk)
        

class CompanyCreateAfter(generic.TemplateView):
    """企業登録後のURLお知らせページ."""

    template_name = 'app/company_after.html'

    def get_context_data(self, *args, **kwargs):
        """その企業の予約ページURLをcontextへ追加."""
        context = super().get_context_data(*args, **kwargs)
        url = reverse(
            'app:company_book',
            kwargs={'pk': self.kwargs['pk']}
        )
        context['url'] = url
        return context


class CompanyBook(generic.CreateView):
    """各企業の予約ビュー."""

    model = Book
    fields = ('date', )

    def get_context_data(self, *args, **kwargs):
        """その企業の予約一覧と、companyをcontextへ追加.
        
        companyを渡し、企業ロゴやタイトルタグを設定させる

        """
        context = super().get_context_data(*args, **kwargs)
        company = Company.objects.get(pk=self.kwargs['pk'])
        book_list = Book.objects.filter(target=company)
        context['book_list'] = book_list
        context['company'] = company
        return context 

    def form_valid(self, form):
        """ForeignKeyなtargetフィールドを指定し、今のページへリダイレクト."""
        book = form.save(commit=False)
        company_pk = self.kwargs['pk']
        company = Company.objects.get(pk=company_pk)
        book.target = company
        book.save()
        return redirect('app:company_book', pk=company_pk)