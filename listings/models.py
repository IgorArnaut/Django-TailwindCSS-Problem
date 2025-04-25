from django.db import models


# Create your models here.
class Building(models.Model):
    city = models.CharField(max_length=255, verbose_name="Grad")
    street = models.CharField(max_length=255, verbose_name="Ulica")
    street_num = models.IntegerField(verbose_name="Broj ulice")
    constructed_in = models.IntegerField(verbose_name="Izgrađen")
    num_of_floors = models.IntegerField(verbose_name="Spratnost")
    parking = models.BooleanField(verbose_name="Parking")
    garage = models.BooleanField(verbose_name="Graža")
    elevator = models.BooleanField(verbose_name="Lift")
    cctv = models.BooleanField(verbose_name="Video nadzor")
    intercom = models.BooleanField(verbose_name="Interfon")

    class Meta:
        db_table = "building"
        verbose_name = "Zgrada"
        verbose_name_plural = "Zgrade"

    def __str__(self):
        return f"{self.street} {self.street_num}, {self.city}"


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Naziv")

    class Meta:
        db_table = "item"
        verbose_name = "Stvar"
        verbose_name_plural = "Stvari"

    def __str__(self):
        return self.name


class Apartment(models.Model):
    location = models.CharField(max_length=255, verbose_name="Lokacija")
    floor = models.IntegerField(verbose_name="Sprat")
    area = models.IntegerField(verbose_name="Površina")
    price = models.IntegerField(verbose_name="Cena")
    num_of_rooms = models.IntegerField(verbose_name="Broj soba")
    state = models.CharField(max_length=255, verbose_name="Stanje")
    heating = models.CharField(max_length=255, verbose_name="Grejanje")
    equipment = models.CharField(max_length=255, verbose_name="Opremljenost")
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, verbose_name="Zgrada"
    )
    items = models.ManyToManyField(Item, verbose_name="Stvari")

    class Meta:
        db_table = "apartment"

    def __str__(self):
        return f"{self.location}, {self.area} m2, {self.price} EUR, {self.num_of_rooms} soba"


class Terms(models.Model):
    available = models.DateField(verbose_name="Useljiv")
    deposit = models.BooleanField(verbose_name="Depozit")
    for_students = models.BooleanField(verbose_name="Za studente")
    for_workers = models.BooleanField(verbose_name="Za radnike")
    smoking_allowed = models.BooleanField(verbose_name="Dozvoljeno pušenje")
    pets_allowed = models.BooleanField(verbose_name="Dozvoljeni ljubimci")

    class Meta:
        db_table = "terms"
        verbose_name = "Uslovi zakupa"
        verbose_name_plural = "Uslovi zakupa"

    def __str__(self):
        s = f"{self.available}"
        if self.deposit:
            s += ", depozit"
        if self.for_students:
            s += ", za studente"
        if self.for_workers:
            s += ", za radnike"
        if self.smoking_allowed:
            s += ", dozvoljeno pušenje"
        if self.pets_allowed:
            s += ", dozvoljeni ljubimci"
        return s


class Listing(models.Model):
    title = models.CharField(max_length=255, verbose_name="Naslov")
    description = models.TextField(verbose_name="Opis")
    apartment = models.ForeignKey(
        Apartment, on_delete=models.CASCADE, verbose_name="Stan"
    )
    terms = models.ForeignKey(
        Terms, on_delete=models.CASCADE, verbose_name="Uslovi zakupa"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Postavljen")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ažuriran")

    class Meta:
        db_table = "listing"
        verbose_name = "Oglas"
        verbose_name_plural = "Oglasi"

    def __str__(self):
        return self.title
