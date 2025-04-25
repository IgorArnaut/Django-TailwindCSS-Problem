from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .services import *

# Create your views here.
building_serv = BuildingService()
apartment_serv = ApartmentService()
terms_serv = TermsService()
listing_serv = ListingService()


def index(request):
    listings = listing_serv.get_all()
    return render(request, "index.html", {"listings": listings})


@csrf_exempt
def create(request: HttpRequest):
    context = {}
    building_form = BuildingForm()
    apartment_form = ApartmentForm()
    terms_form = TermsForm()
    listing_form = ListingForm()

    if request.method == "POST":
        building_form = BuildingForm(request.POST)
        apartment_form = ApartmentForm(request.POST)
        terms_form = TermsForm(request.POST)
        listing_form = ListingForm(request.POST)

        if building_form.is_valid():
            building = building_serv.get_or_create(building_form.cleaned_data)

        if apartment_form.is_valid():
            items = apartment_form.cleaned_data.pop("items")
            apartment = apartment_serv.get_or_create(
                building, items, apartment_form.cleaned_data
            )

        if terms_form.is_valid():
            terms = terms_serv.get_or_create(terms_form.cleaned_data)

        if listing_form.is_valid():
            listing = listing_serv.create(apartment, terms, listing_form.cleaned_data)
        return detail(request, listing.id)

    forms = {
        "building_form": building_form,
        "apartment_form": apartment_form,
        "terms_form": terms_form,
        "listing_form": listing_form,
    }
    context["forms"] = forms
    return render(request, "create.html", context)


def detail(request, id):
    listing = listing_serv.get_by_id(id)
    return render(request, "detail.html", {"listing": listing})


@csrf_exempt
def update(request, id):
    context = {}
    listing = listing_serv.get_by_id(id)
    building_form = BuildingForm(instance=listing.apartment.building)
    apartment_form = ApartmentForm(instance=listing.apartment)
    terms_form = TermsForm(instance=listing.terms)
    listing_form = ListingForm(instance=listing)

    if request.method == "POST":
        building_form = BuildingForm(
            instance=listing.apartment.building, data=request.POST
        )
        apartment_form = ApartmentForm(instance=listing.apartment, data=request.POST)
        terms_form = TermsForm(instance=listing.terms, data=request.POST)
        listing_form = ListingForm(instance=listing, data=request.POST)

        if building_form.is_valid():
            building_serv.update(building_form.instance.id, building_form.cleaned_data)

        if apartment_form.is_valid():
            items = apartment_form.cleaned_data.pop("items")
            apartment_serv.update(
                apartment_form.instance.id, items, apartment_form.cleaned_data
            )

        if terms_form.is_valid():
            terms_serv.update(terms_form.instance.id, terms_form.cleaned_data)

        if listing_form.is_valid():
            listing_serv.update(listing_form.instance.id, listing_form.cleaned_data)
        return detail(request, id)

    forms = {
        "building_form": building_form,
        "apartment_form": apartment_form,
        "terms_form": terms_form,
        "listing_form": listing_form,
    }
    context["forms"] = forms
    context["listing"] = listing
    return render(request, "update.html", context)


def delete(request, id):
    listing_serv.delete(id)
    listings = listing_serv.get_all()
    return render(request, "index.html", {"listings": listings})


def search(request):
    search_form = SearchForm()
    context = {}
    context["form"] = search_form
    return render(request, "search.html", context)
