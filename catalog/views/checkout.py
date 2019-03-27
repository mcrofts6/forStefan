
    #handle the form
    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        form.sale = request.user.get_shopping_cart()
        if form.is_valid():
            #clean already finalized sale
            return


        #render the page
        return request.dmp.render('checkout.html',{
            'cart': cart,
            'form': form,
        })



class CheckoutForm(forms.Form)
    address = forms.CharField(label='Shipping Address')
    city = forms.CharField(label='Shipping City')
    state = forms.CharField(label='Shipping State')
    zipcode = forms.CharField(label='Shipping Zip')
    stripeToken = forms.CharField(widget=forms.HiddenInput())
    #for testing you could change the stripeToken to just a CharField without the hidden input

    def clean(self):
        try:
            self.sale.finalize(self.cleaned_data['stripeToken'])
        except Exception as e:
            raise forms.ValidationError('Error processing payment: {}'.format(e))