from myapp.models import Person, Musician, Album, Student
from datetime import date
from django.db.models import Q

Person.objects.filter(first_name__startswith="Test").delete()
Student.objects.filter(name__startswith="Test").delete()

# Creating objects
person = Person(first_name="John", last_name="Lennon")
person.save()

person2 = Person.objects.create(first_name="Paul", last_name="McCartney")

# Saving changes
person.first_name = "Johnny"
person.save()

# Retrieving all objects
all_people = Person.objects.all()
print(f"All people: {list(all_people)}")

# Filtering objects
johns = Person.objects.filter(first_name="Johnny")
not_johns = Person.objects.exclude(first_name="Johnny")
print(f"Johns: {list(johns)}")
print(f"Not Johns: {list(not_johns)}")

# Chaining filters
Person.objects.create(first_name="George", last_name="Harrison")
Person.objects.create(first_name="Ringo", last_name="Starr")

beatles = Person.objects.filter(
    last_name__in=["Lennon", "McCartney", "Harrison", "Starr"]
).exclude(
    first_name="Johnny"
).filter(
    first_name__startswith="P"
)
print(f"Beatles starting with P: {list(beatles)}")

# Get single object
try:
    paul = Person.objects.get(first_name="Paul")
    print(f"Found Paul: {paul}")
except Person.DoesNotExist:
    print("Paul not found")
except Person.MultipleObjectsReturned:
    print("Multiple Pauls found")

try:
    fake = Person.objects.get(first_name="NonExistent")
except Person.DoesNotExist:
    print("DoesNotExist works correctly")

# Field lookups
Student.objects.create(name="Alice Johnson", year_in_school="FR")
Student.objects.create(name="Bob Smith", year_in_school="SO")
Student.objects.create(name="Carol Johnson", year_in_school="JR")

johnsons = Student.objects.filter(name__contains="Johnson")
a_names = Student.objects.filter(name__startswith="A")
bob_ci = Student.objects.filter(name__icontains="bob")
upperclass = Student.objects.filter(year_in_school__in=["JR", "SR", "GR"])

print(f"Johnsons: {list(johnsons)}")
print(f"Names with A: {list(a_names)}")
print(f"Bob (case-insensitive): {list(bob_ci)}")
print(f"Upperclass: {list(upperclass)}")

# Relationships
musician = Musician.objects.create(
    first_name="Bob",
    last_name="Dylan",
    instrument="Guitar"
)

album1 = Album.objects.create(
    artist=musician,
    name="Highway 61 Revisited",
    release_date=date(1965, 8, 30),
    num_stars=5
)

album2 = Album.objects.create(
    artist=musician,
    name="Blonde on Blonde",
    release_date=date(1966, 6, 20),
    num_stars=4
)

print(f"Album artist: {album1.artist}")
musician_albums = musician.album_set.all()
print(f"Musician albums: {list(musician_albums)}")

guitar_albums = Album.objects.filter(artist__instrument="Guitar")
five_star_musicians = Musician.objects.filter(album__num_stars=5)
print(f"Guitar albums: {list(guitar_albums)}")
print(f"5-star musicians: {list(five_star_musicians)}")

# Q objects
john_or_paul = Person.objects.filter(Q(first_name="Johnny") | Q(first_name="Paul"))
good_albums = Album.objects.filter(Q(num_stars__gte=4) & Q(release_date__year__gte=1965))
not_freshmen = Student.objects.filter(~Q(year_in_school="FR"))

print(f"Johnny OR Paul: {list(john_or_paul)}")
print(f"Good albums 1965+: {list(good_albums)}")
print(f"Not freshmen: {list(not_freshmen)}")

# Deleting objects
to_delete = Person.objects.create(first_name="ToDelete", last_name="Test")
to_delete.delete()

Student.objects.create(name="TestDelete1", year_in_school="FR")
Student.objects.create(name="TestDelete2", year_in_school="FR")
deleted_count, details = Student.objects.filter(name__startswith="TestDelete").delete()
print(f"Deleted {deleted_count} test students")

# Related object methods
album_count = musician.album_set.count()
high_rated = musician.album_set.filter(num_stars__gte=4)
new_album = musician.album_set.create(
    name="New Album",
    release_date=date.today(),
    num_stars=3
)

print(f"Album count: {album_count}")
print(f"High rated: {list(high_rated)}")
print(f"Created via manager: {new_album}")

print("Queries lab completed")