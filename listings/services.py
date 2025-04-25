from django.shortcuts import get_object_or_404

from listings.models import *


class BuildingService:
    def get_or_create(self, data):
        building, created = Building.objects.get_or_create(**data)
        print("Building created:", created)
        return building

    def update(self, id, data):
        Building.objects.filter(id=id).update(**data)


class ApartmentService:
    def get_or_create(self, building, items, data):
        apartment, created = Apartment.objects.get_or_create(building=building, **data)
        print("Apartment created:", created)

        if created:
            apartment.items.set(items)

        return apartment

    def update(self, id, items, data):
        Apartment.objects.filter(id=id).update(**data)
        apartment = Apartment.objects.get(id=id)
        apartment.items.set(items)


class TermsService:
    def get_or_create(self, data):
        terms, created = Terms.objects.get_or_create(**data)
        print("Terms created:", created)
        return terms

    def update(self, id, data):
        Terms.objects.filter(id=id).update(**data)


class ListingService:
    def get_all(self):
        return Listing.objects.all()

    def get_by_id(self, id):
        return get_object_or_404(Listing, id=id)

    def create(self, apartment, terms, data):
        listing, created = Listing.objects.get_or_create(
            apartment=apartment, terms=terms, **data
        )
        return listing

    def update(self, id, data):
        Listing.objects.filter(id=id).update(**data)

    def delete(self, id):
        listing = get_object_or_404(Listing, id=id)
        listing.delete()
