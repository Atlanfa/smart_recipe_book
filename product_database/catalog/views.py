from django.shortcuts import render
from .models import Product, Price, Store, Dish, ProductAmount, KitchenUtensil, Profile, BalancedNutritionFormula, HumanAttributes, MenuForOneDay, MenuForMultipleDays
from django.views import generic
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import RenewProductForm, RenewStoreForm, RenewPriceForm, ProductAmountForm, DishForm, RenewKitchenUtensilForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.forms.formsets import formset_factory
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, HumanAttributesForm, DataForCalculatingTheFormulaForm
from .bnfmc import balanced_nutrition_formula_menu_calculation
# Create your views here.


@login_required
def edit_profile(request, pk):

    profile_inst = get_object_or_404(Profile, pk=pk)

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_inst.date_of_birth = profile_form.cleaned_data['date_of_birth']
            profile_inst.sex = profile_form.cleaned_data['sex']
            profile_inst.weight = profile_form.cleaned_data['weight']
            profile_inst.nursing = profile_form.cleaned_data['nursing']
            profile_inst.cpa = profile_form.cleaned_data['cpa']
            profile_inst.city = profile_form.cleaned_data['city']
            profile_inst.country = profile_form.cleaned_data['country']
            profile_inst.location = profile_form.cleaned_data['location']
            profile_inst.save()
            return HttpResponseRedirect(f'{profile_inst.get_absolute_url()}')
    else:
        user_form = UserEditForm(instance=request.user)
        proposed_profile = Profile.objects.filter(id=pk)

        profile_form = ProfileEditForm(initial={'profile': proposed_profile})
    return render(request, 'catalog/edit.html', {'user_form': user_form, 'profile_form': profile_form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'catalog/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'catalog/register.html', {'user_form': user_form})


def index(request):
    num_products = Product.objects.all().count()
    num_prices = Price.objects.all().count()
    num_stores = Store.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(
        request,
        'index.html',
        context={'num_products': num_products, 'num_prices': num_prices, "num_stores": num_stores,
                 'num_visits':num_visits}
    )


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 20


class StoreListView(generic.ListView):
    model = Store
    paginate_by = 20


class PriceListView(generic.ListView):
    model = Price
    paginate_by = 20


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 20


class KitchenUtensilListView(generic.ListView):
    model = KitchenUtensil
    paginate_by = 20


class ProfileDetailView(generic.DetailView):
    model = Profile


class KitchenUtensilDetailView(generic.DetailView):
    model = KitchenUtensil


class DishDetailView(generic.DetailView):
    model = Dish


class ProductDetailView(generic.DetailView):
    model = Product


class StoreDetailView(generic.DetailView):
    model = Store


class UsersFavoriteProductsListView(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = 'catalog/users_favorite_products.html'
    paginate_by = 20

    def get_queryset(self):
        return Product.objects.filter(favorite=self.request.user)


class UsersFavoriteDishesListView(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = 'catalog/users_favorite_dishes.html'
    paginate_by = 20

    def get_queryset(self):
        return Dish.objects.filter(favorite=self.request.user)


class UsersProductsListView(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = 'catalog/users_products.html'
    paginate_by = 20

    def get_queryset(self):
        return Product.objects.filter(who_added=self.request.user)


class UsersDishesListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = 'catalog/users_dishes.html'
    paginate_by = 20

    def get_queryset(self):
        return Dish.objects.filter(who_added=self.request.user)


class UsersKitchenUtensilsListView(LoginRequiredMixin, generic.ListView):
    model = KitchenUtensil
    template_name = 'catalog/users_kitchen_utensils.html'
    paginate_by = 20

    def get_queryset(self):
        return KitchenUtensil.objects.filter(who_added=self.request.user)


class UsersStoresListView(LoginRequiredMixin, generic.ListView):
    model = Store
    template_name = 'catalog/users_stores.html'
    paginate_by = 20

    def get_queryset(self):
        return Store.objects.filter(who_added=self.request.user)


class UsersPricesListView(LoginRequiredMixin, generic.ListView):
    model = Price
    template_name = 'catalog/users_prices.html'
    paginate_by = 20

    def get_queryset(self):
        return Price.objects.filter(who_added=self.request.user)


@csrf_exempt
def add_product_to_favorite(request, product_id):
    for product in Product.objects.filter(id=product_id):
        product.favorite.add(request.user)
    return HttpResponseRedirect(reverse('my-favorite-products'))


@csrf_exempt
def delete_product_from_favorite(request, product_id):
    for product in Product.objects.filter(id=product_id):
        product.favorite.remove(request.user)
    return HttpResponseRedirect(reverse('my-favorite-products'))


@csrf_exempt
def add_dish_to_favorite(request, dish_id):
    for dish in Dish.objects.filter(id=dish_id):
        dish.favorite.add(request.user)
    return HttpResponseRedirect(reverse('my-favorite-dishes'))


@csrf_exempt
def delete_dish_from_favorite(request, dish_id):
    for dish in Dish.objects.filter(id=dish_id):
        dish.favorite.remove(request.user)
    return HttpResponseRedirect(reverse('my-favorite-dishes'))


@login_required
def renew_product(request, pk):

    product_inst = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':

        form = RenewProductForm(request.POST)

        if form.is_valid():
            product_inst.name = form.cleaned_data['name']
            product_inst.save()

            return HttpResponseRedirect(reverse('products') )

    else:
        proposed_product_name = 'Product name'
        form = RenewProductForm(initial={'name': proposed_product_name,})

    return render(request, 'catalog/product_renew.html', {'form': form, 'product_inst': product_inst})


@login_required
def renew_store(request, pk):

    store_inst = get_object_or_404(Store, pk=pk)

    if request.method == 'POST':

        form = RenewStoreForm(request.POST)

        if form.is_valid():
            store_inst.name = form.cleaned_data['name']
            store_inst.country = form.cleaned_data['country']
            store_inst.city = form.cleaned_data['city']
            store_inst.street = form.cleaned_data['street']
            store_inst.location = form.cleaned_data['location']
            store_inst.save()

            return HttpResponseRedirect(reverse('stores') )

    else:
        form = RenewStoreForm()

    return render(request, 'catalog/store_renew.html', {'form': form, 'store_inst': store_inst})


@login_required
def renew_price(request, pk):

    price_inst = get_object_or_404(Price, pk=pk)

    if request.method == 'POST':

        form = RenewPriceForm(request.POST)

        if form.is_valid():
            price_inst.price = form.cleaned_data['price']
            price_inst.save()

            return HttpResponseRedirect(reverse('prices') )

    else:
        proposed_price = Price.objects.filter(id=pk)

        form = RenewPriceForm(initial={'price': proposed_price})

    return render(request, 'catalog/price_renew.html', {'form': form, 'price_inst': price_inst})


@login_required
def create_dish(request):

    product_amount_form_set = formset_factory(ProductAmountForm, min_num=1)

    if request.method == 'POST':
        form = DishForm(request.POST)
        formset = product_amount_form_set(request.POST)
        print(formset.is_valid())
        if form.is_valid() and formset.is_valid():

            dish_inst = Dish()
            dish_inst.name = form.cleaned_data['name']
            dish_inst.recipe = form.cleaned_data['recipe']
            kitchen_utensils = []
            for kitchen_utensil in form.cleaned_data['kitchen_utensils']:
                kitchen_utensils.append(KitchenUtensil.objects.get(id=kitchen_utensil.id))
            dish_inst.who_added = request.user
            dish_inst.save()
            products_amount = []
            for f in formset:
                product_amount = ProductAmount()
                product_amount.product = f.cleaned_data['product']
                product_amount.amount = f.cleaned_data['amount']
                product_amount.unit = f.cleaned_data['unit']
                product_amount.related_model = dish_inst
                product_amount.save()
                products_amount.append(ProductAmount.objects.get(id=product_amount.id))

            dish_inst.products.add(*products_amount)
            dish_inst.kitchen_utensils.add(*kitchen_utensils)

            return HttpResponseRedirect(f'{dish_inst.get_absolute_url()}')

    else:
        form = DishForm()
        formset = product_amount_form_set()

    return render(request, 'catalog/dish_form.html', {'form': form, 'formset': formset})


class BalancedNutritionFormulaDetailView(generic.DetailView):
    model = BalancedNutritionFormula


class BalancedNutritionFormulaListView(generic.ListView):
    model = BalancedNutritionFormula
    paginate_by = 20
    template_name = 'balancednutritionformula_list'


@login_required
def calculate_formula(request):

    if request.method == 'POST':

        form = DataForCalculatingTheFormulaForm(request.POST)
        profile = request.user.profile
        if profile.weight == '' or profile.city == '' or profile.country == '' or profile.date_of_birth == '':
            return HttpResponse('<h1>First fill your profile</h1>')
        else:
            if form.is_valid():
                balanced_nutrition_formula = BalancedNutritionFormula.objects.all().filter(country=profile.country)[0]
                menu_inst = MenuForMultipleDays()
                menu = balanced_nutrition_formula_menu_calculation(Dish.objects.all(), int(form.cleaned_data['amount_of_days']), int(form.cleaned_data['amount_of_money']) , profile, balanced_nutrition_formula)
                menu_inst.save()
                menu_inst.list_of_menus.add(*menu)
                return render(request, 'catalog/calculated_menu.html', {'menu_inst': menu_inst})

    else:
        form = DataForCalculatingTheFormulaForm()

    return render(request, 'catalog/data_for_calculating_the_formula_form.html', {'form': form})


@login_required
def renew_balanced_nutrition_formula(request, pk):

    human_attributes_form_set = formset_factory(HumanAttributesForm, min_num=1)
    balanced_nutrition_formula_inst = get_object_or_404(BalancedNutritionFormula, pk=pk)

    if request.method == 'POST':
        
        formset = human_attributes_form_set(request.POST)
        
        if formset.is_valid():
            for human_attribute in balanced_nutrition_formula_inst.human_attributes:
                human_attribute.delete()
            human_attributes = []
            for f in formset:
                human_attribute = HumanAttributes()
                human_attribute.age = f.cleaned_data['age']
                human_attribute.sex = f.cleaned_data['sex']
                human_attribute.pag = f.cleaned_data['pga']
                human_attribute.cpa = f.cleaned_data['cpa']
                human_attribute.weight = f.cleaned_data['weight']
                human_attribute.proteins_in_100_g = f.cleaned_data['proteins_in_100_g']
                human_attribute.proteins_in_100_g_including_animals = f.cleaned_data['proteins_in_100_g_including_animals']
                human_attribute.fat_in_100_g = f.cleaned_data['fat_in_100_g']
                human_attribute.fat_in_100_g_including_animals = f.cleaned_data['fat_in_100_g_including_animals']
                human_attribute.digestible_carbohydrates_in_100_g = f.cleaned_data['digestible_carbohydrates_in_100_g']
                human_attribute.digestible_carbohydrates_in_100_g_incl_m_and_d = f.cleaned_data['digestible_carbohydrates_in_100_g_incl_m_and_d']
                human_attribute.dietary_fiber_in_100_g = f.cleaned_data['dietary_fiber_in_100_g']
                human_attribute.dietary_fiber_in_100_g_including_fiber_and_pectin = f.cleaned_data['dietary_fiber_in_100_g_including_fiber_and_pectin']
                human_attribute.polyunsaturated_acid = f.cleaned_data['polyunsaturated_acid']
                human_attribute.saturated_acid = f.cleaned_data['saturated_acid']
                human_attribute.monounsaturated_acid = f.cleaned_data['monounsaturated_acid']
                human_attribute.calcium_in_100_g_in_mg = f.cleaned_data['calcium_in_100_g_in_mg']
                human_attribute.phosphorus_in_100_g_in_mg = f.cleaned_data['phosphorus_in_100_g_in_mg']
                human_attribute.magnesium_in_100_g_in_mg = f.cleaned_data['magnesium_in_100_g_in_mg']
                human_attribute.potassium_in_100_g_in_mg = f.cleaned_data['potassium_in_100_g_in_mg']
                human_attribute.sodium_in_100_g_in_mg = f.cleaned_data['sodium_in_100_g_in_mg']
                human_attribute.chlorine_in_100_g_in_mg = f.cleaned_data['chlorine_in_100_g_in_mg']
                human_attribute.sulfur_in_100_g_in_mg = f.cleaned_data['sulfur_in_100_g_in_mg']
                human_attribute.iron_in_100_g_in_mg = f.cleaned_data['iron_in_100_g_in_mg']
                human_attribute.zinc_in_100_g_in_mg = f.cleaned_data['zinc_in_100_g_in_mg']
                human_attribute.iodine_in_100_g_in_mg = f.cleaned_data['iodine_in_100_g_in_mg']
                human_attribute.fluorine_in_100_g_in_mg = f.cleaned_data['fluorine_in_100_g_in_mg']
                human_attribute.thiamine_vitamin_B1_in_100_g_in_mg = f.cleaned_data['thiamine_vitamin_B1_in_100_g_in_mg']
                human_attribute.riboflavin_vitamin_B2_in_100_g_in_mg = f.cleaned_data['riboflavin_vitamin_B2_in_100_g_in_mg']
                human_attribute.pyridoxine_vitamin_B6_in_100_g_in_mg = f.cleaned_data['pyridoxine_vitamin_B6_in_100_g_in_mg']
                human_attribute.pantothenic_acid_vitamin_B3_in_100_g_in_mg = f.cleaned_data['pantothenic_acid_vitamin_B3_in_100_g_in_mg']
                human_attribute.folacin_acid_vitamin_B9_in_100_g_in_mcg = f.cleaned_data['folacin_acid_vitamin_B9_in_100_g_in_mcg']
                human_attribute.cobalamin_acid_vitamin_B12_in_100_g_in_mcg = f.cleaned_data['cobalamin_acid_vitamin_B12_in_100_g_in_mcg']
                human_attribute.niacin_vitamin_PP_in_100_g_in_mg = f.cleaned_data['niacin_vitamin_PP_in_100_g_in_mg']
                human_attribute.ascorbic_acid_vitamin_C_in_100_g_in_mg = f.cleaned_data['ascorbic_acid_vitamin_C_in_100_g_in_mg']
                human_attribute.retinol_vitamin_A_in_100_g_in_mcg = f.cleaned_data['retinol_vitamin_A_in_100_g_in_mcg']
                human_attribute.tocopherol_vitamin_E_in_100_g_in_mg = f.cleaned_data['tocopherol_vitamin_E_in_100_g_in_mg']
                human_attribute.cholecalciferol_vitamin_D_in_100_g_in_mcg = f.cleaned_data['cholecalciferol_vitamin_D_in_100_g_in_mcg']
                human_attribute.energy_value_in_kcal = f.cleaned_data['energy_value_in_kcal']
                human_attribute.related_model = balanced_nutrition_formula_inst
                human_attribute.save()
                human_attributes.append(human_attribute)

            balanced_nutrition_formula_inst.add(*human_attributes)
            return HttpResponseRedirect(f'{balanced_nutrition_formula_inst.get_absolut_url()}')

    else:
        formset = human_attributes_form_set()

    return render(request, 'catalog/balancednutritionformula_renew.html', {'formset': formset, 'balanced_nutrition_formula_inst': balanced_nutrition_formula_inst})


@login_required
def renew_dish(request, pk):

    product_amount_form_set = formset_factory(ProductAmountForm, min_num=1)
    dish_inst = get_object_or_404(Dish, pk=pk)

    if request.method == 'POST':

        form = DishForm(request.POST)
        formset = product_amount_form_set(request.POST)

        if form.is_valid() and formset.is_valid():
            dish_inst.name = form.cleaned_data['name']
            dish_inst.recipe = form.cleaned_data['recipe']
            kitchen_utensils = []
            for kitchen_utensil in form.cleaned_data['kitchen_utensils']:
                kitchen_utensils.append(KitchenUtensil.objects.get(id=kitchen_utensil.id))
            dish_inst.save()
            for product_amount in dish_inst.products:
                product_amount.delete()

            products_amount = []
            for f in formset:
                product_amount = ProductAmount()
                product_amount.product = f.cleaned_data['product']
                product_amount.amount = f.cleaned_data['amount']
                product_amount.unit = f.cleaned_data['unit']
                product_amount.related_model = dish_inst
                product_amount.save()
                products_amount.append(ProductAmount.objects.get(id=product_amount.id))

            dish_inst.products.add(*products_amount)
            dish_inst.kitchen_utensils.add(*kitchen_utensils)

            return HttpResponseRedirect(f'{dish_inst.get_absolute_url()}')

    else:
        form = DishForm()
        formset = product_amount_form_set()

    return render(request, 'catalog/dish_renew.html', {'form': form, 'formset': formset, 'dish_inst': dish_inst})


class DishDelete(DeleteView):
    model = Dish
    success_url = reverse_lazy('dishes')


class KitchenUtensilCreate(CreateView):
    model = KitchenUtensil
    fields = ['name']

    def form_valid(self, form):
        form.instance.who_added = self.request.user
        return super(KitchenUtensilCreate, self).form_valid(form)


class KitchenUtensilDelete(DeleteView):
    model = KitchenUtensil
    success_url = reverse_lazy('kitchen_utensils')


@login_required
def renew_kitchen_utensil(request, pk):

    kitchen_utensil_inst = get_object_or_404(KitchenUtensil, pk=pk)

    if request.method == 'POST':

        form = RenewKitchenUtensilForm(request.POST)

        if form.is_valid():
            kitchen_utensil_inst.price = form.cleaned_data['price']
            kitchen_utensil_inst.save()

            return HttpResponseRedirect(reverse('kitchen_utensils') )

    else:
        proposed_kitchen_utensil = KitchenUtensil.objects.filter(id=pk)

        form = RenewKitchenUtensilForm(initial={'kitchenutensil': proposed_kitchen_utensil})

    return render(request, 'catalog/kitchenutensil_renew.html', {'form': form, 'kitchen_utensil_inst': kitchen_utensil_inst})


class ProductCreate(CreateView):
    model = Product
    fields = [field.name for field in Product._meta.fields if not field.name == 'favorite' and not field.name == 'who_added']

    def form_valid(self, form):
        form.instance.who_added = self.request.user
        return super(ProductCreate, self).form_valid(form)


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products')


class StoreCreate(CreateView):
    model = Store
    fields = ['name', 'country', 'city', 'street', 'location']

    def form_valid(self, form):
        form.instance.who_added = self.request.user
        return super(StoreCreate, self).form_valid(form)


class StoreDelete(DeleteView):
    model = Store
    success_url = reverse_lazy('stores')


class PriceCreate(CreateView):
    model = Price
    fields = ['store', 'product', 'price']
    success_url = reverse_lazy('prices')

    def form_valid(self, form):
        form.instance.who_added = self.request.user
        return super(PriceCreate, self).form_valid(form)


class PriceDelete(DeleteView):
    model = Price
    success_url = reverse_lazy('prices')


