monthconversions= {
    "Jan": "january",
    "Feb": "February",
    "Mar": "March"

}
print(monthconversions["Mar"])
print(monthconversions.get("Feb"))
print(monthconversions.get("luv", "not found it"))

i=1
while i <= 10:
    print(i)
    i += 1
print("done with loop")


